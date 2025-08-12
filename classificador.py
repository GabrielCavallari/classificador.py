import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import unidecode
import string

# ---------------------------
# Função de pré-processamento
# ---------------------------
def limpar_texto(texto):
    texto = texto.lower()  # tudo minúsculo
    texto = unidecode.unidecode(texto)  # remove acentos
    texto = texto.translate(str.maketrans("", "", string.punctuation))  # remove pontuação
    return texto

# ---------------------------
# 1. Ler dataset
# ---------------------------
dados = pd.read_csv("dataset.csv")

# Aplicar limpeza no dataset
dados['mensagem'] = dados['mensagem'].apply(limpar_texto)

# ---------------------------
# 2. Vetorização
# ---------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dados['mensagem'])
y = dados['categoria']

# ---------------------------
# 3. Treinar modelo
# ---------------------------
modelo = MultinomialNB()
modelo.fit(X, y)

print("✅ Modelo treinado com sucesso!")

# ---------------------------
# 4. Classificação interativa
# ---------------------------
while True:
    mensagem = input("\nDigite uma mensagem (ou 'sair' para encerrar): ")
    if mensagem.lower() == "sair":
        break
    
    mensagem_limpa = limpar_texto(mensagem)
    X_teste = vectorizer.transform([mensagem_limpa])
    categoria_prevista = modelo.predict(X_teste)[0]
    
    print(f"📌 Classificação: {categoria_prevista}")

# Classificador de Textos

Um projeto simples em Python que utiliza aprendizado de máquina para classificar mensagens de texto como **spam** ou **não-spam**, servindo como base para sistemas de filtragem de conteúdo ou integração com chatbots.

## 📌 Objetivo
O objetivo deste projeto é demonstrar como criar um classificador de texto utilizando **machine learning** e **processamento de linguagem natural (NLP)**, aplicando conceitos como:
- Pré-processamento de dados
- Extração de características
- Treinamento de modelos
- Avaliação de desempenho

Este tipo de projeto pode ser integrado a sistemas maiores, como:
- Chatbots (ex.: WhatsApp, Telegram)
- Sistemas de atendimento automático
- Filtros de e-mail ou mensagens

---

## ⚙️ Como funciona
1. **Coleta de dados** – O projeto utiliza um conjunto de mensagens pré-classificadas como spam ou não-spam.
2. **Pré-processamento** – Conversão de texto para minúsculas, remoção de pontuações e stopwords.
3. **Vetorização** – Transformação do texto em vetores numéricos usando `CountVectorizer` ou `TfidfVectorizer`.
4. **Treinamento do modelo** – Utiliza algoritmos de classificação, como Naive Bayes.
5. **Avaliação** – Mede a acurácia e outras métricas para validar o modelo.
6. **Predição** – O usuário pode inserir uma frase e receber a classificação.

---

## 🛠 Tecnologias utilizadas
- **Python 3**
- **scikit-learn** – Treinamento e avaliação do modelo
- **pandas** – Manipulação de dados
- **numpy** – Operações matemáticas
- **nltk** – Processamento de linguagem natural

- ## Funcionalidades
- Treinamento de modelo de classificação de textos
- Entrada personalizada do usuário
- Saída com a categoria prevista
- Salvamento e carregamento do modelo treinado

## Como executar o projeto

```bash
# 1. Clone este repositório
git clone https://github.com/GabrielCavallari/classificador.py.git

# 2. Acesse a pasta do projeto
cd classificador.py

# 3. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv

# 4. Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Execute o script principal
python main.py

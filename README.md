# projeto-imoveis-ml
Projeto de Previsão de Preços de Imóveis com Machine Learning

# 📊 Previsão de Aluguel em São Paulo com Machine Learning

Este é um projeto de Machine Learning com foco em regressão preditiva. O objetivo é prever o valor total de aluguel de um imóvel em São Paulo com base em algumas características simples do imóvel.

A ideia surgiu da curiosidade: "será que consigo estimar o aluguel de um imóvel só com dados básicos?" — e o resultado foi melhor do que eu esperava!

---

## 🚀 O que o projeto faz

Usando um modelo de **Random Forest Regressor**, o sistema é capaz de estimar o valor total do aluguel com base em:

- Bairro
- Tipo de imóvel
- Área útil (m²)
- Número de quartos
- Vagas na garagem

Tudo isso dentro de uma interface interativa feita com **Streamlit**, onde o usuário pode testar em tempo real.

---

## 💻 Tecnologias utilizadas

- Python 3.11
- pandas
- scikit-learn
- joblib
- Streamlit

---

## 🧠 Modelo de Machine Learning

- Tipo: Regressão
- Algoritmo: Random Forest
- Avaliação: RMSE (erro quadrático médio)

> ⚠️ O dataset utilizado é limitado em tamanho, então os resultados ainda podem melhorar com mais dados. Mas a estrutura do projeto já demonstra o potencial da abordagem.

---

## ▶️ Como rodar localmente

1. Clone este repositório:

git clone https://github.com/KfcSerpa/projeto-imoveis-ml.git

2. Instale os pacotes:
pip install -r requisitos.txt

3. Rode o app:
streamlit run Previsao_imoveis.py

Créditos:
- Dataset obtido no Kaggle
- Desenvolvido por KfcSerpa

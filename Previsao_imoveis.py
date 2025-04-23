import streamlit as st
import joblib
import pandas as pd

# Carrega o modelo treinado
modelo = joblib.load('modelo_imoveis.pkl')

st.title('Previsão de Aluguel em SP')

# Inputs do usuário
district = st.selectbox('Bairro', ['Belenzinho', 'Vila Marieta', 'Pinheiros', 'Vila Ré', 'Bela Vista', 'Brás', 'Brooklin Paulista', 'Centro', 'Piqueri', 'Vila Aricanduva', 'Sé', 'Tatuapé', 'Lauzane Paulista', 'Jardim Paraventi', 'Cambuci', 'Liberdade', 'Cidade Monções', 'Água Branca'])
tipo = st.selectbox('Tipo', ['Studio e kitnet', 'Apartamento', 'Casa em condomínio', 'Casa'])
area = st.slider('Área (m²)', 10, 100, 30)
bedrooms = st.slider('Quartos', 1, 5, 1)
garage = st.slider('Vagas na garagem', 0, 3, 0)

# Previsão
input_df = pd.DataFrame([[district, area, bedrooms, garage, tipo]], 
                        columns=['district', 'area', 'bedrooms', 'garage', 'type'])

if st.button('Prever valor total'):
    resultado = modelo.predict(input_df)[0]
    st.success(f'Valor estimado: R$ {resultado:,.2f}')

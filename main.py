import pandas as pd
import joblib
import streamlit as st

x_numericos = {'latitude': 0, 'longitude': 0, 'bedrooms': 0, 'amenities_number': 0, 'extra_people': 0,
               'accommodates': 0,
               'bathrooms': 0, 'beds': 0, 'minimum_nights': 0, 'host_listings_count': 0, 'ano': 0, 'mes': 0,
               'guests_included': 0}

x_tf = {'instant_bookable': 0, 'host_identity_verified': 0}

x_listas = {'property_type': ['Apartment', 'House', 'Condominium', 'Loft', 'Serviced apartment', 'Bed and breakfast',
                              'Guesthouse', 'Hostel', 'Guest suite', 'Outros'],
            'room_type': ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room']}

dicionario_auxiliar = {}

for key, val in x_listas.items():
    for item in val:
        dicionario_auxiliar[f'{key}_{item}'] = 0

for item in x_numericos:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format='%.5f')

    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)

    else:
        valor = st.number_input(f'{item}', step=1, value=0)

    x_numericos[item] = valor

for item in x_tf:
    tf = st.selectbox(f'{item}', ('Sim', 'Não'))

    if tf == 'Sim':
        x_tf[item] = 1
    else:
        x_tf[item] = 0

for key, val in x_listas.items():
    lists = st.selectbox(f'{key}', val)
    dicionario_auxiliar[f'{key}_{lists}'] = 1

botao_calcular = st.button('Prever Valor do Imóvel')

if botao_calcular:
    dicionario_auxiliar.update(x_numericos)
    dicionario_auxiliar.update(x_tf)
    valores_x = pd.DataFrame(dicionario_auxiliar, index=[0])
    modelo = joblib.load('modelo_extratrees.joblib')
    preco = modelo.predict(valores_x)
    st.write(f'O valor previsto foi de R$ {preco[0]}')

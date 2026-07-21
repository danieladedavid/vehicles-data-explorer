import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.title('Análise de anúncios de veículos')

st.write(
    'Este aplicativo permite explorar os dados de anúncios de veículos '
    'por meio de gráficos interativos.')

st.subheader('Visualização dos dados')

show_data = st.checkbox('Mostrar uma amostra dos dados')

if show_data:
    st.dataframe(car_data.head(20), use_container_width=True)

st.subheader('Quantidade de anúncios por tipo de veículo')

type_counts = car_data['type'].value_counts().reset_index()
type_counts.columns = ['type', 'count']

fig = px.bar(
    type_counts,
    x='type',
    y='count',
    title='Quantidade de anúncios por tipo de veículo',
    labels={'type': 'Tipo de veículo', 'count': 'Quantidade de anúncios'})

st.plotly_chart(fig, use_container_width=True)

st.subheader('Distribuição da quilometragem')

fig = px.histogram(
    car_data,
    x='odometer',
    color='type',
    title='Distribuição da quilometragem por tipo de veículo',
    labels={'odometer': 'Quilometragem', 'type': 'Tipo de veículo'})

st.plotly_chart(fig, use_container_width=True)

st.subheader('Comparação de preços entre tipos de veículos')

vehicle_types = sorted(car_data['type'].dropna().unique())

type_1 = st.selectbox(
    'Selecione o primeiro tipo de veículo',
    vehicle_types,
    index=0)

type_2 = st.selectbox(
    'Selecione o segundo tipo de veículo',
    vehicle_types,
    index=1)

normalize = st.checkbox('Normalizar histograma')

filtered_data = car_data[
    car_data['type'].isin([type_1, type_2])]

histogram_normalization = 'percent' if normalize else None

fig = px.histogram(
    filtered_data,
    x='price',
    color='type',
    barmode='overlay',
    histnorm=histogram_normalization,
    title='Comparação da distribuição de preços entre tipos de veículos',
    labels={'price': 'Preço', 'type': 'Tipo de veículo'},
    opacity=0.7)

st.plotly_chart(fig, use_container_width=True)

st.subheader('Relação entre preço e quilometragem')

selected_type = st.selectbox(
    'Selecione um tipo de veículo para o gráfico de dispersão',
    vehicle_types)

scatter_data = car_data[car_data['type'] == selected_type]

fig = px.scatter(
    scatter_data,
    x='odometer',
    y='price',
    color='condition',
    title=f'Relação entre preço e quilometragem: {selected_type}',
    labels={
        'odometer': 'Quilometragem',
        'price': 'Preço',
        'condition': 'Condição'})

st.plotly_chart(fig, use_container_width=True)
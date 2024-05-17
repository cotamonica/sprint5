#proyecto sprint5
import pandas as pd 
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv') 

# Crear las casillas de verificación
histograma = st.checkbox('Mostrar histograma')
grafico_dispersion = st.checkbox('Mostrar gráfico de dispersión')
grafico_barras = st.checkbox('Mostrar gráfico de barras')

# Filtrar los datos para incluir solo vehículos con condición "excellent" y model_year >= 2000
filtered_data = car_data[(car_data['condition'] == 'excellent') & (car_data['model_year'] >= 2000)]

# Ordenar los datos por 'model_year' de forma ascendente
filtered_data = filtered_data.sort_values(by='model_year')

# Obtener los modelos únicos para crear un mapa de colores
unique_models = filtered_data['model'].unique()

# Crear un mapa de colores personalizado
color_map = {model: px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)] for i, model in enumerate(unique_models)}

# Casilla de histograma
if histograma:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", color_discrete_sequence=['blue'])
    st.plotly_chart(fig, use_container_width=True)

# Casilla de grafico de dispersión
if grafico_dispersion:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price", color_discrete_sequence=['blue'])
    st.plotly_chart(fig, use_container_width=True)

# Casilla de grafico de pastel
if grafico_barras:
    st.write('Distribución de tipos de vehículos')
    fig = px.bar(filtered_data, x='model_year', y='price', color='model', title='Precios de Vehículos en Condición Excelente por Año de Modelo (2000 en adelante)', labels={'price': 'Precio', 'model_year': 'Año de Modelo'}, hover_data=['model'], color_discrete_map=color_map)
    st.plotly_chart(fig)
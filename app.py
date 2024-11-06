import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')  # Asegúrate de que el archivo está en la misma carpeta o proporciona la ruta correcta

# Título de la aplicación
st.title("Análisis de Datos de Vehículos")

# Encabezado
st.header("Visualización de Datos de Vehículos")

# Botón para construir el histograma
hist_button = st.button('Construir histograma')  # Crear un botón

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma de la columna 'odometer'
    fig_histogram = px.histogram(car_data, x="odometer", title="Histograma de Odometer")
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_histogram, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')  # Crear un segundo botón

if scatter_button:  # Al hacer clic en el segundo botón
    st.write('Creación de un gráfico de dispersión entre Odometer y Price')
    
    # Crear el gráfico de dispersión entre 'odometer' y 'price'
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odometer vs Price")
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

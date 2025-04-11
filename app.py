import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
df = pd.read_csv('./vehicles_us.csv')

# Encabezado principal
st.title('🚗 Panel interactivo de anuncios de vehículos')

# Descripción introductoria
st.markdown("""
Bienvenida/o al panel de control interactivo. Aquí podrás explorar los datos de anuncios de vehículos usados.
Usa las casillas de verificación para mostrar distintos gráficos y comprender mejor los datos disponibles.
""")

# Mostrar datos crudos (opcional)
if st.checkbox('Mostrar datos crudos', key='crudos'):
    st.write(df.head(10))

# Histograma: Distribución del odómetro
if st.checkbox('Mostrar histograma del odómetro', key='hist_odometro'):
    st.subheader('Distribución del odómetro')
    fig = px.histogram(df, x='odometer', nbins=30, title='Histograma del odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Histograma adicional (opcional): Distribución del precio
if st.checkbox('Mostrar histograma del precio', key='hist_precio'):
    st.subheader('Distribución del precio')
    fig_price = px.histogram(df, x='price', nbins=30, title='Histograma del precio')
    st.plotly_chart(fig_price, use_container_width=True)

# Gráfico de dispersión: precio vs odómetro
if st.checkbox('Mostrar scatter plot: precio vs odómetro', key='scatter_precio_odometro'):
    st.subheader('Relación entre odómetro y precio')
    fig2 = px.scatter(
        df, x='odometer', y='price',
        title='Precio según el odómetro',
        labels={'odometer': 'Odómetro', 'price': 'Precio'}
    )
    st.plotly_chart(fig2, use_container_width=True)

# Boxplot: Precio por tipo de transmisión
if st.checkbox('Mostrar gráfico de cajas: precio por tipo de transmisión', key='boxplot_transmision'):
    st.subheader('Precio por tipo de transmisión')
    fig3 = px.box(
        df, x='transmission', y='price',
        title='Distribución del precio por tipo de transmisión'
    )
    st.plotly_chart(fig3, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Proyecto Sprint 7 | Lunita 🌙")

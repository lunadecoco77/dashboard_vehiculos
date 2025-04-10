import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('./vehicles_us.csv')


# Encabezado de la app
st.header('Panel interactivo de anuncios de vehículos 🚗')

# Checkbox para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Distribución del odómetro:')
    fig = px.histogram(df, x='odometer', nbins=30)
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter plot
if st.checkbox('Mostrar scatter plot: precio vs odómetro'):
    st.write('Relación entre odómetro y precio:')
    fig2 = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)

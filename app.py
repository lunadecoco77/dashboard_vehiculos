import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('./vehicles_us.csv')


# Encabezado de la app
st.header('Panel interactivo de anuncios de vehículos')

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


# Histograma del odómetro
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Distribución del odómetro:')
    fig1 = px.histogram(df, x='odometer', nbins=30)
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico de barras: modelos más comunes
if st.checkbox('Mostrar los modelos más comunes'):
    st.write('Modelos más comunes en los anuncios:')
    top_models = df['model'].value_
# Checkbox para gráfico de transmisiones
if st.checkbox('Mostrar gráfico de transmisiones'):
    st.write('Cantidad de vehículos por tipo de transmisión:')
    fig3 = px.bar(df['transmission'].value_counts().reset_index(),
                  x='index', y='transmission',
                  labels={'index': 'Tipo de transmisión', 'transmission': 'Cantidad'})
    st.plotly_chart(fig3, use_container_width=True)
# Checkbox para gráfico de cajas por condición
if st.checkbox('Mostrar gráfico de cajas por condición'):
    st.write('Distribución del precio según la condición del vehículo:')
    fig4 = px.box(df, x='condition', y='price', points='all')
    st.plotly_chart(fig4, use_container_width=True)
# Selector de fabricante con scatter filtrado
fabricante = st.selectbox('Selecciona un fabricante para analizar:', df['manufacturer'].dropna().unique())

df_filtrado = df[df['manufacturer'] == fabricante]

if not df_filtrado.empty:
    st.write(f'Gráfico de odómetro vs precio para {fabricante}:')
    fig5 = px.scatter(df_filtrado, x='odometer', y='price')
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.warning('No hay datos para ese fabricante.')
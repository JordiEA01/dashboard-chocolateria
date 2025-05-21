import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard Interactivo de Internacionalización", layout="wide")

st.title("🌎 Dashboard Interactivo para Análisis de Internacionalización")

# === 1. DATOS DE BARRERAS DE ENTRADA ===
barreras_data = pd.DataFrame({
    'País': ['Brasil', 'Argentina', 'Chile', 'Colombia', 'Ecuador'],
    'Barrera de Entrada': ['Regulaciones Comerciales', 'Impuestos Altos', 'Barreras Culturales', 'Competencia Local', 'Desafíos Logísticos'],
    'Nivel de Dificultad (1-10)': [7, 6, 5, 8, 6]
})

# === 2. DATOS DE CLIENTES ===
clientes_data = pd.DataFrame({
    'Cliente': ['Chocolate & Co', 'Cocoa Kingdom', 'Sweet Delights', 'Cocoa Trading', 'Chocolate World'],
    'País': ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Ecuador'],
    'Tamaño de la Empresa': ['Mediana', 'Grande', 'Pequeña', 'Mediana', 'Grande'],
    'Demanda Anual (Toneladas)': [150, 300, 50, 100, 250]
})

# === 3. DATOS DE EXPORTACIONES ===
exportaciones_data = pd.DataFrame({
    'País': ['Brasil', 'Argentina', 'Chile', 'Colombia', 'Ecuador'],
    'Exportaciones (USD millones)': [4000, 1500, 1200, 3000, 2500]
})

# === 4. DATOS DE SEGMENTO DE CLIENTES ===
segmento_data = pd.D_


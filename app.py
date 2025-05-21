import streamlit as st
import pandas as pd
import altair as alt

# Configuración de página
st.set_page_config(page_title="Dashboard LATAM", layout="wide")

# Estilos
st.markdown("<h1 style='text-align: center; color: #4B0082;'>🌎 Dashboard Interactivo - Comercio Internacional LATAM</h1>", unsafe_allow_html=True)
st.markdown("---")

# Datos
barriers_data = {
    "País": ["Brasil", "Argentina", "Chile", "Colombia", "Ecuador"],
    "Barrera de Entrada": [
        "Regulaciones Comerciales", "Impuestos Altos", "Barreras Culturales",
        "Competencia Local", "Desafíos Logísticos"
    ],
    "Nivel de Dificultad (1-10)": [7, 6, 5, 8, 6]
}

clients_data = {
    "Cliente": ["Chocolate & Co", "Cocoa Kingdom", "Sweet Delights", "Cocoa Trading", "Chocolate World"],
    "País": ["Argentina", "Brasil", "Chile", "Colombia", "Ecuador"],
    "Tamaño de la Empresa": ["Mediana", "Grande", "Pequeña", "Mediana", "Grande"],
    "Demanda Anual (Toneladas)": [150, 300, 50, 100, 250]
}

exports_data = {
    "País": ["Brasil"],
    "Exportaciones (USD millones)": [4000]
}

market_segment_data = {
    "País": ["Brasil", "Argentina", "Chile", "Colombia", "Ecuador"],
    "Segmento de Clientes": ["Supermercados", "Tiendas Especializadas", "Comercios Minoristas", "Distribuidores", "Mayoristas"],
    "Tamaño del Mercado (USD millones)": [5000, 1500, 1200, 3000, 2000]
}

# DataFrames
df_barriers = pd.DataFrame(barriers_data)
df_clients = pd.DataFrame(clients_data)
df_exports = pd.DataFrame(exports_data)
df_market = pd.DataFrame(market_segment_data)

# Sección 1
st.subheader("🛑 Barreras de Entrada por País")
st.dataframe(df_barriers, use_container_width=True)

barriers_chart = alt.Chart(df_barriers).mark_bar(color="#FF6F61").encode(
    x=alt.X('País', sort='-y'),
    y='Nivel de Dificultad (1-10)',
    tooltip=['País', 'Barrera de Entrada', 'Nivel de Dificultad (1-10)']
).properties(
    width=600,
    height=300
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

st.altair_chart(barriers_chart, use_container_width=True)
st.divider()

# Sección 2: Clientes y Demanda
st.subheader("📦 Clientes y Demanda Anual")
st.dataframe(df_clients, use_container_width=True)

demand_chart = alt.Chart(df_clients).mark_circle(size=200).encode(
    x=alt.X('Cliente', sort='-y'),
    y='Demanda Anual (Toneladas)',
    color=alt.Color('País', scale=alt.Scale(scheme='tableau10')),
    tooltip=['Cliente', 'País', 'Tamaño de la Empresa', 'Demanda Anual (Toneladas)']
).properties(
    width=800,
    height=300
)

st.altair_chart(demand_chart, use_container_width=True)
st.divider()

# Sección 3: Exportaciones
st.subheader("🚢 Exportaciones por País")
col1, col2 = st.columns([1, 2])

with col1:
    st.dataframe(df_exports, use_container_width=True)

with col2:
    export_chart = alt.Chart(df_exports).mark_bar(color="#4682B4").encode(
        x='País',
        y='Exportaciones (USD millones)',
        tooltip=['País', 'Exportaciones (USD millones)']
    ).properties(
        width=400,
        height=300
    )
    st.altair_chart(export_chart, use_container_width=True)

st.divider()

# Sección 4: Segmentos de Clientes y Tamaño de Mercado
st.subheader("📊 Segmentos de Clientes y Tamaño de Mercado")
st.dataframe(df_market, use_container_width=True)

market_chart = alt.Chart(df_market).mark_bar(color="#8A2BE2").encode(
    x=alt.X('País', sort='-y'),
    y='Tamaño del Mercado (USD millones)',
    tooltip=['País', 'Segmento de Clientes', 'Tamaño del Mercado (USD millones)']
).properties(
    width=700,
    height=300
)

st.altair_chart(market_chart, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 - Dashboard desarrollado para análisis de internacionalización de productos</p>", unsafe_allow_html=True)

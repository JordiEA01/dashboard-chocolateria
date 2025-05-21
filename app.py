import streamlit as st
import pandas as pd
import altair as alt

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

# Convertir a DataFrame
df_barriers = pd.DataFrame(barriers_data)
df_clients = pd.DataFrame(clients_data)
df_exports = pd.DataFrame(exports_data)
df_market = pd.DataFrame(market_segment_data)

# Título
st.title("Dashboard Interactivo - Comercio Internacional en Países de América Latina")

# Sección 1: Barreras de Entrada
st.header("Barreras de Entrada por País")
st.dataframe(df_barriers)

# Gráfico dificultad por país
barriers_chart = alt.Chart(df_barriers).mark_bar(color="coral").encode(
    x='País',
    y='Nivel de Dificultad (1-10)',
    tooltip=['País', 'Barrera de Entrada', 'Nivel de Dificultad (1-10)']
).properties(
    width=600,
    height=300,
    title="Nivel de Dificultad de Barreras de Entrada"
)
st.altair_chart(barriers_chart, use_container_width=True)

# Sección 2: Clientes y Demanda
st.header("Clientes y Demanda Anual por País")
st.dataframe(df_clients)

# Gráfico demanda anual por cliente
demand_chart = alt.Chart(df_clients).mark_circle(size=100, color='mediumseagreen').encode(
    x='Cliente',
    y='Demanda Anual (Toneladas)',
    color='País',
    tooltip=['Cliente', 'País', 'Tamaño de la Empresa', 'Demanda Anual (Toneladas)']
).properties(
    width=700,
    height=300,
    title="Demanda Anual de Clientes (Toneladas)"
)
st.altair_chart(demand_chart, use_container_width=True)

# Sección 3: Exportaciones
st.header("Exportaciones por País (USD millones)")
st.dataframe(df_exports)

# Gráfico exportaciones (solo Brasil)
export_chart = alt.Chart(df_exports).mark_bar(color="steelblue").encode(
    x='País',
    y='Exportaciones (USD millones)',
    tooltip=['País', 'Exportaciones (USD millones)']
).properties(
    width=400,
    height=300,
    title="Exportaciones (USD millones)"
)
st.altair_chart(export_chart, use_container_width=True)

# Sección 4: Segmentos de Clientes y Tamaño del Mercado
st.header("Segmentos de Clientes y Tamaño de Mercado por País")
st.dataframe(df_market)

# Gráfico tamaño de mercado
market_chart = alt.Chart(df_market).mark_bar(color="mediumpurple").encode(
    x='País',
    y='Tamaño del Mercado (USD millones)',
    tooltip=['País', 'Segmento de Clientes', 'Tamaño del Mercado (USD millones)']
).properties(
    width=600,
    height=300,
    title="Tamaño del Mercado por Segmento de Clientes"
)
st.altair_chart(market_chart, use_container_width=True)


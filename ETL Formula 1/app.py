import configparser
import streamlit as st
from libreria.airtable import AirtableConnector
from libreria.graficos import (
    diez_mejores_pilotos,
    comparativa_todos_pilotos,
    puntaje_piloto,
    puntaje_escuderia,
    distribucion_puntaje_piloto,
    distribucion_puntaje_escuderia,
    mapa,
    graficar_viento,
    graficas_temperatura,
    columna_lluvia,
)

# Initialize configurations
config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('airtable', 'TOKEN')
BASE_ID = config.get('airtable', 'BASE_ID')

# Connect to Airtable
connector = AirtableConnector(TOKEN, BASE_ID)
carreras = connector.to_df('carreras')
weather = connector.to_df('weather')
carreras_detalles = connector.to_df('carreras_detalles')

# Streamlit Sidebar
st.sidebar.title("Formula 1 Dashboard")
option = st.sidebar.radio(
    "Select Visualization:",
    [
        "Top 10 Drivers",
        "All Drivers Comparison",
        "Driver Points",
        "Team Points",
        "Points Distribution (Drivers)",
        "Points Distribution (Teams)",
        "Race Map",
        "Wind Visualization",
        "Temperature Trends",
        "Rainfall Patterns",
    ]
)

# Main Visualization Logic
st.title("Interactive Formula 1 Visualizations")

if option == "Top 10 Drivers":
    st.header("Top 10 Drivers by Performance")
    fig = diez_mejores_pilotos(carreras)
    st.plotly_chart(fig)

elif option == "All Drivers Comparison":
    st.header("Comparison of All Drivers")
    fig = comparativa_todos_pilotos(carreras)
    st.plotly_chart(fig)

elif option == "Driver Points":
    st.header("Driver Points Overview")
    fig = puntaje_piloto(carreras_detalles)
    st.plotly_chart(fig)

elif option == "Team Points":
    st.header("Team Points Overview")
    fig = puntaje_escuderia(carreras_detalles)
    st.plotly_chart(fig)

elif option == "Points Distribution (Drivers)":
    st.header("Points Distribution Among Drivers")
    fig = distribucion_puntaje_piloto(carreras_detalles)
    st.plotly_chart(fig)

elif option == "Points Distribution (Teams)":
    st.header("Points Distribution Among Teams")
    fig = distribucion_puntaje_escuderia(carreras_detalles)
    st.plotly_chart(fig)

elif option == "Race Map":
    st.header("Race Map")
    fig = mapa(weather)
    st.plotly_chart(fig)

elif option == "Wind Visualization":
    st.header("Wind Patterns")
    fig = graficar_viento(weather)
    st.plotly_chart(fig)

elif option == "Temperature Trends":
    st.header("Temperature Trends Across Races")
    fig = graficas_temperatura(weather)
    st.plotly_chart(fig)

elif option == "Rainfall Patterns":
    st.header("Rainfall Patterns")
    fig = columna_lluvia(weather)
    st.plotly_chart(fig)
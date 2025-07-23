import folium
import pandas as pd
import requests
import streamlit as st
from streamlit.components.v1 import html


def generate_financial_loss_map(df):
    # 1. Charger les données GeoJSON des pays
    url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
    geo_data = requests.get(url).json()

    # 2. Nettoyage des données
    rename_dict = {"USA": "United States of America", "UK": "United Kingdom"}
    df["Country"] = df["Country"].replace(rename_dict)

    # 3. Agrégation des pertes financières
    df_country_loss = df.groupby("Country", as_index=False)[
        "Financial Loss (in Million $)"
    ].sum()
    df_country_loss["Country"] = df_country_loss["Country"].astype(str)

    # 4. Création de la carte Folium
    m = folium.Map(location=[20, 0], zoom_start=2)

    # 5. Ajout de la couche choroplèthe
    folium.Choropleth(
        geo_data=geo_data,
        name="choropleth",
        data=df_country_loss,
        columns=["Country", "Financial Loss (in Million $)"],
        key_on="feature.properties.name",
        fill_color="YlOrRd",
        nan_fill_color="gray",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Financial Loss (in Million $)",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    # 6. Exporter la carte HTML et afficher dans Streamlit
    map_html = m._repr_html_()
    html(map_html, height=600, width=1500)

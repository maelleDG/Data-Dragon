import pandas as pd
import folium
from folium import IFrame
import matplotlib.pyplot as plt
import io
import base64
import geopandas as gpd
import requests
from streamlit.components.v1 import html


def generate_attack_type_map(df):
    # Charger GeoJSON
    url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json"
    geo_data = requests.get(url).json()
    gdf = gpd.GeoDataFrame.from_features(geo_data["features"])

    # Calculer les centroïdes
    gdf["centroid"] = gdf.geometry.centroid

    # Initialiser la carte
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Fonction pour camembert
    def create_pie_chart(data):
        plt.figure(figsize=(6, 6))
        data.plot.pie(
            y="Number of Affected Users",
            labels=data["Attack Type"],
            autopct="%1.1f%%",
            legend=False,
        )
        plt.ylabel("")
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close()
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")

    # Fonction pour bar chart
    def create_bar_chart(data):
        plt.figure(figsize=(6, 4))
        plt.bar(
            data["Attack Type"],
            data["Incident Resolution Time (in Hours)"],
            color="skyblue",
        )
        plt.ylabel("Avg Resolution Time (hrs)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        plt.close()
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")

    # Générer les popups par pays
    for idx, row in gdf.iterrows():
        country_name = row["name"]
        centroid = row["centroid"]
        df_country = df[df["Country"] == country_name]

        if df_country.empty:
            continue

        count = df_country["Number of Affected Users"].sum()
        pie_data = df_country.groupby("Attack Type", as_index=False)[
            "Number of Affected Users"
        ].sum()
        bar_data = df_country.groupby("Attack Type", as_index=False)[
            "Incident Resolution Time (in Hours)"
        ].mean()

        pie_base64 = create_pie_chart(pie_data)
        bar_base64 = create_bar_chart(bar_data)

        html_content = f"""
        <h4>{country_name}</h4>
        <p><b>Affected Users</b> (Pie Chart)</p>
        <img src="data:image/png;base64,{pie_base64}"><br>
        <p><b>Avg Incident Resolution Time</b> (Bar Chart)</p>
        <img src="data:image/png;base64,{bar_base64}"><br>
        <p><b>Total Users Affected:</b> {count}</p>
        """

        iframe = IFrame(html_content, width=650, height=850)
        popup = folium.Popup(iframe, max_width=650)

        folium.Marker(
            location=[centroid.y, centroid.x], popup=popup, tooltip=country_name
        ).add_to(m)

    # Affichage Streamlit
    html(m._repr_html_(), height=850, width=1000)

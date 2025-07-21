import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import theme  # Importe votre fichier de thème
import seaborn as sns
from matplotlib.ticker import PercentFormatter
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
from plotly.subplots import make_subplots


def display_incidents_fr():

    with st.expander("Cliquez pour voir l'évolution des incidents en France"):

        @st.cache_data(ttl=300)
        def load_ransomware_data():
            url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS4AQdSMA6le89nABL7ztSUACk_tPI7IWjE57IwCQtNnavtrO41M2cxlY-xEwr9tavysWSWiqGZJERx/pub?gid=1450603232&single=true&output=csv"
            df1 = pd.read_csv(url)

            # Nettoyage et préparation des données
            df1["Années"] = df1["Années"].astype(int)
            df1["Nombres signalements"] = pd.to_numeric(
                df1["Nombres signalements"], errors="coerce"
            )
            nombres_signalements_interp = df1["Nombres signalements"].interpolate(
                method="linear"
            )

            df1["Texte Signalements"] = df1.apply(
                lambda row: (
                    f"{int(row['Nombres signalements'])}"
                    if pd.notna(row["Nombres signalements"])
                    else f"{int(nombres_signalements_interp[row.name])}*"
                ),
                axis=1,
            )
            df1["Nombres signalements interpolé"] = nombres_signalements_interp

            return df1

        try:
            df1 = load_ransomware_data()

            # Graphique 1
            fig1_px = px.line(
                df1,
                x="Années",
                y="Nombres incidents",
                title="Évolution du Nombre d'Incidents de Sécurité",
                markers=True,
                line_shape="linear",
                color_discrete_sequence=["royalblue"],
                text="Nombres incidents",
            )
            fig1_px.update_traces(mode="lines+markers+text", textposition="top center")
            fig1_px.update_layout(
                xaxis_title="Année",
                yaxis_title="Nombre d'Incidents",
                xaxis_tickmode="array",
                xaxis_tickvals=df1["Années"].unique().tolist(),
                hovermode="x unified",
            )

            # Graphique 2
            fig2_px = px.line(
                df1,
                x="Années",
                y="Nombres signalements interpolé",
                title="Évolution du Nombre de Signalements",
                markers=True,
                line_shape="linear",
                color_discrete_sequence=["coral"],
                text="Texte Signalements",
            )
            fig2_px.update_traces(mode="lines+markers+text", textposition="top center")
            fig2_px.update_layout(
                xaxis_title="Année",
                yaxis_title="Nombre de Signalements",
                xaxis_tickmode="array",
                xaxis_tickvals=df1["Années"].unique().tolist(),
                hovermode="x unified",
            )

            # Combinaison des graphes
            fig = make_subplots(
                rows=1,
                cols=2,
                subplot_titles=(
                    "Évolution du Nombre d'Incidents de Sécurité",
                    "Évolution du Nombre de Signalements",
                ),
                shared_xaxes=True,
            )

            for trace in fig1_px.data:
                fig.add_trace(trace, row=1, col=1)
            for trace in fig2_px.data:
                fig.add_trace(trace, row=1, col=2)

            fig.update_layout(
                title_text="Comparaison de l'Évolution des Incidents et des Signalements en France (2020-2024)",
                title_font_size=18,
                height=550,
                showlegend=True,
                xaxis=dict(
                    title="Année",
                    tickmode="array",
                    tickvals=df1["Années"].unique().tolist(),
                ),
                xaxis2=dict(
                    title="Année",
                    tickmode="array",
                    tickvals=df1["Années"].unique().tolist(),
                ),
                yaxis=dict(title="Nombre d'Incidents"),
                yaxis2=dict(title="Nombre de Signalements"),
                hovermode="x unified",
            )

            st.plotly_chart(fig, use_container_width=True)

        except FileNotFoundError:
            st.error("Le fichier source n'a pas été trouvé. Veuillez vérifier le chemin.")
        except Exception as e:
            st.error(
                f"Une erreur est survenue lors du chargement ou de l'affichage des données : {e}"
            )

        if st.button("Recharger les données maintenant", key="reload2"):
            load_ransomware_data.clear()
            st.rerun()

        st.markdown(
            """
        #### Augmentation Générale des Incidents de Sécurité (Nombres incidents) :

    On observe une tendance globale à la hausse du nombre d'incidents signalés. Partant de 759 en 2020, ce chiffre atteint 1361 en 2024.
    Bien qu'il y ait eu un léger recul en 2022 par rapport à 2021, la croissance est repartie de manière significative en 2023 et 2024, suggérant une intensification du paysage des menaces.

    #### Capacités de Traitement des Vulnérabilités en Hausse (Nombre de dossiers CVE traités par la CERT-FR) :

    Le nombre de dossiers CVE traités par la CERT-FR a connu une augmentation constante et rapide, passant de seulement 7 en 2020 à 40 en 2024.
    Cela peut indiquer une augmentation du nombre de vulnérabilités découvertes et/ou une capacité accrue de la CERT-FR à les identifier, les analyser et y répondre, démontrant une réactivité et un engagement croissants de l'agence nationale.

    #### Évolution des Signalements (Nombres signalements) :

    Après une légère fluctuation entre 2020 et 2022, on constate un bond très important du nombre de signalements en 2024 (3004), après une donnée manquante pour 2023.
    La donnée manquante pour 2023 est une lacune notable. L'explosion en 2024 pourrait signifier une sensibilisation accrue des organisations et du public à signaler les incidents, ou une amélioration des plateformes et processus de signalement.

    #### Nouvelles Métriques et Élargissement de la Surveillance :

    Les colonnes Nombre événements de sécurité et Attaques par rançongiciel n'apparaissent qu'à partir de 2023 et 2024 respectivement (avec des valeurs NaN avant).
    Cela suggère un élargissement du périmètre de surveillance et de collecte de données pour inclure des catégories plus spécifiques d'événements ou d'attaques.
    Pour Nombre événements de sécurité, le chiffre passe de 3703 en 2023 à 4386 en 2024, indiquant une augmentation de ces événements plus "génériques" une fois qu'ils sont suivis.
    Pour les Attaques par rançongiciel, 144 attaques ont été enregistrées en 2024. C'est une donnée de référence importante pour le futur, mais l'absence d'historique ne permet pas de dégager une tendance pour l'instant. Cela souligne l'importance croissante de cette menace spécifique, justifiant son suivi dédié.

    #### Résumé 

    Le tableau dépeint un paysage de la cybersécurité en France qui est de plus en plus dynamique et complexe.

    La menace cyber est clairement en augmentation, comme en témoigne la hausse constante du nombre d'incidents.
    Simultanément, les capacités de détection, de traitement et de signalement s'améliorent et s'étendent, ce qui est positif dans la lutte contre la cybercriminalité.
    L'introduction de nouvelles métriques au fil du temps montre une maturité croissante dans la compréhension et le suivi des différentes facettes de la cybermenace par les autorités compétentes.
    """
        )
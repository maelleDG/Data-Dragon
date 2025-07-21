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


def display_menaces():

    with st.expander("Cliquez pour voir les principales menaces en France"):
        st.markdown(
            """
            ### Le paysage des menaces cybernétiques est de plus en plus complexe et diversifié, impactant un large éventail d'acteurs. 
            Voici les principales formes de cyberattaques observées récemment :
            """
        )
        st.markdown(
            """
                - Rançongiciels (Ransomware) : L'activité des rançongiciels reste à un niveau élevé. En 2023, le nombre d'attaques par rançongiciel portées à la connaissance de l'ANSSI a augmenté de 30% par rapport à 2022. Les TPE/PME/ETI, collectivités territoriales et établissements de santé sont particulièrement ciblés.

                - Espionnage stratégique et industriel : L'espionnage informatique demeure la menace qui mobilise le plus les équipes de l'ANSSI. Il cible notamment les équipements et infrastructures de télécommunications, ainsi que des intérêts stratégiques étatiques.

                - Attaques à finalité lucrative : Au-delà des rançongiciels, les escroqueries "classiques", tentatives d'extorsion et vols de données sont fréquents.

                - Déstabilisation / Hacktivisme : Une hausse des attaques à finalité de déstabilisation a été observée en 2024, notamment de la part de groupes hacktivistes, avec des tentatives de sabotage et des attaques par déni de service (DDoS) d'intensité accrue.

                - Phishing : Le phishing reste une méthode d'attaque très répandue, touchant près de la moitié des télétravailleurs.

                - Exploitation de vulnérabilités : L'exploitation de vulnérabilités "jour-zéro" et "jour-un" (nouvellement découvertes) est une porte d'entrée majeure pour les attaquants. Les erreurs de configuration et les vulnérabilités résiduelles sont également des facteurs de risque importants.

                - Fuites de données : En 2023, 4 668 fuites de données ont été notifiées aux autorités compétentes en France, soit une augmentation de 16% par rapport à 2022.
                    """
        )

        # Fonction de chargement des données avec cache (TTL 5 minutes)
        @st.cache_data(ttl=300)
        def load_ransomware_data():
            url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTUXOauBmCDBKJQQR2QnTSLOsdXxWtBhwI-3bqcTDsuiVlADJVqZZEMBnUtjY3tPJW35eY3JL_elFFm/pub?gid=1588107422&single=true&output=csv"
            df = pd.read_csv(url)
            return df

        def plot_ransomware_data(df):
            # Préparation des données
            df_indexed = df.set_index("Types / Année")
            df_indexed["2023"] = df_indexed["2023"].str.replace("%", "").astype(float)
            df_indexed["2024"] = df_indexed["2024"].str.replace("%", "").astype(float)

            fig, ax = plt.subplots(figsize=(10, 6))
            df_indexed.plot.bar(ax=ax, width=0.8)

            fig.patch.set_facecolor("black")
            ax.set_facecolor("black")

            ax.set_title(
                "Répartition des victimes de rançongiciel en France (2023 vs 2024)",
                fontsize=16,
                color="white",
            )
            ax.set_xlabel("Types d'organisations", fontsize=10, color="white")
            ax.set_ylabel("Pourcentage de victimes (%)", fontsize=10, color="white")
            ax.legend(title="Année", fontsize=10, labelcolor="white")
            plt.xticks(rotation=45, ha="right", color="white")
            ax.tick_params(axis="x", labelsize=8, color="white")
            plt.grid(axis="y", linestyle="--", alpha=0.7, color="gray")

            for container in ax.containers:
                ax.bar_label(
                    container, fmt="%.0f%%", label_type="edge", fontsize=9, color="white"
                )

            plt.tight_layout()
            return fig

        # Affichage des données
        df = load_ransomware_data()

        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.markdown(
                "<h3 style='text-align: center;'>Analyse des menaces de rançongiciel en France</h3>",
                unsafe_allow_html=True,
            )
            st.pyplot(plot_ransomware_data(df))

        st.write(
            """
            Cette application présente la répartition des victimes de rançongiciel en France pour les années 2023 et 2024.
            Les données montrent les différents types d'organisations affectées et le pourcentage qu'elles représentent.
            """
        )

        # Bouton pour forcer la recharge
        if st.button("Recharger les données maintenant", key="reload1"):
            load_ransomware_data.clear()
            st.rerun()
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


def display_marche_fr():
    
    with st.expander("Cliquez pour voir le marché global de la cybersécurité en France"):
        # Le code de scraping
        url = "https://www.mordorintelligence.com/fr/industry-reports/france-cybersecurity-market"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        soup_chiffre = soup.find(
            "div", {"class": "overview-points-list flex-49 share-feature-end"}
        )
        data = {}
        if soup_chiffre:
            rows = soup_chiffre.find_all("tr")
            for row in rows:
                cells = row.find_all("td")
                if len(cells) == 2:
                    key = cells[0].get_text(strip=True)
                    value = cells[1].get_text(strip=True)
                    data[key] = value

        market_size_2024_str = data.get("Taille du Marché (2024)", "0 USD")
        market_size_2029_str = data.get("Taille du Marché (2029)", "0 USD")
        cagr_2024_2029_str = data.get("CAGR (2024 - 2029)", "0%")

        try:
            market_size_2024 = float(
                market_size_2024_str.replace("USD", "").replace("Billion", "").strip()
            )
        except ValueError:
            market_size_2024 = 0.0

        try:
            market_size_2029 = float(
                market_size_2029_str.replace("USD", "").replace("Billion", "").strip()
            )
        except ValueError:
            market_size_2029 = 0.0 

        try:
            cagr_2024_2029 = float(cagr_2024_2029_str.replace("%", "").strip())
        except ValueError:
            cagr_2024_2029 = 0.0 

        st.markdown(
            """Le marché global de la cybersécurité en France est estimé à 9,10 milliards de dollars en 2024
            et devrait atteindre 15,54 milliards de dollars en 2029, avec un taux de croissance annuel composé (CAGR) de 11,29%.
            La CTI, bien que n'ayant pas de chiffres spécifiques distincts de ce marché global, en est une composante essentielle et en forte demande."""
        )

        # --- Début du code pour les vignettes rondes ---
        
        st.subheader("Informations Clés")

        st.markdown(
            """
        <style>
        .round-metric-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 20px; /* Espace entre les bulles */
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .round-metric {
            width: 280px; /* Diamètre de la bulle */
            height: 280px;
            border-radius: 50%; /* Rend la forme circulaire */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            font-family: sans-serif;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2); /* Légère ombre */
            transition: transform 0.2s ease-in-out; /* Effet de transition au survol */
        }
        .round-metric:hover {
            transform: translateY(-5px); /* Effet de survol */
        }
        .round-metric-label {
            font-size: 1.2em;
            font-weight: normal;
            margin-bottom: 5px;
            line-height: 1.2;
        }
        .round-metric-value {
            font-size: 2.5em;
            font-weight: bold;
        }
        /* Couleurs pour chaque bulle */
        .color-blue { background-color: #2196F3; } /* Bleu */
        .color-orange { background-color: #FF9800; } /* Orange */
        .color-purple { background-color: #9C27B0; } /* Violet */
        </style>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
        <div class="round-metric-container">
            <div class="round-metric color-blue">
                <div class="round-metric-label">Taille du Marché<br>(2024)</div>
                <div class="round-metric-value">{market_size_2024_str}</div>
            </div>
            <div class="round-metric color-orange">
                <div class="round-metric-label">Taille du Marché<br>(2029)</div>
                <div class="round-metric-value">{market_size_2029_str}</div>
            </div>
            <div class="round-metric color-purple">
                <div class="round-metric-label">CAGR<br>(2024-2029)</div>
                <div class="round-metric-value">{cagr_2024_2029_str}</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # --- Fin du code pour les vignettes rondes ---

        # GRAPHIQUE Répartition des budgets IT
        # Barre violette en haut
        st.markdown(
            """
        <div style="background-color:#6a0dad; padding: 2px; border-radius: 8px; margin-bottom: 20px;"></div>
        """,
            unsafe_allow_html=True,
        )

        # Titre centré
        st.markdown(
            """
        <h2 style='text-align: center;'>💻 Répartition des budgets IT alloués à la cybersécurité</h2>
        """,
            unsafe_allow_html=True,
        )

        # Mise en page en colonnes
        col1, col2 = st.columns([2, 1])

        # Données
        data_budgets = {
            "Secteur": ["Finance", "Industrie", "Santé", "Commerce", "Services publics"],
            "Budget IT (%)": [8, 5, 6, 4.5, 6],
        }

        df_budgets = pd.DataFrame(data_budgets)

        # Création du graphique
        fig, ax = plt.subplots(figsize=(8, 4))

        # Fond noir
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")

        # Graphique
        sns.barplot(
            data=df_budgets,
            x="Secteur",
            y="Budget IT (%)",
            hue="Secteur",
            palette="pastel",
            ax=ax,
        )

        # Titre en blanc
        ax.set_title(
            "Part du budget IT dédiée à la cybersécurité par secteur",
            fontsize=16,
            pad=20,
            color="white",
        )

        # Axe Y en blanc
        ax.set_ylabel("Pourcentage du budget IT", color="white")
        ax.set_xlabel("")

        # Ticks en blanc
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")

        # Bordures et graduations en blanc
        for spine in ax.spines.values():
            spine.set_color("white")

        ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
        plt.xticks(rotation=30, ha="right")

        # Afficher le graphique dans une colonne étroite
        col1, col2, col3 = st.columns([1, 2, 1])  # Colonne centrale plus large

        with col2:  # Affichage dans la colonne centrale
            st.pyplot(fig)

        # Informations
        st.markdown(
            """
        ### 💡 Informations clés :
        - Le secteur **Finance** est le plus investi en cybersécurité.
        - Les **Services publics** et la **Santé** maintiennent un budget stable.
        - Le secteur **Commerce** reste en retrait.
        """
        )

        st.markdown("#### 🔎 Analyse rapide :")
        st.info(
            "👉 Les secteurs à forte exposition aux risques financiers allouent logiquement une part plus importante de leur budget IT à la cybersécurité."
        )
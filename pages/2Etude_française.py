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

# Applique les configurations de page et le thème
theme.set_page_defaults()  # Optionnel si main.py gère déjà la config globale, mais bonne pratique
theme.apply_theme()


# Image de couverture
st.image(
    "logo_bandeau.png",
    use_container_width=True,
)

st.markdown(
    """
    <h1 style='text-align: center;'>Contexte du marché et menace en France</h1>
    """,
    unsafe_allow_html=True,
)

# Contenu spécifique à la page des services
st.markdown(
    """
<div class="big-text">
Comprenez le contexte actuel du marché français de la cybersécurité et découvrez en détail comment Cyber Dragon peut transformer votre approche de la sécurité et de l'analyse face à ces menaces grandissantes.
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("""---""")

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

    # Nettoyage et conversion des données
    # On retire "USD", "Billion", "Billion" et "%" et on convertit en float
    try:
        market_size_2024 = float(
            market_size_2024_str.replace("USD", "").replace("Billion", "").strip()
        )
    except ValueError:
        market_size_2024 = 0.0  # Gérer les cas où la conversion échoue

    try:
        market_size_2029 = float(
            market_size_2029_str.replace("USD", "").replace("Billion", "").strip()
        )
    except ValueError:
        market_size_2029 = 0.0  # Gérer les cas où la conversion échoue

    try:
        cagr_2024_2029 = float(cagr_2024_2029_str.replace("%", "").strip())
    except ValueError:
        cagr_2024_2029 = 0.0  # Gérer les cas où la conversion échoue

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


##########################################################################################################

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

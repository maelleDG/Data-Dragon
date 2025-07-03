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

    def plot_ransomware_data():
        # Chargement des données
        df = pd.read_csv(
            "Principales menaces en France - Répartition des victimes rançongiciel.csv"
        )

        # Préparation des données pour le graphique
        # Définir la colonne 'Types / Année' comme index
        df_indexed = df.set_index("Types / Année")

        # Convertir les colonnes d'années en numérique (en supprimant le '%')
        df_indexed["2023"] = df_indexed["2023"].str.replace("%", "").astype(float)
        df_indexed["2024"] = df_indexed["2024"].str.replace("%", "").astype(float)

        # Création du graphique à barres
        fig, ax = plt.subplots(
            figsize=(10, 6)
        )  # Ajuster la taille du graphique si nécessaire
        df_indexed.plot.bar(ax=ax, width=0.8)  # 'width' ajuste l'épaisseur des barres

        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")

        # Personnalisation du graphique
        ax.set_title(
            "Répartition des victimes de rançongiciel en France (2023 vs 2024)",
            fontsize=16,
            color="white",
        )
        ax.set_xlabel("Types d'organisations", fontsize=10, color="white")
        ax.set_ylabel("Pourcentage de victimes (%)", fontsize=10, color="white")
        ax.legend(title="Année", fontsize=10, labelcolor="white")  # Titre de la légende
        plt.xticks(
            rotation=45, ha="right", color="white"
        )  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
        ax.tick_params(axis="x", labelsize=8, color="white")
        plt.grid(
            axis="y", linestyle="--", alpha=0.7, color="gray"
        )  # Ajout d'une grille légère sur l'axe y

        # Afficher les valeurs sur les barres
        for container in ax.containers:
            ax.bar_label(
                container, fmt="%.0f%%", label_type="edge", fontsize=9, color="white"
            )  # Affiche les pourcentages

        plt.tight_layout()  # Ajuste les marges pour que tout rentre
        return fig  # Retourne l'objet figure Matplotlib

    col1, col2, col3 = st.columns([1, 4, 1])
    # Afficher le graphique
    with col2:
        # Titre de l'application Streamlit
        st.markdown(
            "<h3 style='text-align: center;'>Analyse des menaces de rançongiciel en France</h3>",
            unsafe_allow_html=True,
        )
        st.pyplot(plot_ransomware_data())

    # Vous pouvez ajouter plus d'éléments à votre application Streamlit ici, par exemple:
    st.write(
        """
    Cette application présente la répartition des victimes de rançongiciel en France pour les années 2023 et 2024.
    Les données montrent les différents types d'organisations affectées et le pourcentage qu'elles représentent.
    """
    )

with st.expander("Cliquez pour voir l'évolution des incidents en France"):
    try:
        df1 = pd.read_csv("Principales menaces en France - Evolution des incidents.csv")

        # S'assurer que la colonne 'Années' est de type numérique
        df1["Années"] = df1["Années"].astype(int)

        # Convertir 'Nombres signalements' en numérique, en forçant les erreurs à NaN
        df1["Nombres signalements"] = pd.to_numeric(
            df1["Nombres signalements"], errors="coerce"
        )

        # Créer une copie de la colonne pour l'interpolation afin de ne pas modifier les données originales
        nombres_signalements_interp = df1["Nombres signalements"].interpolate(
            method="linear"
        )

        # Préparer les étiquettes de texte pour le graphique des signalements
        df1["Texte Signalements"] = df1.apply(
            lambda row: (
                f"{int(row['Nombres signalements'])}"
                if pd.notna(row["Nombres signalements"])
                else f"{int(nombres_signalements_interp[row.name])}*"
            ),  # row.name est l'index de la ligne
            axis=1,
        )
        # Assurez-vous d'utiliser la série interpolée pour la colonne du graphique
        df1["Nombres signalements interpolé"] = nombres_signalements_interp

        # 1. Créer le premier graphique (Nombres incidents) avec Plotly Express
        fig1_px = px.line(
            df1,
            x="Années",
            y="Nombres incidents",
            title="Évolution du Nombre d'Incidents de Sécurité",
            markers=True,
            line_shape="linear",  # 'linear' ou 'spline' pour des courbes lisses
            color_discrete_sequence=["royalblue"],
            text="Nombres incidents",  # Affiche les valeurs sur les points
        )
        fig1_px.update_traces(
            mode="lines+markers+text",
            textposition="top center",  # Position du texte au-dessus des points
        )
        fig1_px.update_layout(
            xaxis_title="Année",
            yaxis_title="Nombre d'Incidents",
            xaxis_tickmode="array",
            xaxis_tickvals=df1["Années"].unique().tolist(),
            hovermode="x unified",  # Améliore l'interactivité au survol
        )

        # 2. Créer le deuxième graphique (Nombres signalements) avec Plotly Express
        fig2_px = px.line(
            df1,
            x="Années",
            y="Nombres signalements interpolé",  # Utilisez la colonne interpolée
            title="Évolution du Nombre de Signalements",
            markers=True,
            line_shape="linear",
            color_discrete_sequence=["coral"],
            text="Texte Signalements",  # Utilisez la colonne de texte personnalisée
        )
        fig2_px.update_traces(mode="lines+markers+text", textposition="top center")
        fig2_px.update_layout(
            xaxis_title="Année",
            yaxis_title="Nombre de Signalements",
            xaxis_tickmode="array",
            xaxis_tickvals=df1["Années"].unique().tolist(),
            hovermode="x unified",
        )

        # 3. Combiner les deux graphiques en sous-graphiques avec make_subplots
        fig = make_subplots(
            rows=1,
            cols=2,
            subplot_titles=(
                "Évolution du Nombre d'Incidents de Sécurité",
                "Évolution du Nombre de Signalements",
            ),
            shared_xaxes=True,  # Partage l'axe des X
        )

        # Ajouter les traces du premier graphique au premier sous-graphique
        for trace in fig1_px.data:
            fig.add_trace(trace, row=1, col=1)

        # Ajouter les traces du deuxième graphique au deuxième sous-graphique
        for trace in fig2_px.data:
            fig.add_trace(trace, row=1, col=2)

        # Mettre à jour la mise en page des sous-graphiques
        fig.update_layout(
            title_text="Comparaison de l'Évolution des Incidents et des Signalements en France (2020-2024)",
            title_font_size=18,
            height=550,  # Ajustez la hauteur de la figure globale
            showlegend=True,  # Affiche les légendes pour chaque trace
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

        # Afficher la figure dans Streamlit
        st.plotly_chart(fig, use_container_width=True)

    except FileNotFoundError:
        st.error(
            "Le fichier 'Principales menaces en France - Evolution des incidents.csv' n'a pas été trouvé. Veuillez vérifier le chemin."
        )
    except Exception as e:
        st.error(
            f"Une erreur est survenue lors du chargement ou de l'affichage des données : {e}"
        )
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

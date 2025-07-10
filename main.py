import streamlit as st
import theme  # Importe votre fichier de thème

# Applique les configurations de page et le thème
theme.set_page_defaults()
theme.apply_theme()

# --- Définir la navigation ---
pages = {
    "Accueil": [
        st.Page("pages/main_page.py", title="Accueil"),
    ],
    "Renseignement sur les menaces": [  # Equivalent de "CyberThreatIntelligence"
        st.Page("pages/1CyberThreatIntelligence.py", title="Cyber Threat Intelligence"),
    ],
    "Analyse du marché": [  # Equivalent de "Étude française"
        st.Page("pages/2Etude_française.py", title="Étude française"),
    ],
    "Solutions & partenaires": [
        st.Page("pages/5Partenaires.py", title="Solutions & Partenaires"),
    ],
    "Chatbot": [
        st.Page(
            "pages/cyberveille.py",
            title="Veille Technologique & Chatbot Météo Cybercriminalité",
        ),
        st.Page(
            "pages/3Chatbot.py", title="Assistant IA"
        ),  # Renommé pour plus de clarté
    ],
    "Sources": [
        st.Page("pages/4Sources.py", title="Nos sources"),
    ],
}

# Créer la navigation en position "top"
pg = st.navigation(pages, position="top")

# Exécuter l'application de navigation
pg.run()

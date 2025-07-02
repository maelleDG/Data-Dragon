import streamlit as st

# --- Couleurs de la Charte Graphique (Hex) ---
COLORS = {
    "BLUE_CYBER_LIGHT": "#66CCFF",
    "BLUE_CYBER_MID": "#0099FF",
    "BLUE_CYBER_DARK": "#0066CC",
    "VIOLET_NIGHT": "#1A0F3D",
    "WHITE": "#FFFFFF",
    "GREY_SLOGAN": "#CCCCCC",
}


def apply_theme():
    """Applique les styles CSS personnalisés à l'application Streamlit."""
    st.markdown(
        f"""
    <style>
        .reportview-container {{
            background: linear-gradient(to bottom, {COLORS["VIOLET_NIGHT"]}, #000000);
        }}
        .stApp {{
            background-color: {COLORS["VIOLET_NIGHT"]};
            color: {COLORS["WHITE"]};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {COLORS["WHITE"]};
            font-family: 'Montserrat', sans-serif; /* Assurez-vous d'importer les polices si nécessaire */
            font-weight: bold;
        }}
        .css-1aumxtk {{ /* Texte par défaut de Streamlit */
            color: {COLORS["WHITE"]};
            font-family: 'Open Sans', sans-serif;
        }}
        .slogan {{
            color: {COLORS["GREY_SLOGAN"]};
            font-family: 'Montserrat', sans-serif;
            font-weight: normal;
            font-size: 1.2em;
            text-align: center;
            margin-top: -15px;
            margin-bottom: 30px;
        }}
        .block-container {{
            padding-top: 2rem;
        }}
        .big-text {{
            font-size: 1.2em;
            line-height: 1.6;
            color: {COLORS["WHITE"]};
        }}
        .section-title {{
            color: {COLORS["BLUE_CYBER_LIGHT"]};
            font-size: 1.8em;
            font-weight: bold;
            margin-top: 40px;
            margin-bottom: 20px;
        }}
        .icon-text {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
            color: {COLORS["WHITE"]};
        }}
        .icon-text svg {{
            margin-right: 10px;
            fill: {COLORS["BLUE_CYBER_MID"]};
        }}
        .stButton>button {{
            background-color: {COLORS["BLUE_CYBER_MID"]};
            color: {COLORS["WHITE"]};
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 1.1em;
            font-weight: bold;
            transition: background-color 0.3s;
        }}
        .stButton>button:hover {{
            background-color: {COLORS["BLUE_CYBER_DARK"]};
            color: {COLORS["WHITE"]};
        }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def set_page_defaults():
    """Définit les configurations de page par défaut."""
    st.set_page_config(
        page_title="Cyber Dragon - Data & Cybersecurity Agency",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded",
    )


# Vous pouvez aussi ajouter d'autres fonctions utilitaires ici, par exemple pour charger le logo
from PIL import Image


def display_logo(path="logo.png"):
    try:
        logo = Image.open(path)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(logo, use_container_width=True)
    except FileNotFoundError:
        st.error(
            f"Le fichier '{path}' n'a pas été trouvé. Assurez-vous qu'il est dans le bon répertoire."
        )
        st.markdown(
            f"<h1 style='text-align: center; color: {COLORS['WHITE']};'>CYBER DRAGON</h1>",
            unsafe_allow_html=True,
        )

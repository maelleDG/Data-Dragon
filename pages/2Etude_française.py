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

from packages.marche_fr import display_marche_fr
from packages.menaces import display_menaces
from packages.incidents_fr import display_incidents_fr


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

##########################################################################################################

display_marche_fr()

##########################################################################################################

display_menaces()

##########################################################################################################

display_incidents_fr()

##########################################################################################################

st.markdown(
    f"<p style='text-align: center; color: {theme.COLORS['GREY_SLOGAN']}; font-size: 0.9em;'>© 2025 Cyber Dragon. Tous droits réservés.</p>",
    unsafe_allow_html=True,
)
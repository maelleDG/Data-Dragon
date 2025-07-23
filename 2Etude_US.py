import os, sys, json, requests
import pandas as pd
import streamlit as st

# Visualisation
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import geopandas, folium

# Modules internes
from vulnérabilités import display_chart
from perte_financière import generate_financial_loss_map
from number_attacks import display_attacks_chart
from global_map import generate_attack_type_map
import theme

# ================= CONFIGURATION & THÈME ================= #
theme.set_page_defaults()
theme.apply_theme()

# ================= CHARGEMENT DES DONNÉES ================= #
df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

# ================= CSS POUR STYLISATION ================= #
st.markdown(
    """
<style>
.big-text {
    font-size: 18px;
    font-weight: 500;
    text-align: justify;
    line-height: 1.6;
}
.tag {
    display: inline-block;
    background-color: #1e3a8a;
    color: white;
    padding: 4px 10px;
    font-size: 14px;
    border-radius: 12px;
    margin: 6px 0;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============= EN-TÊTE & CONTEXTE US ============= #
st.markdown(
    "<h1 style='text-align: center;'>Marché & Menaces de la Cybercriminalité aux États‑Unis</h1>",
    unsafe_allow_html=True,
)

# ================= SECTION MARCHÉ ================= #
st.markdown(
    """
<div class="big-text">
    <h2>2. Marché de la cybersécurité</h2>
    <span class="tag">+85 milliards USD en 2024</span>
    <ul>
        <li><strong>Croissance annuelle :</strong> 10–12 %</li>
        <li><strong>Secteurs clés :</strong> Finance, santé, industrie, énergie, gouvernement</li>
        <li><strong>Acteurs :</strong> Palo Alto Networks, CrowdStrike, Fortinet, Cisco, IBM Security</li>
        <li><strong>Technos dominantes :</strong> XDR, IA, Zero Trust, cryptographie post-quantique</li>
    </ul>
    Les États-Unis représentent le plus grand marché mondial de la cybersécurité. Le secteur pèse environ 85 milliards USD en 2024 et devrait atteindre près de 167 milliards d’ici 2032, avec un TCAC compris entre 7,9 % et 12,5 %.<br>
    Ce marché est soutenu par des investissements gouvernementaux massifs, la pression des assureurs cyber, et l’augmentation des coûts liés aux fuites de données (5,1 M USD par incident en moyenne).
</div>
""",
    unsafe_allow_html=True,
)
st.markdown("---")

# ============ COÛTS & TYPES D’ATTAQUES ============ #
with st.expander("📊 Voir la répartition des coûts et des attaques dans le monde"):
    st.markdown(
        "<h2 style='text-align:center;'>Cartographie des pertes dues aux cyberattaques</h2>",
        unsafe_allow_html=True,
    )
    generate_financial_loss_map(df)

    st.markdown(
        "<h2 style='text-align:center;'>Types d'attaques les plus fréquentes et leurs temps de résolution</h2>",
        unsafe_allow_html=True,
    )
    generate_attack_type_map(df)

    st.markdown(
        """
    <div class="big-text">
    Les États-Unis font face à une vague persistante de cyberattaques. En 2024, on compte près de 860 000 plaintes, pour des pertes financières estimées à 16,6 milliards USD (+33 % vs 2023).
    Le ransomware reste la menace numéro 1 (+49 % d’incidents au 1er semestre 2025), avec des coûts opérationnels dépassant souvent le million USD.
    Les PME sont particulièrement vulnérables : 1 sur 2 subit une attaque, causant parfois la fermeture définitive. Les fraudes à la cryptomonnaie pèsent désormais plus de 9,3 milliards USD.
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============ TENDANCES & INNOVATIONS ================= #
with st.expander("🛡️ Tendances du marché et innovations US"):
    display_attacks_chart()
    st.markdown(
        """
    <div class="big-text">
    <h3>💼 Marché & investissements</h3>
    Le marché américain connaît une dynamique forte, portée par la digitalisation et l’essor du cloud. 72 % des entreprises investissent dans l’IA pour détecter les menaces, et 41 % adoptent une approche “zero-trust”.

    <h3>⚔️ Cybercriminalité & IA</h3>
    En 2025, 85 % des experts alertent sur l’usage de l’IA par les hackers (phishing, deepfakes, etc.).
    Le FBI estime que la cybercriminalité représenterait la 3e “économie” mondiale après les USA et la Chine.

    <h3>📈 Prévisions</h3>
    Le marché pourrait doubler d’ici 2032. Les solutions de sécurité intégrée, la détection proactive, et les technologies post-quantiques deviendront des standards.
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============ VULNÉRABILITÉS ================= #
with st.expander("🔓 Vulnérabilités & Facteurs humains aux USA"):
    display_chart()
    st.markdown(
        """
    <div class="big-text">
    Près de 95 % des incidents de cybersécurité ont une composante humaine. Le manque de formation, les erreurs de configuration, ou le manque de rigueur dans la gestion des accès sont des vecteurs critiques.
    Le télétravail et l’hybridation des usages ont aussi multiplié les failles, notamment dans les PME qui ne disposent pas d’équipes dédiées.
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============ FOOTER ============ #
st.markdown("---")
st.markdown(
    """
*Sources : FBI IC3 (Reuters/Axios), IBM Security, Sophos, Cybersecurity Ventures, VikingCloud, MRT, Palo Alto Networks, CrowdStrike.*
"""
)

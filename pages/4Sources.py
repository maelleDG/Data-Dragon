import streamlit as st
import theme  # Importe votre fichier de thème

# Applique les configurations de page et le thème
theme.set_page_defaults()  # Optionnel si main.py gère déjà la config globale, mais bonne pratique
theme.apply_theme()

st.title("Nos Services Détaillés")

# Contenu spécifique à la page des services
st.markdown(
    """
<div class="big-text">
Découvrez en détail comment Cyber Dragon peut transformer votre approche de la sécurité et de l'analyse.
</div>
""",
    unsafe_allow_html=True,
)

st.subheader("Audit et Pentest")
st.write("Nous identifions les vulnérabilités de vos systèmes...")

# ... et ainsi de suite ...

st.header("Sources des données")

with st.expander("Cliquez pour voir les sources détaillées"):
    st.markdown(
        """
    Les informations et les termes utilisés pour générer l'étude française proviennent principalement des rapports et articles suivants :

    * **Cybermalveillance.gouv.fr :**
        * "Rapport d'activité 2024" (ou articles de synthèse des tendances de la menace).
        * "Rançongiciel ou ransomware : que faire si votre organisation est victime d'une attaque ?" (fiche réflexe).
        * https://www.cybermalveillance.gouv.fr/(https://www.cybermalveillance.gouv.fr/)
    * **ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) :**
        * "Panorama de la Cybermenace de 2018 à 2024" (disponible sur le site).
        * https://cyber.gouv.fr/(https://cyber.gouv.fr/)
    * **MordorIntelligence.com :**
        * Analyse de la taille et de la part du marché de la cybersécurité en France – Tendances et prévisions de croissance (2024 – 2029) 
        * Source: https://www.mordorintelligence.com/fr/industry-reports/france-cybersecurity-market
    """
    )

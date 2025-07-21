import streamlit as st
import theme  # Importe votre fichier de thème
from packages.def_cti import display_cti_section
from packages.paysage_cti import display_paysage_section
from packages.intro_cti import display_intro_section
from packages.niveaux_cti import display_niveaux_cti
from packages.sources_cti import display_sources_cti
from packages.strategique_cti import display_strategique_cti
from packages.analyse_cti import display_analyse_cti
from packages.approche_cti import display_approche_cti

# Applique les configurations de page et le thème
theme.set_page_defaults()
theme.apply_theme()

# Image de couverture
st.image(
    "https://i.imgur.com/eTAhEem.jpeg",
    use_container_width=True,
)

# --- Introduction Générale ---

display_intro_section()

## 1. Définition et Objectifs de la Cyber Threat Intelligence (CTI)

display_cti_section()

## 2. Le Paysage Actuel des Cybermenaces

display_paysage_section()

## 3. Les Niveaux de Cyber Threat Intelligence

display_niveaux_cti()

## 4. Sources et Éthique de la CTI

display_sources_cti()

## 5. La Valeur Stratégique de la CTI pour les Organisations

display_strategique_cti()

## 6. Analyse Coût-Bénéfice : Prévenir une Attaque est plus Rentable

display_analyse_cti()

## 7. Notre Approche en Cybersécurité : Spécialistes de la CTI pour votre PME

display_approche_cti()

st.markdown(
    f"<p style='text-align: center; color: {theme.COLORS['GREY_SLOGAN']}; font-size: 0.9em;'>© 2025 Cyber Dragon. Tous droits réservés.</p>",
    unsafe_allow_html=True,
)

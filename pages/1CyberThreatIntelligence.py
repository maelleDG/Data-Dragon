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

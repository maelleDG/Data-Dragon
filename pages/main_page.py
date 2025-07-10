import streamlit as st
import theme  # Importe votre fichier de thème
import streamlit.components.v1 as components

# Image de couverture
st.image(
    "logo_bandeau.png",
    use_container_width=True,
)

# Introduction (avec les balises <strong> pour le gras)
st.markdown(
    """
<div style="text-align: center; font-size: 24px;">
    <strong>Bienvenue chez Cyber Dragon</strong>, votre partenaire de confiance pour naviguer dans le paysage complexe de la <strong>cybersécurité</strong> et exploiter la puissance de l'<strong>analyse de données</strong>. Nous protégeons votre entreprise contre les menaces numériques tout en transformant vos données brutes en informations stratégiques.
</div>
""",
    unsafe_allow_html=True,
)


#LIVE MAP

# --- Carte dans un encadré élégant ---
components.html(
    """
    <div style='display: flex; justify-content: center;'>
        <div style='background-color: grey; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 12px rgba(0,0,0,0.2);'>
            <iframe src="https://cybermap.kaspersky.com/en/widget/dynamic/dark"
                    style="border: none; width: 80vw; max-width: 1200px; height: 700px; border-radius: 8px;">
            </iframe>
        </div>
    </div>
    """,
    height=750,
    scrolling=False
)

# --- Description centrée ---
st.markdown("""
<p style='text-align: center; font-size: 18px; color: lightgray;'>
Suivez en direct les cyberattaques détectées dans le monde par Kaspersky. Cette carte interactive vous permet de visualiser les menaces en temps réel.
</p>
""", unsafe_allow_html=True)

# --- Nos Services (Section) ---
st.markdown(
    f"<h2 class='section-title' style='text-align: center;'>Nos Services</h2>",
    unsafe_allow_html=True,
)

col_service1, col_service2 = st.columns(2)

with col_service1:
    st.markdown(
        f"""
    <div class="icon-text">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v6h-2zm0 8h2v2h-2z"/></svg>
        <span><b>Cybersécurité Avancée :</b></span>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    Nous offrons des solutions complètes pour protéger vos systèmes, réseaux et données contre les cyberattaques. De l'évaluation des vulnérabilités à la réponse aux incidents, nous assurons votre résilience numérique.
    """
    )

with col_service2:
    st.markdown(
        f"""
    <div class="icon-text">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-2 10h-4v4h4v-4zm0-6h-4v4h4V7zM7 7h4v4H7V7zm0 6h4v4H7v-4z"/></svg>
        <span><b>Analyse de Données Stratégique :</b></span>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    Transformez vos données en un avantage concurrentiel. Nos experts en data analytics révèlent les tendances, prédisent les comportements et optimisent vos processus décisionnels.
    """
    )

# --- Appel à l'Action ---

# --- Hack CSS pour centrer le st.button même sans colonnes ---
st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Appel à l'Action ---
st.markdown(
    "<h2 style='text-align: center;'>Prêt à sécuriser et optimiser votre avenir ?</h2>",
    unsafe_allow_html=True,
)

if st.button("Contactez-nous dès aujourd'hui !"):
    st.success("Merci de votre intérêt ! Nous vous contacterons bientôt.")

# --- Pied de page (optionnel) ---
st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: {theme.COLORS['GREY_SLOGAN']}; font-size: 0.9em;'>© 2025 Cyber Dragon. Tous droits réservés.</p>",  # <-- Supprimez le guillemet double en trop ici
    unsafe_allow_html=True,
)

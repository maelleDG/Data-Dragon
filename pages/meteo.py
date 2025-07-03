import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Carte Cyberattaque", page_icon="🛡️", layout="wide")

# --- Bandeau violet ---
st.markdown("""
<div style="background-color:#6a0dad; padding: 4px; border-radius: 8px; margin-bottom: 20px;"></div>
""", unsafe_allow_html=True)

# --- Titre centré ---
st.markdown("""
<h1 style='text-align: center;'>🌐 Carte mondiale des cyberattaques en temps réel</h1>
""", unsafe_allow_html=True)

# --- Description centrée ---
st.markdown("""
<p style='text-align: center; font-size: 18px; color: lightgray;'>
Suivez en direct les cyberattaques détectées dans le monde par Kaspersky. <br>
Cette carte interactive vous permet de visualiser les menaces en temps réel.
</p>
""", unsafe_allow_html=True)

# --- Carte dans un encadré élégant ---
components.html(
    """
    <div style='display: flex; justify-content: center;'>
        <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 12px rgba(0,0,0,0.2);'>
            <iframe src="https://cybermap.kaspersky.com/en/widget/dynamic/dark"
                    style="border: none; width: 80vw; max-width: 1200px; height: 700px; border-radius: 8px;">
            </iframe>
        </div>
    </div>
    """,
    height=750,
    scrolling=False
)

# --- Footer ---
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 - Dashboard Cybersécurité • Données fournies par Kaspersky</p>", unsafe_allow_html=True)





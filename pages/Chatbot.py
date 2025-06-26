import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(page_title="Projet 3", layout="wide")


 # Config de l'API
genai.configure(api_key="AIzaSyAG8NgAuuACAmFoiG8xEVKzNbrDKrcx7Bc")
 # Prompt système
system_prompt = """
Tu es un spécialiste en cyber sécurité. Tu donnes des réponses précises pour un public qui te donnera, soit une URL, une adresse mail ( a vérifier sur : https://haveibeenpwned.com/) ou un fichier que tu verifera, analysera afin de savoir si ce dernier est sûr.
Si la question ne concerne pas la cyber sécurité, indique que tu ne peux répondre qu'à ce sujet.
"""

# Fonction pour initialiser le chat
def init_chat():
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat(history=[
        {"role": "user", "parts": [system_prompt]},
        {"role": "model", "parts": ["Compris, je suis prêt à te proposer des recommandations."]}
    ])
    return chat

# Initialisation du chat
if "chat" not in st.session_state:
    st.session_state.chat = init_chat()
    st.session_state.messages = [
        {"role": "assistant", "text": "Aucune reco disponible ? 🔎 "}
    ]

# Affichage de la discussion
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# Champ de saisie
user_input = st.chat_input("URL, Adresse mail ou fichier ?")

# Traitement du message
if user_input:
    # Afficher le message de l'utilisateur
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Obtenir la réponse de Gemini
    response = st.session_state.chat.send_message(user_input)

    # Afficher la réponse du bot
    st.session_state.messages.append({"role": "assistant", "text": response.text})
    with st.chat_message("assistant"):
        st.markdown(response.text)

# Bouton de réinitialisation en dessous de la zone de texte du chatbot
if st.button("Réinitialiser SécuBot 🤖", key="reset_button"):
    st.session_state.chat = init_chat()
    st.session_state.messages = [
        {"role": "assistant", "text": "URL, Adresse mail ou fichier  ? 🔎"}
    ]
    st.rerun()
   

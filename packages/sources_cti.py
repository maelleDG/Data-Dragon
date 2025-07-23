import streamlit as st


def display_sources_cti():
    st.write(
        "La collecte d'informations pour la CTI repose sur des méthodologies rigoureuses et est menée dans le respect des cadres légaux et éthiques."
    )
    st.write("Nos analyses s'appuient sur une diversité de sources fiables :")
    st.markdown(
        """
    * ⚠️ **Renseignements Open Source (OSINT) :** Rapports publics d'agences gouvernementales (ex: ANSSI, CERT-FR), publications de chercheurs en sécurité, bases de données de vulnérabilités, actualités sectorielles.
    * 🕵️ **Surveillance des Forums Spécialisés et du Dark Web :** Monitoring des plateformes où les acteurs de la menace partagent des informations, vendent des accès ou développent de nouvelles techniques, permettant une anticipation des menaces émergentes.
    * 🔧 **Analyse de Programmes Malveillants (Malware Analysis) :** Dissection et ingénierie inverse de codes malveillants pour comprendre leurs fonctionnalités et leurs vecteurs d'infection.
    * 📊 **Flux de Menaces Commerciaux et Partenariats :** Accès à des bases de données consolidées et à des informations partagées au sein de communautés de cybersécurité professionnelles.
    * ↩️ **Retours d'Expérience Incident Response :** Analyse des incidents réels pour identifier les tactiques, techniques et procédures (TTPs) couramment utilisées et affiner les stratégies de défense.

    
    """
    )
    st.write(
        "Ces informations sont ensuite soumises à un processus d'analyse approfondie, de corrélation et de contextualisation pour générer des renseignements pertinents et directement actionnables."
    )

    st.markdown("---")

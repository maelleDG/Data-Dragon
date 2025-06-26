import streamlit as st

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
    * **NetExplorer :**
        * "Les 10 Cyberattaques qui ont marqué la France en 2024".
        * https://www.01net.com/actualites/cyberattaques-qui-marque-france-2024.html(https://www.netexplorer.fr/10-cyberattaques-qui-ont-marque-la-france-en-2024/)
    * **Ministère de l'Europe et des Affaires étrangères :**
        * "Russie – Attribution de cyberattaques contre la France au service de renseignement militaire russe (APT28)".
        * https://www.diplomatie.gouv.fr/fr/dossiers-pays/russie/evenements/evenements-de-l-annee-2025/article/russie-attribution-de-cyberattaques-contre-la-france-au-service-de(https://www.diplomatie.gouv.fr/fr/dossiers-pays/russie/evenements/evenements-de-l-annee-2025/article/russie-attribution-de-cyberattaques-contre-la-france-au-service-de)
    """
    )

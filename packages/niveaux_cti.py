import streamlit as st


def display_niveaux_cti():
    st.write(
        "La CTI est structurée en plusieurs niveaux, chacun offrant une granularité d'information différente, essentielle pour une défense stratifiée et efficace."
    )

    cti_data = {
        "Niveau": ["Stratégique", "Tactique", "Opérationnel"],
        "Signification": [
            "Vue d'ensemble des tendances macro, des motivations des attaquants, et de l'impact potentiel sur le secteur d'activité ou la géographie de l'organisation.",
            "Détails sur les Techniques, Tactiques et Procédures (TTPs) spécifiques employées par les acteurs de la menace, y compris leurs outils et méthodes d'approche.",
            "Informations hautement techniques et spécifiques (Indicateurs de Compromission - IoCs) tels que des adresses IP malveillantes, des noms de domaine, ou des signatures de logiciels malveillants.",
        ],
        "Exemple d'Application :": [
            "Comprendre que les organisations du **secteur des services financiers** sont activement ciblées par des groupes cybercriminels spécialisés dans l'exfiltration de données pour la revente.",
            "Apprendre que des groupes spécifiques utilisent des **campagnes de spear-phishing personnalisées** via des plateformes professionnelles, se faisant passer pour des recruteurs, afin d'introduire des logiciels espions.",
            "Recevoir une alerte sur un fichier exécutable spécifique nommé “Report_Q2_2025.exe” qui contient un nouveau variant de rançongiciel, avec ses signatures cryptographiques et les règles de détection correspondantes pour un SIEM (Security Information and Event Management).",
        ],
    }
    st.table(cti_data)

    st.markdown("---")

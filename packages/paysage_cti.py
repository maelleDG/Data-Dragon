import streamlit as st


def display_paysage_section():
    st.subheader("💥 La Réalité des Cybermenaces :")
    st.write(
        "Les cybercriminels adoptent des stratégies de plus en plus diversifiées et opportunistes. "
        "Aucune entité n'est à l'abri, et la perception d'être une cible secondaire est un risque en soi. Le volume et la sophistication des cyberattaques sont en constante augmentation, rendant toute organisation, quelle que soit sa taille ou son secteur d'activité, potentiellement vulnérable."
    )
    st.header("Principaux types de cyberattaques")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("🛡️ **Attaques par Rançongiciel (Ransomware)**"):
            st.write(
                """
            Ces attaques paralysent les opérations en chiffrant les données critiques, exigeant une rançon pour leur restitution. 
            L'impact peut être financier, opérationnel et réputationnel.
            """
            )

        with st.expander("🎣 **Hameçonnage (Phishing) et Ingénierie Sociale**"):
            st.write(
                """
            Ces techniques manipulent le facteur humain pour obtenir des informations confidentielles, 
            des accès non autorisés, ou initier des actions frauduleuses.
            """
            )

    with col2:
        with st.expander("🐛 **Exploitation de Vulnérabilités**"):
            st.write(
                """
            Les attaquants exploitent les failles de sécurité connues ou inconnues (zero-day) dans les logiciels et systèmes 
            pour s'infiltrer et compromettre les infrastructures.
            """
            )

        with st.expander("🔗 **Attaques sur la Chaîne d'Approvisionnement**"):
            st.write(
                """
            La compromission d'un maillon plus faible dans l'écosystème d'une organisation peut servir de vecteur 
            pour atteindre des cibles principales.
            """
            )

    st.markdown("---")

    st.image(
        "https://i.imgur.com/f0UDGBP.png",
        use_container_width=True,
    )

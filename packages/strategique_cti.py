import streamlit as st


def display_strategique_cti():
    st.image(
        "https://i.imgur.com/HEPD3hh.jpeg",
        use_container_width=True,
    )

    st.write(
        "L'intégration de la CTI permet à toute organisation de passer d'une posture de **réactivité subie** à une stratégie de **sécurité proactive et prédictive**."
    )
    st.header("💡 Bénéfices Clés de la CTI :")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("☢️​ **Anticipation des Menaces :**"):
            st.write(
                """
            Identifier et comprendre les risques avant qu'ils ne se matérialisent, offrant une fenêtre de tir pour renforcer les défenses.
            """
            )

        with st.expander("​🔝​ **Allocation Optimale des Ressources :**"):
            st.write(
                """
            Orienter les investissements en sécurité vers les domaines les plus pertinents, en fonction des menaces spécifiques à l'écosystème de l'organisation.
            """
            )
        with st.expander("🤝​ **Renforcement de la Confiance des Parties Prenantes :**"):
            st.write(
                """
            Démontrer un engagement fort envers la protection des données et des systèmes, consolidant la réputation et la confiance des clients et partenaires.
            """
            )

    with col2:
        with st.expander("💲 **Minimisation des Coûts d'Incident :**"):
            st.write(
                """
            La prévention est intrinsèquement plus économique que la gestion d'une crise cybernétique, qui peut engendrer des pertes financières considérables.
            """
            )

        with st.expander("​​📝​ **Garantie de Continuité d'Activité :**"):
            st.write(
                """
            Réduire drastiquement les interruptions opérationnelles dues aux cyberattaques, assurant la résilience et la fluidité des opérations.
            """
            )

    st.subheader("🛡️ Applications Concrètes de la CTI :")
    st.markdown(
        """
    * Si la CTI révèle une **campagne d'hameçonnage ciblée** sur un secteur d'activité particulier, les équipes de sécurité peuvent **sensibiliser le personnel et préparer des défenses spécifiques** *avant* que ces attaques ne soient reçues.
    * L'identification d'une **vulnérabilité critique** dans un logiciel largement utilisé, et son exploitation active par des cybercriminels, permet une **mise à jour prioritaire** des systèmes, prévenant ainsi une compromission.
    * La CTI peut fournir des **listes d'adresses IP ou de noms de domaine** connus pour héberger des infrastructures malveillantes, permettant leur **blocage proactif au niveau du périmètre réseau**.
    """
    )

    st.markdown("---")

import streamlit as st


def display_approche_cti():

    st.write(
        "En tant qu'agence spécialisée en cybersécurité, notre mission est de fournir de la **visibilité sur les menaces**, des **outils concrets de prévention**, et une **capacité de réaction agile** pour garantir la sécurité et la continuité des opérations."
    )

    st.subheader("✅ Comment nous accompagnons spécifiquement les PME :")
    st.write(
        "Bien que la CTI soit pertinente pour toute entité, nous avons développé une expertise particulière dans l'adaptation de ses principes et de ses outils aux besoins spécifiques des Petites et Moyennes Entreprises, qui n'ont pas toujours les ressources internes dédiées."
    )
    st.markdown(
        """
    * **Veille CTI Proactive et Personnalisée :** Nous mettons en place une surveillance continue des menaces les plus pertinentes pour votre secteur d'activité, vos technologies et votre contexte opérationnel de PME.
    * **Alertes Contextualisées et Actionnables :** Nous diffusons des notifications claires, sans jargon excessif, accompagnées de recommandations précises sur les actions à entreprendre, directement adaptées aux réalités des PME.
    * **Programmes de Sensibilisation Ciblé :** Des formations adaptées aux contraintes de temps et aux niveaux de connaissance des équipes de PME, les préparant aux techniques d'ingénierie sociale et aux vecteurs d'attaque émergents.
    * **Diagnostic Cybersécurité Initial :** Nous proposons un diagnostic pour évaluer la posture de sécurité actuelle de votre PME et identifier les vulnérabilités prioritaires.
    * **Support Réactif et Expert :** Une ligne dédiée pour toute interrogation sur une activité suspecte ou un besoin d'assistance rapide en cas d'incident de sécurité, dimensionnée pour la réactivité nécessaire aux PME.
    """
    )

    st.markdown("---")

    st.info(
        "N'hésitez pas à nous contacter pour une analyse approfondie de vos besoins et l'élaboration d'une stratégie de Cyber Threat Intelligence sur mesure pour votre organisation. **Comment pouvons-nous vous accompagner dans la sécurisation de votre futur numérique ?**"
    )

    st.markdown("---")

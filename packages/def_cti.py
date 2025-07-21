import streamlit as st


def display_cti_section():
    st.markdown("## 1. Définition et Objectifs de la Cyber Threat Intelligence (CTI)")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(
            """✅
        La Cyber Threat Intelligence (CTI) est le processus rigoureux de **collecte, d'analyse et d'interprétation d'informations** relatives aux menaces cybernétiques. Son objectif principal est de transformer des données brutes en **renseignements exploitables et contextualisés**, permettant de comprendre les motivations, les capacités techniques et les stratégies des cyberadversaires.
        """
        )

    with col2:
        center_col_left, center_col_image, center_col_right = st.columns([1, 2, 1])
        with center_col_image:
            st.image(
                "https://images.unsplash.com/photo-1508674861872-a51e06c50c9b?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                width=200,
            )

    with col3:
        st.write(
            """🤔
        La CTI vise également à **informer les décisions stratégiques** en matière de cybersécurité, en fournissant des analyses sur les tendances émergentes et les menaces potentielles. En intégrant la CTI dans leur stratégie de sécurité, les organisations peuvent mieux se préparer à faire face à un paysage de menaces en constante évolution.
        """
        )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        center_col_left, center_col_image, center_col_right = st.columns([1, 2, 1])
        with center_col_image:
            st.image(
                "https://plus.unsplash.com/premium_photo-1683134684062-e3d753eb77d0?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                width=200,
            )

    with col2:
        st.write(
            """📡​
        Plus qu'une simple surveillance, la CTI agit comme un **système de renseignement avancé pour la cybersécurité**. Elle permet d'anticiper les vecteurs d'attaque potentiels, les tactiques employées par les acteurs malveillants et les cibles privilégiées. Cette approche prédictive offre la capacité d'adapter les défenses de manière proactive, minimisant ainsi les risques d'incidents avant même qu'ils ne se manifestent.
        """
        )

    with col3:
        center_col_left, center_col_image, center_col_right = st.columns([1, 2, 1])
        with center_col_image:
            st.image(
                "https://images.unsplash.com/photo-1480160734175-e2209654433c?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                width=200,
            )

    st.markdown("---")

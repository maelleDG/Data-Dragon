import streamlit as st


def display_analyse_cti():
    st.write(
        "La mise en œuvre de la CTI représente un investissement stratégique dont le retour est significatif face aux coûts potentiels d'une cyberattaque."
    )

    attack_costs = {
        "Conséquence d’une Attaque": [
            "Interruption totale ou partielle de l'activité (ex: rançongiciel)",
            "Compromission ou Exfiltration de Données (Clients, Propriété Intellectuelle)",
            "Coûts de Récupération et de Remise en État des Systèmes",
            "Paiement de Rançon (fortement déconseillé, sans garantie de résultat)",
        ],
        "Estimation des Coûts Associés (Directs et Indirects)": [
            "De **5 000 € à 30 000 € par jour** d'inactivité (pertes de revenus, salaires, pénalités contractuelles).",
            "Sanctions réglementaires (amendes RGPD/CNIL pouvant atteindre 20 M€ ou 4% du CA mondial), atteinte irréversible à la réputation, perte de confiance client.",
            "Plusieurs jours/semaines d'intervention d'experts en forensique, coûts de remplacement matériel et logiciel. Potentiellement **plus de 20 000 €**.",
            "De **500 € à 50 000 €** (sans garantie de récupération des données et incitant de futures attaques).",
        ],
    }
    st.table(attack_costs)

    st.subheader("💬 L'Impact de la CTI :")
    st.write(
        "Grâce à une stratégie de CTI proactive, le risque d'impact financier d'une cyberattaque peut être **réduit de 70% ou plus**. En anticipant les menaces, votre organisation peut bloquer les attaques ou y réagir en quelques minutes, évitant ainsi des interruptions prolongées de plusieurs jours."
    )

    col1, col2 = st.columns(2)

    with col1:
        # Crée de NOUVELLES sous-colonnes pour centrer l'image dans col1
        center_col1_left, center_col1_image, center_col1_right = st.columns([1, 2, 1])

        with center_col1_image:  # Place l'image dans la sous-colonne du milieu de col1
            st.image("https://i.imgur.com/AjhE1bc.png")

    with col2:
        # Crée de NOUVELLES sous-colonnes pour centrer l'image dans col2
        center_col2_left, center_col2_image, center_col2_right = st.columns([1, 2, 1])

        with center_col2_image:  # Place l'image dans la sous-colonne du milieu de col2
            st.image("https://i.imgur.com/L3TJvAs.png")

    st.markdown("---")

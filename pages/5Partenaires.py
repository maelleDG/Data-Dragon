import streamlit as st
import theme  # Importe votre fichier de thème

# Applique les configurations de page et le thème
theme.set_page_defaults()  # Optionnel si main.py gère déjà la config globale, mais bonne pratique
theme.apply_theme()

# Image de couverture
st.image(
    "https://i.imgur.com/oQU7pnC.jpeg",
    use_container_width=True,
)

col1, col2 = st.columns(
    [1, 2]
)  # Crée deux colonnes avec des largeurs relatives de 1 et 2

with col1:
    st.image(
        "https://yt3.googleusercontent.com/juvDMrQFoVWi6_iacPYKRhwa4X1HOskYQ8fhMzyLoEx-MzGaAinkPRRMsKSIu6Ai8uqY99q0hJw=s900-c-k-c0x00ffffff-no-rj",
        use_container_width=True,
    )

with col2:
    st.header("Services de Orange Cyberdefense")

    with st.expander("Cyber Threat Intelligence (CTI) : "):
        st.write(
            """
        Collecte, analyse et diffusion de renseignements sur les menaces pour anticiper les attaques. Ils développent leurs propres bases de données de menaces.
        """
        )
    with st.expander("Managed Detection and Response (MDR) : "):
        st.write(
            """
        Surveillance 24/7 des systèmes d'information, détection proactive des menaces, qualification des alertes et plans d'action de remédiation par leurs experts CyberSOC.\n
        MicroSOC Mobiles: \n
        Pour les offres dédiées aux mobiles, on trouve des services de détection managés à partir de 3 euros par poste et par mois pour un grand nombre de postes (par exemple, 1000 postes).
        """
        )
    with st.expander("Réponse à Incident (CERT) : "):
        st.write(
            """
        La réponse à Incident proposé par Orange Cyberdefense et les options du digital Forensic qui l'accompagnent, constituent une assurance efficace contre les menaces cyber. \n
        Elle permet d'identifier et qualifier les comportements suspects, de réagir rapidement pour contrer les attaques avérées connues dès leur détection et d'éviter tout nouvelles cyberattaques.
        """
        )
        st.image(
            "https://www.orangecyberdefense.com/fileadmin/_processed_/2/9/csm_Illustration_Reponse_a_incident_gestion_de_crise_cyber_5757844d89.png",
            use_container_width=True,
        )
    with st.expander("Cyber Surveillance / Brand Protection : "):
        st.write(
            """
        Surveillance proactive des menaces potentielles pour la marque à l'extérieur de l'entreprise (clonage de sites web/applications, piratage de comptes réseaux sociaux, fuites de données sur le dark web).\n
        Si vous disposez de plusieurs postes à protéger, n'hésitez pas à contacter votre service client afin de commander plusieurs licences pours vos ordinateurs :\n
        Cyber Protection 3 postes - 19€HT/mois\n 
        Cyber Protection 6 postes - 39€HT/mois \n
        Cyber Protection 10 postes - 65€HT/mois \n
        Cyber Protection 19 postes - 89€HT/mois \n
        Cyber Protection 30 postes - 129€HT/mois \n
        """
        )
    with st.expander("Gestion des vulnérabilités : "):
        st.write(
            """
        Veille, scan, qualification des vulnérabilités et surveillance des données sensibles pour identifier les failles et les corriger.
        """
        )
    with st.expander("Cyber-résilience et gestion de crise : "):
        st.write(
            """
        Nos experts accompagnent les entreprises dans la définition, la mise en œuvre et l'évaluation des dispositifs permettant d'assurer la continuité des activités en cas de cyberattaque ou de sinistre majeur. \n 
        Nos prestations sont les suivantes :\n
        > Audits des dispositifs de continuité d'activité informatique et métier \n
        > Cartographie des actifs sensibles (bilan d'impacts sur l'activité) \n
        > Définition des organisations de crise \n
        > Accompagnement à leur mise en œuvre \n
        > Organisation et animation d'exercices de gestion de crise \n
        > Étude des politiques et stratégies de continuité (PCA/PCM/PRA/PSI…).
        """
        )
    with st.expander("Visitez leurs autres solutions"):
        st.write(
            """
        Visitez [Orange Cyberdefense](https://www.orangecyberdefense.com/fr/).
        """
        )

st.markdown("---")

col1, col2 = st.columns(
    [1, 2]
)  # Crée deux colonnes avec des largeurs relatives de 1 et 2

with col1:
    st.image(
        "https://media.licdn.com/dms/image/v2/D5605AQFdrLpFXI2AQA/videocover-high/videocover-high/0/1732576920424?e=2147483647&v=beta&t=A58jgSJd8-JwQ_fAomQPvDAFmcWEWLWUTPGCtYa6kM0",
        use_container_width=True,
    )

with col2:
    st.header("Services de Thales Cyberdefense")

    with st.expander("Cybel Risk & Threat Evaluation : "):
        st.write(
            """
        Évaluation Cyber et Définition de la Stratégie : Cette étape consiste à évaluer les mesures cyber existantes, à analyser les risques, à identifier les menaces et à élaborer des plans d'action pour se conformer aux réglementations telles que NIST, ISO27001, RGPD et NIS2.\n
        Mise en œuvre de la Stratégie Cyber : Cette étape se concentre sur la définition et l'application de politiques et de procédures de cybersécurité (par exemple, exigences de mot de passe, sécurité des e-mails, traitement des données sensibles, plans de réponse aux incidents) et sur l'utilisation de tableaux de bord cyber et d'indicateurs clés de performance (KPI) pour le suivi.\n
        Contrôle Cyber : Cela inclut l'audit des processus de cybersécurité et des structures de gouvernance pour identifier les lacunes et la réalisation de simulations de crise cyber pour tester la résilience.\n
        CISOaaS (CISO as a Service) / DPOaaS : Thales offre un accès à des experts en cybersécurité et à un support technique pour renforcer la gouvernance informatique et se préparer aux menaces futures.
        """
        )
    with st.expander("Services de détection & réponse : "):
        st.write(
            """
        Cyber Threat Intelligence\n
        Optimiser les capacités de détection grâce à l'utilisation du cyber renseignement transmis par nos équipes\n
        Capitaliser sur des analystes qui couvrent l'ensemble du renseignement cyber, avec une expertise dans le partage de renseignements, d'indicateurs et de rapports opérationnels permettant une cybersécurité proactive.\n
        Qu'il s'agisse d'infrastructures nationales critiques, de gouvernements à travers le monde, nos équipes de Cyber Threat Intelligence partagent les dernières menaces, indicateurs et sources avec les clients, enrichissant de surcroit le SOC de Thales.\n
        """
        )
        st.image(
            "https://cds.thalesgroup.com/sites/default/files/2024-03/schema-detect_0.svg",
            use_container_width=True,
        )
    with st.expander("Formation Cyber & Experimentation : "):
        st.write(
            """
        L'offre de formation et d'expérimentation cyber de Thales, est un service complet de cybersécurité conçu pour permettre une pratique immersive, s'appuyant au besoin, sur la réplication réaliste de scénarios d'attaque cyber. En mettant l'accent sur l'accompagnement des clients, Thales apporte à une forte expertise sur la plupart des domaines cyber, y compris des cas d'usage spécifiques.\n
        Via une solide infrastructure de formation, Thales s'engage à couvrir tous les domaines critiques de la cybersécurité, allant de l'aéronautique à la défense, en passant par les secteurs industriels (OT), spatial, bancaires, navals, automobiles, etc. \n
        Nous comprenons le besoin continu de former des professionnels de la cybersécurité et ce, dans divers contextes de pratique pour garantir la résilience contre les menaces actuelles et émergentes.     
        """
        )
        st.image(
            "https://cds.thalesgroup.com/sites/default/files/2024-03/cyber-training-schema.jpg",
            use_container_width=True,
        )
    with st.expander("Visitez leurs autres solutions"):
        st.write(
            """
        Visitez [Cyber Solutions by Thales](https://cds.thalesgroup.com/fr).
        """
        )

st.markdown("---")

col1, col2 = st.columns(
    [1, 2]
)  # Crée deux colonnes avec des largeurs relatives de 1 et 2

with col1:
    st.image(
        "https://companieslogo.com/img/orig/CAP.PA-9b4110b0.png?t=1720244491",
        use_container_width=True,
    )

with col2:
    st.header("Services de Capgemini Cyberdefense")

    with st.expander("Conseils, audits et évaluation : "):
        st.write(
            """
        Cartographie des données et classification\n
        Analyse de risque, vulnérabilité\n
        Threat intelligence, audit de code source\n
        Audit organisationnel et d'architecture
        """
        )
    with st.expander("Protection (implémentation & intégration) : "):
        st.write(
            """
        IAM (gestion des identités et accès)\n
        Protection de la donnée, applications, postes de travail, réseaux\n
        Sécurisation des terminaux mobiles, cryptographie, architectures Zero Trust
        """
        )
    with st.expander("Sécurité gérée (exploitation) : "):
        st.write(
            """
        SIEM, SOC (centre opérationnel de sécurité)\n
        Log management, dashboards de sécurité\n
        Réponse à incident, analyses forensiques\n
        Contrôles continus
        """
        )
    with st.expander("Tarification (indicative) : "):
        st.write(
            """
        Formation (Capgemini Institut)\n
        Exemples de formations spécialisées:\n
        «Sécurisez votre système d'info» (3 jours) : 2995€ HT/pers \n
        «Solutions techniques pour sécuriser votre SI» (3 jours) : 2995€ HT/pers \n
        Modules sur IA, ransomware, IAM, NIS v2 : 2295€ à 2995€ HT/pers \n
        \n
        Projets / prestations personnalisées\n
        Modèle ROI/valeur : de 120-230€/h pour du conseil classique\n
        Projets sur mesure : tarifs variables, de 50000€ pour de petits projets à >1M€ pour engagements stratégiques \n
        Services sous forme d'abonnement (digital platforms) : ≈300€/mois + échelles selon usages \n
        Grands contrats (bundles + longue durée) : 0,5-5M€ voire plus, avec remises 10-20%\n
        Également, le TJM (tarif journalier moyen) facturé à l'État français par Capgemini peut atteindre 1500€/jour, mais varie selon le profil et le secteur\n
        """
        )
    with st.expander("Visitez leurs autres solutions"):
        st.write(
            """
        Visitez [Cyber4Good by Capgemini](https://www.capgemini.com/fr-fr/services/cybersecurite/).
        """
        )

st.markdown("---")
st.markdown(
    f"<p style='text-align: center; color: {theme.COLORS['GREY_SLOGAN']}; font-size: 0.9em;'>© 2025 Cyber Dragon. Tous droits réservés.</p>",
    unsafe_allow_html=True,
)

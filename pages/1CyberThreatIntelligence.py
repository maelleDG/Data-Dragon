import streamlit as st
import theme  # Importe votre fichier de thème

# Applique les configurations de page et le thème
theme.set_page_defaults()  # Optionnel si main.py gère déjà la config globale, mais bonne pratique
theme.apply_theme()

# Image de couverture
st.image(
    "https://i.imgur.com/eTAhEem.jpeg",
    use_container_width=True,
)

# --- Introduction Générale ---
st.title(
    "La Cyber Threat Intelligence (CTI), composante essentielle de la cybersécurité"
)
st.write(
    """
Dans un paysage numérique en constante évolution, la **compréhension proactive des menaces cybernétiques** est devenue un impératif pour la résilience de toute organisation. Cette présentation vise à démystifier la **Cyber Threat Intelligence (CTI)** et à illustrer comment son intégration peut significativement renforcer la posture de sécurité d'une entité, en la prémunissant contre des risques financiers et opérationnels majeurs.
"""
)

st.markdown("---")

## 1. Définition et Objectifs de la Cyber Threat Intelligence (CTI)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(
        """✅
    La Cyber Threat Intelligence (CTI) est le processus rigoureux de **collecte, d'analyse et d'interprétation d'informations** relatives aux menaces cybernétiques. Son objectif principal est de transformer des données brutes en **renseignements exploitables et contextualisés**, permettant de comprendre les motivations, les capacités techniques et les stratégies des cyberadversaires.
    """
    )

with col2:

    center_col_left, center_col_image, center_col_right = st.columns([1, 2, 1])

    with center_col_image:  # Placez l'image dans la sous-colonne du milieu
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

    with center_col_image:  # Placez l'image dans la sous-colonne du milieu
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

    with center_col_image:  # Placez l'image dans la sous-colonne du milieu
        st.image(
            "https://images.unsplash.com/photo-1480160734175-e2209654433c?q=80&w=880&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            width=200,
        )


st.markdown("---")

## 2. Le Paysage Actuel des Cybermenaces


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

## 3. Les Niveaux de Cyber Threat Intelligence

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

## 4. Sources et Éthique de la CTI

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

## 5. La Valeur Stratégique de la CTI pour les Organisations

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

## 6. Analyse Coût-Bénéfice : Prévenir une Attaque est plus Rentable

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

## 7. Notre Approche en Cybersécurité : Spécialistes de la CTI pour votre PME

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
st.markdown(
    f"<p style='text-align: center; color: {theme.COLORS['GREY_SLOGAN']}; font-size: 0.9em;'>© 2025 Cyber Dragon. Tous droits réservés.</p>",
    unsafe_allow_html=True,
)

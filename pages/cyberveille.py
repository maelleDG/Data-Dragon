import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv
import theme  # Importe votre fichier de thème
from packages.collecte import NewsCollector
from packages.cybermeteo_ia import CyberThreatChatbot
from collections import Counter
from datetime import datetime, timedelta
import plotly.express as px

load_dotenv()

# Applique les configurations de page et le thème
theme.set_page_defaults()  # Optionnel si main.py gère déjà la config globale, mais bonne pratique
theme.apply_theme()


@st.cache_resource
def initialize_components():
    return NewsCollector(), CyberThreatChatbot()


def cyberveille():
    # En-tête principal
    st.markdown(
        """
    <div class="main-header">
        <h1>🔒 Cyber Threat Intelligence</h1>
        <p style="text-align: center; color: white; margin: 0;">Système de Veille Technologique & Chatbot Météo Cybercriminalité</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Initialisation
    collecte, cybermeteo_ia = initialize_components()

    # Sidebar pour les paramètres
    st.sidebar.title("⚙️ Configuration")

    # Configuration des APIs
    st.sidebar.subheader("🔌 Configuration APIs")

    # NewsAPI
    with st.sidebar.expander("📰 NewsAPI"):
        # Vérifie si la clé API est présente
        has_newsapi_key = bool(collecte.apis_config["newsapi"]["api_key"])

        # La checkbox est initialisée à True si la clé est présente et l'API est déjà activée
        # Ou à False si la clé est absente ou si l'API était désactivée.
        newsapi_enabled_from_ui = st.checkbox(
            "Activer NewsAPI",
            value=collecte.apis_config["newsapi"]["enabled"]
            and has_newsapi_key,  # Coché si clé présente ET déjà activé
            disabled=not has_newsapi_key,  # Désactive la checkbox si pas de clé
            help="Cochez pour activer NewsAPI. Nécessite une clé API configurée dans le fichier .env",
        )

        # Met à jour l'état d'activation de l'API dans l'objet 'collecte'
        # Seulement si l'état de la checkbox a changé ou si c'est la première exécution
        if newsapi_enabled_from_ui != collecte.apis_config["newsapi"]["enabled"]:
            collecte.configure_api("newsapi", enabled=newsapi_enabled_from_ui)
            st.rerun()  # Reruns pour appliquer le changement immédiatement

        if has_newsapi_key:
            if collecte.apis_config["newsapi"]["enabled"]:
                st.success("✅ NewsAPI est configuré et actif.")
            else:
                st.info(
                    "ℹ️ NewsAPI est configuré mais désactivé. Cochez la case pour l'activer."
                )
        else:
            st.warning(
                "⚠️ NewsAPI n'est pas configuré. Veuillez définir NEWS_API_KEY dans votre fichier .env pour l'activer."
            )

    # GNews API
    with st.sidebar.expander("🌐 GNews API"):
        has_gnews_key = bool(collecte.apis_config["gnews"]["api_key"])

        gnews_enabled_from_ui = st.checkbox(
            "Activer GNews API",
            value=collecte.apis_config["gnews"]["enabled"] and has_gnews_key,
            disabled=not has_gnews_key,
            help="Cochez pour activer GNews API. Nécessite une clé API configurée dans le fichier .env",
        )

        if gnews_enabled_from_ui != collecte.apis_config["gnews"]["enabled"]:
            collecte.configure_api("gnews", enabled=gnews_enabled_from_ui)
            st.rerun()

        if has_gnews_key:
            if collecte.apis_config["gnews"]["enabled"]:
                st.success("✅ GNews API est configuré et actif.")
            else:
                st.info(
                    "ℹ️ GNews API est configuré mais désactivé. Cochez la case pour l'activer."
                )
        else:
            st.warning(
                "⚠️ GNews API n'est pas configuré. Veuillez définir GNEWS_API_KEY dans votre fichier .env pour l'activer."
            )

    # Flux RSS
    with st.sidebar.expander("📡 Flux RSS"):
        # Garder cette checkbox car les RSS n'ont pas de clé API externe
        rss_enabled = st.checkbox(
            "Activer RSS", value=collecte.apis_config["rss_feeds"]["enabled"]
        )
        if rss_enabled != collecte.apis_config["rss_feeds"]["enabled"]:
            collecte.configure_api("rss_feeds", enabled=rss_enabled)
            st.rerun()
        st.write("Sources RSS actives:")
        for feed in collecte.apis_config["rss_feeds"]["feeds"]:
            st.write(f"• {feed}")

    # Reddit
    with st.sidebar.expander("🤖 Reddit"):
        reddit_enabled = st.checkbox(
            "Activer Reddit", value=collecte.apis_config["reddit"]["enabled"]
        )
        collecte.configure_api("reddit", enabled=reddit_enabled)
        st.write("Subreddits surveillés:")
        for sub in collecte.apis_config["reddit"]["subreddits"]:
            st.write(f"• r/{sub}")

    st.sidebar.markdown("---")

    # Paramètres de collecte
    st.sidebar.subheader("🔍 Collecte d'Articles")
    search_query = st.sidebar.text_input(
        "Mots-clés de recherche", value="cybersécurité France"
    )
    max_articles = st.sidebar.slider("Nombre d'articles", 5, 50, 20)
    auto_refresh = st.sidebar.checkbox("Actualisation automatique", value=False)

    if auto_refresh:
        refresh_interval = st.sidebar.slider("Intervalle (minutes)", 1, 60, 5)

    # Filtres
    st.sidebar.subheader("Filtres")
    threat_levels = st.sidebar.multiselect(
        "Niveaux de menace",
        ["critical", "high", "medium", "low"],
        default=["critical", "high", "medium", "low"],
    )

    categories = st.sidebar.multiselect(
        "Catégories",
        [
            "Ransomware",
            "Phishing",
            "Malware",
            "Data Breach",
            "Infrastructure",
            "APT",
            "Vulnerability",
            "DDoS",
            "General",
        ],
        default=[
            "Ransomware",
            "Phishing",
            "Malware",
            "Data Breach",
            "Infrastructure",
            "APT",
            "Vulnerability",
            "DDoS",
            "General",
        ],
    )

    # Bouton de collecte
    if st.sidebar.button("🔄 Actualiser les données", type="primary"):
        with st.spinner("Collecte des articles en cours..."):
            articles = collecte.search_news(search_query, max_articles)
            st.session_state.articles = articles
            st.success(f"✅ {len(articles)} articles collectés")

    # Initialisation des données si nécessaire
    if "articles" not in st.session_state:
        st.session_state.articles = collecte.search_news(search_query, max_articles)

    # Onglets principaux
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Dashboard", "📰 Articles", "🤖 Chatbot Météo", "📈 Analyses"]
    )

    with tab1:
        st.header("📊 Dashboard de Veille")

        # Métriques principales
        col1, col2, col3, col4 = st.columns(4)

        articles = st.session_state.articles

        with col1:
            st.metric("📰 Total Articles", len(articles))

        with col2:
            critical_count = sum(
                1 for a in articles if a.get("threat_level") == "critical"
            )
            st.metric("🔴 Menaces Critiques", critical_count)

        with col3:
            high_count = sum(1 for a in articles if a.get("threat_level") == "high")
            st.metric("🟠 Menaces Élevées", high_count)

        with col4:
            today_count = sum(
                1
                for a in articles
                if a["published_date"].date() == datetime.now().date()
            )
            st.metric("📅 Aujourd'hui", today_count)

        # Graphiques
        col1, col2 = st.columns(2)

        with col1:
            # Répartition par niveau de menace
            threat_counts = Counter(a.get("threat_level", "unknown") for a in articles)
            fig_threat = px.pie(
                values=list(threat_counts.values()),
                names=list(threat_counts.keys()),
                title="Répartition par Niveau de Menace",
                color_discrete_map={
                    "critical": "#ff4444",
                    "high": "#ff8800",
                    "medium": "#ffcc00",
                    "low": "#44ff44",
                },
            )
            st.plotly_chart(fig_threat, use_container_width=True)

        with col2:
            # Évolution temporelle
            df_time = pd.DataFrame(articles)
            df_time["published_date"] = pd.to_datetime(
                df_time["published_date"].astype(str), utc=True, errors="coerce"
            )
            df_time["date"] = df_time["published_date"].dt.date
            time_counts = df_time.groupby("date").size().reset_index(name="count")

            fig_time = px.line(
                time_counts,
                x="date",
                y="count",
                title="Évolution du Nombre d'Articles",
                markers=True,
            )
            st.plotly_chart(fig_time, use_container_width=True)

    with tab2:
        st.header("📰 Articles de Presse")
        # Filtrage des articles
        filtered_articles = [
            a
            for a in articles
            if a.get("threat_level") in threat_levels
            and a.get("category") in categories
        ]

        st.write(f"Affichage de {len(filtered_articles)} articles")

        # Affichage des articles
        for article in filtered_articles:
            threat_level = article.get("threat_level", "unknown")
            threat_class = f"threat-level-{threat_level}"
            api_source = article.get("api_source", "unknown")

            # Icône selon la source API
            source_icons = {
                "newsapi": "📰",
                "gnews": "🌐",
                "rss": "📡",
                "reddit": "🤖",
                "simulation": "🔄",
            }
            source_icon = source_icons.get(api_source, "📄")

            st.markdown(
                f"""
            <div class="news-card">
                <h3>{source_icon} {article['title']}</h3>
                <div class="{threat_class}">
                    Niveau de menace: {threat_level.upper()}
                </div>
                <p><strong>Source:</strong> {article['source']} | 
                   <strong>Date:</strong> {article['published_date'].strftime('%d/%m/%Y %H:%M')} |
                   <strong>Catégorie:</strong> {article.get('category', 'N/A')} |
                   <strong>API:</strong> {api_source}</p>
                <p>{article['summary']}</p>
                <p><strong>Mots-clés:</strong> {', '.join(article.get('keywords', []))}</p>
                <a href="{article['url']}" target="_blank">🔗 Lire l'article complet</a>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with tab3:
        st.header("🤖 Chatbot Météo Cybercriminalité")

        st.markdown(
            """
        <div class="chatbot-container">
            <h4>💬 Assistant Cyber Threat Intelligence</h4>
            <p>Posez-moi vos questions sur la cybersécurité en France ou demandez un rapport météo !</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Historique des conversations
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Affichage de l'historique
        for i, (question, response) in enumerate(st.session_state.chat_history):
            st.markdown(
                f"""
            <div class="chat-message">
                <strong>Vous:</strong> {question}
            </div>
            <div class="chat-response">
                <strong>Assistant:</strong> {response}
            </div>
            """,
                unsafe_allow_html=True,
            )

        # Interface de chat
        user_input = st.text_input(
            "Votre question:",
            placeholder="Ex: Donne-moi la météo cybercriminalité actuelle",
        )

        col1, col2, col3 = st.columns([1, 1, 4])

        with col1:
            if st.button("📤 Envoyer"):
                if user_input:
                    response = cybermeteo_ia.respond_to_query(user_input)
                    st.session_state.chat_history.append((user_input, response))
                    st.rerun()

        with col2:
            if st.button("🌡️ Météo"):
                weather_report = cybermeteo_ia.get_weather_report()
                st.session_state.chat_history.append(
                    "Météo cybercriminalité", weather_report
                )
                st.rerun()

        # Raccourcis
        st.subheader("🔧 Raccourcis")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📊 Tendances actuelles"):
                response = "📈 **Tendances Cybersécurité France**\n\n• Hausse de 40% des attaques par ransomware\n• Multiplication des campagnes de phishing ciblant les PME\n• Émergence de nouvelles techniques d'ingénierie sociale\n• Augmentation des attaques sur les infrastructures critiques"
                st.session_state.chat_history.append("Tendances actuelles", response)
                st.rerun()

        with col2:
            if st.button("🎯 Secteurs à risque"):
                response = "🎯 **Secteurs les plus ciblés en France**\n\n1. **Santé** - Hôpitaux et cliniques\n2. **Éducation** - Universités et écoles\n3. **Collectivités** - Mairies et services publics\n4. **Finance** - Banques et assurances\n5. **Industrie** - PME manufacturières"
                st.session_state.chat_history.append("Secteurs à risque", response)
                st.rerun()

        with col3:
            if st.button("🛡️ Recommandations"):
                response = "🛡️ **Recommandations de sécurité**\n\n• Mettre en place une authentification multi-facteurs\n• Former régulièrement les employés aux risques cyber\n• Maintenir les systèmes à jour\n• Effectuer des sauvegardes régulières\n• Surveiller les activités réseau\n• Établir un plan de réponse aux incidents"
                st.session_state.chat_history.append("Recommandations", response)
                st.rerun()

    with tab4:
        st.header("📈 Analyses Approfondies")

        # Analyse des mots-clés
        st.subheader("🔍 Analyse des Mots-clés")

        all_keywords = []
        for article in articles:
            all_keywords.extend(article.get("keywords", []))

        if all_keywords:
            keyword_counts = Counter(all_keywords)
            top_keywords = keyword_counts.most_common(10)

            fig_keywords = px.bar(
                x=[k[1] for k in top_keywords],
                y=[k[0] for k in top_keywords],
                orientation="h",
                title="Top 10 des Mots-clés",
                labels={"x": "Fréquence", "y": "Mots-clés"},
            )
            st.plotly_chart(fig_keywords, use_container_width=True)

        # Analyse des sources
        st.subheader("📰 Analyse des Sources")

        source_counts = Counter(a["source"] for a in articles)
        fig_sources = px.bar(
            x=list(source_counts.keys()),
            y=list(source_counts.values()),
            title="Répartition par Source",
            labels={"x": "Source", "y": "Nombre d'articles"},
        )
        st.plotly_chart(fig_sources, use_container_width=True)

        # Heatmap des menaces par catégorie
        st.subheader("🔥 Heatmap des Menaces")

        threat_category_matrix = {}
        for article in articles:
            category = article.get("category", "Unknown")
            threat_level = article.get("threat_level", "unknown")

            if category not in threat_category_matrix:
                threat_category_matrix[category] = {}
            if threat_level not in threat_category_matrix[category]:
                threat_category_matrix[category][threat_level] = 0
            threat_category_matrix[category][threat_level] += 1

        # Conversion en DataFrame pour la heatmap
        if threat_category_matrix:
            df_heatmap = pd.DataFrame(threat_category_matrix).fillna(0)

            fig_heatmap = px.imshow(
                df_heatmap,
                title="Heatmap: Catégories vs Niveaux de Menace",
                color_continuous_scale="Reds",
                aspect="auto",
            )
            st.plotly_chart(fig_heatmap, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown(
        f"""
        <div style="text-align: center; color: #666; margin-top: 2rem;">
            <p style='text-align: center; color: {theme.COLORS['GREY_SLOGAN']}; font-size: 0.9em;'>© 2025 Cyber Dragon. Tous droits réservés.</p>
            <p>Dernière mise à jour: {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    cyberveille()

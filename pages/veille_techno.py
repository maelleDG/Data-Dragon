import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import feedparser
import re
from datetime import datetime, timedelta
import theme  # Importe votre fichier de thème

# Applique les configurations de page et le thème
theme.set_page_defaults()  # Optionnel si main.py gère déjà la config globale, mais bonne pratique
theme.apply_theme()

# --- Définition des catégories et mots-clés ---
# Dictionnaire des catégories de menaces et des mots-clés associés (en minuscules pour une correspondance insensible à la casse)
THREAT_CATEGORIES = {
    "Ransomware": ["ransomware", "rançongiciel", "cryptolocker", "wannacry", "notpetya"],
    "Phishing": ["phishing", "hameçonnage", "spear phishing", "fraude", "email fraud"],
    "APT (Advanced Persistent Threat)": ["apt", "advanced persistent threat", "groupe de menaces", "state-sponsored"],
    "Vulnérabilité": ["vulnerability", "vulnérabilité", "exploit", "cve", "patch", "zero-day"],
    "Malware": ["malware", "logiciel malveillant", "virus", "trojan", "ver", "spyware", "rootkit", "adware"],
    "Fuite de Données": ["data breach", "fuite de données", "violation de données", "compromission", "data leak"],
    "DDoS": ["ddos", "denial of service", "attaque par déni de service"],
    "Cryptojacking": ["cryptojacking", "minage de crypto"],
    "Attaque Chaîne d'Approvisionnement": ["supply chain attack", "attaque chaîne d'approvisionnement"],
    "Sécurité IoT": ["iot security", "sécurité iot", "internet des objets"],
    "Sécurité Cloud": ["cloud security", "sécurité cloud", "cloud computing"],
    "Ingénierie Sociale": ["social engineering", "ingénierie sociale", "arnaque", "scam"],
    "Authentification": ["authentication", "authentification", "mfa", "2fa", "credential stuffing"],
    "Zero Trust": ["zero trust", "zero-trust"],
    "Conformité/Régulation": ["gdpr", "rgpd", "compliance", "conformité", "regulation"],
    "Menace Interne": ["insider threat", "menace interne"],
    "Sécurité Mobile": ["mobile security", "sécurité mobile", "android security", "ios security"],
}

# --- Fonctions de collecte de données ---

def categorize_article(title, summary):
    """
    Catégorise un article basé sur les mots-clés présents dans son titre et son résumé.
    Retourne une liste de catégories correspondantes ou ['Non catégorisé'] si aucune correspondance.
    """
    found_categories = []
    text_to_analyze = (title + " " + summary).lower()

    for category, keywords in THREAT_CATEGORIES.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_to_analyze): # Utilise re.search pour des correspondances de mots entiers
                found_categories.append(category)
                break # Passe à la catégorie suivante une fois qu'un mot-clé est trouvé pour cette catégorie
    
    if not found_categories:
        return ["Non catégorisé"]
    return sorted(list(set(found_categories))) # Retourne des catégories uniques et triées

def get_rss_feed_data(url):
    """
    Récupère les articles d'un flux RSS et les enrichit avec une catégorie.
    """
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            title = entry.title if hasattr(entry, "title") else "No title"
            link = entry.link if hasattr(entry, "link") else "No link"
            summary = entry.summary if hasattr(entry, "summary") else "No summary"
            published = (
                entry.published_parsed if hasattr(entry, "published_parsed") else None
            )
            published_date = (
                datetime(*published[:6]).strftime("%Y-%m-%d %H:%M:%S")
                if published
                else "N/A"
            )
            
            # Catégorisation de l'article
            categories = categorize_article(title, summary)

            articles.append(
                {
                    "Source": url,
                    "Titre": title,
                    "Lien": link,
                    "Résumé": summary,
                    "Date": published_date,
                    "Catégories": categories,  # Nouvelle colonne pour les catégories
                }
            )
        return articles
    except Exception as e:
        st.warning(f"Impossible de récupérer le flux RSS de {url}: {e}")
        return []

# --- Configuration des sources ---
SOURCES_CTI = {
    "Flux RSS": [
        "https://www.cert.ssi.gouv.fr/alerte/feed/",
        "https://www.cert.ssi.gouv.fr/cti/feed/",
        "https://www.cert.ssi.gouv.fr/actualite/feed/",
        "https://threatpost.com/feed/",
        "https://feeds.feedburner.com/TheHackersNews",
        "https://www.bleepingcomputer.com/feed/",
        "https://www.misp-project.org/feed",
    ],
}

# --- Interface Streamlit ---

st.title("🛡️ Veille Cyber Threat Intelligence (CTI)")
st.markdown(
    "Bienvenue dans votre tableau de bord de veille sur les cybermenaces. Explorez les dernières actualités et analyses."
)

# Sidebar pour les filtres
st.sidebar.header("Options de la veille")
date_filter = st.sidebar.date_input(
    "Filtrer par date (depuis)", datetime.now() - timedelta(days=7)
)
search_query = st.sidebar.text_input("Rechercher par mot-clé")

# Récupérer toutes les catégories uniques pour le multiselect
all_available_categories = sorted(list(THREAT_CATEGORIES.keys()) + ["Non catégorisé"])
selected_categories = st.sidebar.multiselect(
    "Filtrer par Type de Menace / Catégorie",
    options=all_available_categories,
)

# Bouton pour lancer la veille
if st.sidebar.button("Lancer la veille / Actualiser"):
    all_articles = []

    st.info("Collecte des données via les flux RSS...")
    for rss_url in SOURCES_CTI["Flux RSS"]:
        articles = get_rss_feed_data(rss_url)
        all_articles.extend(articles)

    if all_articles:
        df = pd.DataFrame(all_articles)
        df["Date"] = pd.to_datetime(
            df["Date"]
        )  # Convertir en datetime pour le filtrage
        st.session_state["data"] = df
        st.success(f"{len(df)} articles collectés.")
    else:
        st.warning("Aucun article n'a pu être collecté. Vérifiez vos sources.")
else:
    if "data" not in st.session_state:
        st.info(
            "Cliquez sur 'Lancer la veille / Actualiser' pour commencer la collecte."
        )

# Affichage des résultats
if "data" in st.session_state:
    df_filtered = st.session_state["data"].copy()

    # Appliquer le filtre de date
    df_filtered = df_filtered[df_filtered["Date"] >= pd.to_datetime(date_filter)]

    # Appliquer le filtre par mot-clé
    if search_query:
        df_filtered = df_filtered[
            df_filtered.apply(
                lambda row: search_query.lower()
                in row.astype(str).str.lower().to_string(),
                axis=1,
            )
        ]

    # Appliquer le filtre par catégorie
    if selected_categories:
        # Un article peut avoir plusieurs catégories, donc nous vérifions si au moins une des catégories sélectionnées est présente
        df_filtered = df_filtered[
            df_filtered["Catégories"].apply(
                lambda article_categories: any(cat in selected_categories for cat in article_categories)
            )
        ]

    st.subheader(f"Articles collectés ({len(df_filtered)} résultats)")

    if not df_filtered.empty:
        # Afficher les articles dans des expanders ou une table
        for index, row in df_filtered.sort_values(
            by="Date", ascending=False
        ).iterrows():
            with st.expander(
                f"**{row['Titre']}** (Source: {row['Source'].split('//')[1].split('/')[0]} - {row['Date'].strftime('%Y-%m-%d %H:%M')})"
            ):
                st.write(f"**Résumé:** {row['Résumé']}")
                st.markdown(f"**Lien:** [Lire l'article]({row['Lien']})")
    else:
        st.info("Aucun article ne correspond à vos critères de recherche.")

st.sidebar.markdown("---")
st.sidebar.markdown("Développé avec ❤️ et Streamlit")

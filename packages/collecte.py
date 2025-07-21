import streamlit as st
import requests
from datetime import datetime, timezone
from typing import List, Dict, Any
import pandas as pd
from collections import Counter
import hashlib
import feedparser
import theme  # Importe votre fichier de thème
import os
from dotenv import load_dotenv
from dateutil import parser

# Charger les variables d'environnement au début du script
load_dotenv()


# Classe pour la collecte d'articles
class NewsCollector:
    def __init__(self):
        self.cyber_keywords = [
            "ransomware",
            "malware",
            "phishing",
            "cybersécurité",
            "cyberattaque",
            "piratage",
            "violation données",
            "sécurité informatique",
            "cyber menace",
            "hacking",
            "virus informatique",
            "trojan",
            "botnet",
            "APT",
            "cryptolocker",
            "spyware",
            "zero-day",
            "vulnérabilité",
            "ANSSI",
            "CNIL",
            "RGPD",
            "breach",
            "cyber espionnage",
            "dark web",
        ]

        # Configuration des APIs
        self.apis_config = {
            "newsapi": {
                "enabled": True,
                "api_key": os.getenv("NEWSAPI_KEY"),
                "base_url": "https://newsapi.org/v2/everything",
            },
            "gnews": {
                "enabled": True,
                "api_key": os.getenv("GNEWS_KEY"),
                "base_url": "https://gnews.io/api/v4/search",
            },
            "otx": {
                "enabled": True,
                "api_key": os.getenv("OTX_VAULT_KEY"),
                "base_url": "https://otx.alienvault.com/api/v1",
            },
            "rss_feeds": {
                "enabled": True,
                "feeds": [
                    "https://www.cert.ssi.gouv.fr/feed/",
                    "https://www.anssi.gouv.fr/fr/rss.xml",
                    "https://feeds.feedburner.com/TheHackersNews",
                    "https://feeds.feedburner.com/securityweek",
                    "https://threatpost.com/feed/",
                    "https://www.misp-project.org/feed.xml",
                ],
            },
            "reddit": {
                "enabled": True,
                "subreddits": ["cybersecurity", "netsec", "france"],
            },
        }

    def configure_api(self, api_name: str, api_key: str = None, enabled: bool = True):
        """Configure une API spécifique"""
        if api_name in self.apis_config:
            self.apis_config[api_name]["enabled"] = enabled
            if api_key:
                self.apis_config[api_name]["api_key"] = api_key
            return True
        return False

    def _to_utc_aware(self, date_input: Any) -> datetime:
        """
        Convertit une chaîne de date/heure ou un objet datetime en un objet datetime UTC-aware.
        Gère les cas où la chaîne pourrait être tz-naive ou dans des formats variés.
        """
        if isinstance(date_input, datetime):
            dt_object = date_input
        elif isinstance(date_input, str):
            if not date_input:
                return datetime.now(
                    timezone.utc
                )  # Retourne l'heure actuelle en UTC si la chaîne est vide
            try:
                dt_object = parser.parse(date_input)
            except ValueError:
                st.warning(
                    f"Impossible de parser la date '{date_input}'. Utilisation de la date actuelle en UTC."
                )
                return datetime.now(timezone.utc)
        else:
            st.warning(
                f"Type de date inattendu '{type(date_input)}'. Utilisation de la date actuelle en UTC."
            )
            return datetime.now(timezone.utc)

        # Si l'objet datetime est tz-naive, suppose qu'il est en UTC et rend-le tz-aware.
        if dt_object.tzinfo is None:
            dt_object = dt_object.replace(tzinfo=timezone.utc)
        else:
            # Si l'objet est déjà tz-aware, convertis-le en UTC
            dt_object = dt_object.astimezone(timezone.utc)

        return dt_object

    def search_newsapi(self, query: str, max_results: int = 10) -> List[Dict]:
        """Collecte via NewsAPI"""
        if (
            not self.apis_config["newsapi"]["enabled"]
            or not self.apis_config["newsapi"]["api_key"]
        ):
            return []

        try:
            params = {
                "q": f"{query} AND (cybersecurity OR cybersécurité OR cyberattaque)",
                "language": "fr",
                "sortBy": "publishedAt",
                "pageSize": max_results,
                "apiKey": self.apis_config["newsapi"]["api_key"],
            }

            response = requests.get(
                self.apis_config["newsapi"]["base_url"], params=params
            )
            response.raise_for_status()

            data = response.json()
            articles = []

            for item in data.get("articles", []):
                published_at_utc = self._to_utc_aware(item["publishedAt"])
                article = {
                    "id": hashlib.md5(item["url"].encode()).hexdigest()[:8],
                    "title": item["title"],
                    "source": item["source"]["name"],
                    "published_date": published_at_utc,  # Date en UTC
                    "url": item["url"],
                    "summary": item["description"] or item["content"][:200] + "...",
                    "threat_level": self.analyze_threat_level(
                        {"title": item["title"], "summary": item["description"]}
                    ),
                    "category": self.categorize_article(
                        item["title"] + " " + (item["description"] or "")
                    ),
                    "keywords": self.extract_keywords(
                        item["title"] + " " + (item["description"] or "")
                    ),
                    "api_source": "newsapi",
                }
                articles.append(article)

            return articles

        except Exception as e:
            st.error(f"Erreur NewsAPI: {str(e)}")
            return []

    def search_gnews(self, query: str, max_results: int = 10) -> List[Dict]:
        """Collecte via GNews API"""
        if (
            not self.apis_config["gnews"]["enabled"]
            or not self.apis_config["gnews"]["api_key"]
        ):
            return []

        try:
            params = {
                "q": f"{query} cybersécurité",
                "lang": "fr",
                "country": "fr",
                "max": max_results,
                "apikey": self.apis_config["gnews"]["api_key"],
            }

            response = requests.get(
                self.apis_config["gnews"]["base_url"], params=params
            )
            response.raise_for_status()

            data = response.json()
            articles = []

            for item in data.get("articles", []):
                published_at_utc = self._to_utc_aware(item["publishedAt"])
                article = {
                    "id": hashlib.md5(item["url"].encode()).hexdigest()[:8],
                    "title": item["title"],
                    "source": item["source"]["name"],
                    "published_date": published_at_utc,  # Date en UTC
                    "url": item["url"],
                    "summary": item["description"][:200] + "...",
                    "threat_level": self.analyze_threat_level(
                        {"title": item["title"], "summary": item["description"]}
                    ),
                    "category": self.categorize_article(
                        item["title"] + " " + item["description"]
                    ),
                    "keywords": self.extract_keywords(
                        item["title"] + " " + item["description"]
                    ),
                    "api_source": "gnews",
                }
                articles.append(article)

            return articles

        except Exception as e:
            st.error(f"Erreur GNews: {str(e)}")
            return []

    def search_rss_feeds(self, max_results: int = 10) -> List[Dict]:
        """Collecte via flux RSS"""
        if not self.apis_config["rss_feeds"]["enabled"]:
            return []

        articles = []

        for feed_url in self.apis_config["rss_feeds"]["feeds"]:
            try:
                feed = feedparser.parse(feed_url)

                for entry in feed.entries[
                    : max_results // len(self.apis_config["rss_feeds"]["feeds"])
                ]:
                    # Vérifier si l'article contient des mots-clés cyber
                    content = (
                        entry.get("title", "") + " " + entry.get("summary", "")
                    ).lower()
                    if any(keyword in content for keyword in self.cyber_keywords):

                        published_date = self._to_utc_aware(
                            entry.get("published") or entry.get("updated")
                        )

                        summary = entry.get("summary", "")
                        if summary:
                            summary = (
                                (summary[:197] + "...")
                                if len(summary) > 200
                                else summary
                            )
                        else:
                            summary = "Pas de résumé disponible."

                        article = {
                            "id": hashlib.md5(entry.link.encode()).hexdigest()[:8],
                            "title": entry.title,
                            "source": feed.feed.get("title", "RSS Feed"),
                            "published_date": published_date,
                            "url": entry.link,
                            "summary": entry.get("summary", "")[:200] + "...",
                            "threat_level": self.analyze_threat_level(
                                {
                                    "title": entry.title,
                                    "summary": entry.get("summary", ""),
                                }
                            ),
                            "category": self.categorize_article(
                                entry.title + " " + entry.get("summary", "")
                            ),
                            "keywords": self.extract_keywords(
                                entry.title + " " + entry.get("summary", "")
                            ),
                            "api_source": "rss",
                        }
                        articles.append(article)

            except Exception as e:
                st.warning(f"Erreur RSS {feed_url}: {str(e)}")
                continue

        return articles[:max_results]

    def search_reddit(self, query: str, max_results: int = 10) -> List[Dict]:
        """Collecte via Reddit API (sans authentification)"""
        if not self.apis_config["reddit"]["enabled"]:
            return []

        articles = []

        for subreddit in self.apis_config["reddit"]["subreddits"]:
            try:
                url = f"https://www.reddit.com/r/{subreddit}/search.json"
                params = {
                    "q": query,
                    "restrict_sr": "true",
                    "sort": "new",
                    "limit": max_results
                    // len(self.apis_config["reddit"]["subreddits"]),
                }

                headers = {"User-Agent": "CyberThreatIntelligence/1.0"}
                response = requests.get(url, params=params, headers=headers)

                if response.status_code == 200:
                    data = response.json()

                    for post in data["data"]["children"]:
                        post_data = post["data"]

                        # Filtrer les posts liés à la cybersécurité
                        content = (
                            post_data.get("title", "")
                            + " "
                            + post_data.get("selftext", "")
                        ).lower()
                        if any(keyword in content for keyword in self.cyber_keywords):
                            published_date_utc = self._to_utc_aware(
                                datetime.fromtimestamp(post_data["created_utc"])
                            )

                            summary = post_data.get("selftext", "")
                            if summary:
                                summary = (
                                    (summary[:197] + "...")
                                    if len(summary) > 200
                                    else summary
                                )
                            else:
                                summary = "Pas de résumé disponible."
                            article = {
                                "id": post_data["id"],
                                "title": post_data["title"],
                                "source": f"Reddit r/{subreddit}",
                                "published_date": published_date_utc,
                                "url": f"https://reddit.com{post_data['permalink']}",
                                "summary": post_data.get("selftext", "")[:200] + "...",
                                "threat_level": self.analyze_threat_level(
                                    {
                                        "title": post_data["title"],
                                        "summary": post_data.get("selftext", ""),
                                    }
                                ),
                                "category": self.categorize_article(
                                    post_data["title"]
                                    + " "
                                    + post_data.get("selftext", "")
                                ),
                                "keywords": self.extract_keywords(
                                    post_data["title"]
                                    + " "
                                    + post_data.get("selftext", "")
                                ),
                                "api_source": "reddit",
                            }
                            articles.append(article)

            except Exception as e:
                st.warning(f"Erreur Reddit r/{subreddit}: {str(e)}")
                continue

        return articles[:max_results]

    def search_threat_intelligence_feeds(self) -> List[Dict]:
        """Collecte depuis les flux de threat intelligence"""
        articles = []

        # Flux AlienVault OTX
        try:
            otx_articles = self.fetch_otx_pulses()
            articles.extend(otx_articles)
        except Exception as e:
            st.warning(f"OTX non disponible: {str(e)}")

        return articles

    def fetch_otx_pulses(self) -> List[Dict]:
        """Récupère les pulses AlienVault OTX et les formate en articles."""
        otx_config = self.apis_config.get("otx", {})
        if not otx_config.get("enabled") or not otx_config.get("api_key"):
            st.info("AlienVault OTX est désactivé ou la clé API est manquante.")
            return []

        pulses_url = f"{otx_config['base_url']}/pulses/subscribed"
        headers = {"X-OTX-API-KEY": otx_config["api_key"]}
        articles = []

        try:
            # Effectue la requête à l'API OTX
            response = requests.get(
                pulses_url, headers=headers, timeout=10
            )  # Ajout d'un timeout
            response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP (4xx ou 5xx)

            data = response.json()

            # Parcourt les pulses reçus
            for pulse in data.get("results", []):
                # OTX ne donne pas toujours un summary très complet ou une URL unique par "article".
                # Nous construisons un résumé et une URL de référence.
                summary_content = pulse.get(
                    "description", pulse.get("name", "Pas de description.")
                )
                # Prend les 200 premiers caractères pour le résumé
                summary_formatted = (
                    (summary_content[:197] + "...")
                    if len(summary_content) > 200
                    else summary_content
                )

                # L'URL du pulse sur le site OTX
                pulse_url = f"https://otx.alienvault.com/pulse/{pulse.get('id', '')}"

                # Date de publication
                published_date = datetime.now(timezone.utc)  # Valeur par défaut
                if pulse.get("modified"):
                    try:
                        # OTX utilise un format ISO pour la date modifiée
                        published_date = self._to_utc_aware(pulse["modified"])
                    except ValueError:
                        pass  # Garde la date par défaut si le format est incorrect

                # Extraction des indicateurs comme mots-clés (exemple simple)
                indicators_keywords = []
                for indicator in pulse.get("indicators", []):
                    indicators_keywords.append(indicator.get("indicator", ""))

                # Concaténer le nom du pulse et la description pour l'analyse
                full_content_for_analysis = (
                    pulse.get("name", "") + " " + summary_content
                )

                article = {
                    "id": hashlib.md5(pulse_url.encode()).hexdigest()[
                        :8
                    ],  # ID basé sur l'URL du pulse
                    "title": pulse.get("name", "Pulse OTX sans titre"),
                    "source": "AlienVault OTX",
                    "published_date": published_date,
                    "url": pulse_url,
                    "summary": summary_formatted,
                    "threat_level": self.analyze_threat_level(
                        {"title": pulse.get("name", ""), "summary": summary_content}
                    ),
                    "category": self.categorize_article(full_content_for_analysis),
                    "keywords": self.extract_keywords(full_content_for_analysis)
                    + indicators_keywords,  # Ajout des IOCs aux mots-clés
                    "api_source": "otx",
                }
                articles.append(article)

            return articles

        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de requête OTX: {e}")
            return []
        except ValueError as e:
            st.error(f"Erreur de parsing JSON OTX: {e}")
            return []
        except Exception as e:
            st.error(
                f"Une erreur inattendue est survenue lors de la récupération OTX: {e}"
            )
            return []

    def categorize_article(self, content: str) -> str:
        """Catégorise un article selon son contenu"""
        content_lower = content.lower()

        categories = {
            "Ransomware": ["ransomware", "cryptolocker", "wannacry", "petya"],
            "Phishing": ["phishing", "hameçonnage", "email", "social engineering"],
            "Malware": ["malware", "trojan", "virus", "botnet", "spyware"],
            "Data Breach": ["violation données", "fuite", "breach", "rgpd"],
            "Infrastructure": ["infrastructure", "scada", "iot", "industriel"],
            "APT": ["apt", "advanced persistent threat", "espionnage"],
            "Vulnerability": ["vulnérabilité", "cve", "zero-day", "patch"],
            "DDoS": ["ddos", "déni de service", "attaque volumétrique"],
        }

        for category, keywords in categories.items():
            if any(keyword in content_lower for keyword in keywords):
                return category

        return "General"

    def extract_keywords(self, content: str) -> List[str]:
        """Extrait les mots-clés pertinents"""
        content_lower = content.lower()
        found_keywords = []

        for keyword in self.cyber_keywords:
            if keyword in content_lower:
                found_keywords.append(keyword)

        return found_keywords[:5]  # Limite à 5 mots-clés

    def search_news(self, query: str, max_results: int = 10) -> List[Dict]:
        """Méthode principale de collecte combinant toutes les sources"""
        all_articles = []

        # Collecter depuis différentes sources
        if self.apis_config["newsapi"]["enabled"]:
            newsapi_articles = self.search_newsapi(query, max_results // 4)
            all_articles.extend(newsapi_articles)

        if self.apis_config["gnews"]["enabled"]:
            gnews_articles = self.search_gnews(query, max_results // 4)
            all_articles.extend(gnews_articles)

        if self.apis_config["otx"]["enabled"]:
            otx_articles = self.fetch_otx_pulses()
            all_articles.extend(otx_articles)

        if self.apis_config["rss_feeds"]["enabled"]:
            rss_articles = self.search_rss_feeds(max_results // 4)
            all_articles.extend(rss_articles)

        if self.apis_config["reddit"]["enabled"]:
            reddit_articles = self.search_reddit(query, max_results // 4)
            all_articles.extend(reddit_articles)

        # Déduplication par URL
        seen_urls = set()
        unique_articles = []
        for article in all_articles:
            if article["url"] not in seen_urls:
                seen_urls.add(article["url"])
                unique_articles.append(article)

        return unique_articles[:max_results]

    def analyze_threat_level(self, article: Dict) -> str:
        """Analyse le niveau de menace d'un article"""
        critical_keywords = [
            "ransomware",
            "zero-day",
            "APT",
            "infrastructure critique",
            "cryptolocker",
        ]
        high_keywords = [
            "malware",
            "violation données",
            "cyberattaque",
            "breach",
            "botnet",
        ]
        medium_keywords = ["phishing", "vulnérabilité", "hacking", "trojan"]

        content = f"{article.get('title', '')} {article.get('summary', '')}".lower()

        if any(keyword in content for keyword in critical_keywords):
            return "critical"
        elif any(keyword in content for keyword in high_keywords):
            return "high"
        elif any(keyword in content for keyword in medium_keywords):
            return "medium"
        else:
            return "low"

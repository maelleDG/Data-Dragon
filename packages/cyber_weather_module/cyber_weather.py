import streamlit as st
import requests
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any
import pandas as pd
from collections import Counter
import hashlib
import feedparser
import os
from dotenv import load_dotenv
from dateutil import parser
from packages.collecte import NewsCollector


def get_daily_cyber_articles(
    query: str = "cybersécurité France", max_articles: int = 50
) -> List[Dict]:
    """
    Récupère les articles de cybersécurité du jour ciblant spécifiquement la France.
    """
    try:
        collector = NewsCollector()
        all_articles = collector.search_news(query, max_results=max_articles)

        # Vérifier que all_articles est bien une liste
        if not isinstance(all_articles, list):
            print(
                f"❌ Erreur: search_news a retourné {type(all_articles)}, attendu: list"
            )
            return []

        articles_today = []
        # Nous utilisons aujourd'hui - 1 jour pour capturer les articles publiés hier soir
        # qui pourraient être considérés comme "du jour" le matin.
        # Ou simplement la date d'aujourd'hui, selon la précision souhaitée.
        today_date_utc = datetime.now(timezone.utc).date()
        yesterday_date_utc = (datetime.now(timezone.utc) - timedelta(days=1)).date()

        for article in all_articles:
            try:
                # Vérifier que l'article a la structure attendue
                if not isinstance(article, dict):
                    print(f"❌ Article ignoré: format invalide {type(article)}")
                    continue

                if "published_date" not in article:
                    print(f"❌ Article ignoré: pas de published_date")
                    continue

                # Gérer différents types de dates
                pub_date = article["published_date"]
                if isinstance(pub_date, str):
                    pub_date = parser.parse(pub_date)

                if (
                    pub_date.date() == today_date_utc
                    or pub_date.date() == yesterday_date_utc
                ):  # Inclure hier soir
                    # Filtrer les articles plus spécifiquement pour la France
                    title = article.get("title", "")
                    summary = article.get("summary", "")
                    content = (title + " " + summary).lower()

                    if (
                        "france" in content
                        or "française" in content
                        or "anssi" in content
                        or "cnil" in content
                        or article.get("api_source") == "gnews"
                    ):
                        articles_today.append(article)
            except Exception as e:
                print(f"❌ Erreur traitement article: {e}")
                continue

        return articles_today

    except Exception as e:
        print(f"❌ Erreur dans get_daily_cyber_articles: {e}")
        return []


def analyze_daily_cyber_weather(articles: List[Dict]) -> Dict:
    """
    Analyse les articles du jour pour synthétiser la "météo cybercriminalité".
    """
    if not articles:
        return {
            "threat_level": "Faible",
            "summary": "Aucune activité cyber significative n'a été détectée en France aujourd'hui.",
            "categories": {},
            "keywords": {},
            "article_count": 0,
            "relevant_articles": [],
        }

    try:
        # Vérifier que les articles ont les champs nécessaires
        threat_levels = []
        categories = []
        all_keywords = []

        for article in articles:
            # Extraire threat_level avec valeur par défaut
            threat_level = article.get("threat_level", "unknown")
            threat_levels.append(threat_level)

            # Extraire category avec valeur par défaut
            category = article.get("category", "général")
            categories.append(category)

            # Extraire keywords avec valeur par défaut
            keywords = article.get("keywords", [])
            if isinstance(keywords, list):
                all_keywords.extend(keywords)
            elif isinstance(keywords, str):
                all_keywords.append(keywords)

        # Niveau de menace dominant
        threat_level_counts = Counter(threat_levels)
        # Mapping des niveaux de menace pour un classement
        threat_ranking = {"critical": 4, "high": 3, "medium": 2, "low": 1, "unknown": 0}

        # Déterminer le niveau de menace global
        if "critical" in threat_level_counts and threat_level_counts["critical"] > 0:
            overall_threat = "Élevé (Attention Critique)"
        elif "high" in threat_level_counts and threat_level_counts["high"] > 0:
            overall_threat = "Élevé"
        elif "medium" in threat_level_counts and threat_level_counts["medium"] > 0:
            overall_threat = "Modéré"
        else:
            overall_threat = "Faible"  # Par défaut si pas de menaces fortes

        # Synthèse du résumé
        summary_phrases = []
        if overall_threat == "Élevé (Attention Critique)":
            summary_phrases.append(
                "Aujourd'hui, la météo cyber en France est **critique**, avec des alertes majeures concernant :"
            )
        elif overall_threat == "Élevé":
            summary_phrases.append(
                "La météo cyber en France est **élevée**, signalant une activité significative autour des :"
            )
        elif overall_threat == "Modéré":
            summary_phrases.append(
                "Une activité cyber **modérée** est observée en France, principalement autour des sujets suivants :"
            )
        else:
            summary_phrases.append(
                "La météo cyber en France est **calme** aujourd'hui, avec peu d'incidents signalés. Quelques sujets d'intérêt :"
            )

        # Catégories dominantes
        most_common_categories = Counter(categories).most_common(3)
        for cat, count in most_common_categories:
            summary_phrases.append(
                f"- {cat} ({count} article{'s' if count > 1 else ''})"
            )

        # Mots-clés les plus fréquents
        most_common_keywords = Counter(all_keywords).most_common(5)
        if most_common_keywords:
            summary_phrases.append(
                "\nMots-clés récurrents : "
                + ", ".join([kw for kw, _ in most_common_keywords])
            )

        # Ajout d'une phrase de conclusion
        summary_phrases.append(
            "\nRestez vigilants et appliquez les bonnes pratiques de sécurité."
        )

        return {
            "threat_level": overall_threat,
            "summary": "\n".join(summary_phrases),
            "categories": dict(Counter(categories)),
            "keywords": dict(Counter(all_keywords)),
            "article_count": len(articles),
            "relevant_articles": articles,  # Garde les articles pour référence si besoin
        }

    except Exception as e:
        print(f"❌ Erreur dans analyze_daily_cyber_weather: {e}")
        return {
            "threat_level": "Erreur",
            "summary": f"Erreur lors de l'analyse des articles: {e}",
            "categories": {},
            "keywords": {},
            "article_count": 0,
            "relevant_articles": [],
        }


def get_cyber_weather_for_chatbot() -> str:
    """
    Fonction principale à appeler par le chatbot pour obtenir le résumé quotidien.
    """
    try:
        print("Collecting daily cyber articles...")
        articles = get_daily_cyber_articles(
            query="cybersécurité France", max_articles=75
        )  # Augmentez si nécessaire
        print(f"Found {len(articles)} relevant articles for today/yesterday.")

        print("Analyzing cyber weather...")
        weather_report = analyze_daily_cyber_weather(articles)

        report_text = f"**Météo Cybercriminalité en France du {datetime.now(timezone.utc).strftime('%d/%m/%Y')}**\n\n"
        report_text += (
            f"**Niveau de menace général :** {weather_report['threat_level']}\n\n"
        )
        report_text += weather_report["summary"]

        if weather_report["article_count"] > 0:
            report_text += "\n\n**Quelques titres d'articles pertinents :**\n"
            # Afficher quelques titres d'articles les plus menaçants ou récents
            threat_ranking = {
                "critical": 4,
                "high": 3,
                "medium": 2,
                "low": 1,
                "unknown": 0,
            }

            sorted_articles = sorted(
                weather_report["relevant_articles"],
                key=lambda x: (
                    threat_ranking.get(x.get("threat_level", "unknown"), 0),
                    x.get("published_date", datetime.now(timezone.utc)),
                ),
                reverse=True,
            )[
                :5
            ]  # Prend les 5 articles les plus pertinents/menaçants

            for i, article in enumerate(sorted_articles):
                title = article.get("title", "Titre non disponible")
                source = article.get("source", "Source inconnue")
                threat_level = article.get("threat_level", "unknown")
                url = article.get("url", "#")

                report_text += f"- **{title}** (Source: {source}, Menace: {threat_level.capitalize()})\n"
                report_text += f"  Lien: {url}\n"
        else:
            report_text += "\n\nAucun article significatif n'a été trouvé pour établir une météo cyber détaillée aujourd'hui. Le calme règne sur le cyberespace français."

        return report_text

    except Exception as e:
        print(f"❌ Erreur dans get_cyber_weather_for_chatbot: {e}")
        return f"❌ Erreur lors de la génération du rapport météo cyber: {e}"

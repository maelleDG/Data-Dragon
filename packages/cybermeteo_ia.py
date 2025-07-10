import streamlit as st
import requests
from datetime import datetime, timedelta
import json
import time
import re
from typing import List, Dict, Any
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from collections import Counter
import hashlib
import feedparser
import theme  # Importe votre fichier de thème
import os
from dotenv import load_dotenv


class CyberThreatChatbot:
    def __init__(self):
        self.knowledge_base = {
            "ransomware": "Le ransomware est un type de malware qui chiffre les fichiers d'une victime et demande une rançon pour les déchiffrer. En France, les attaques de ransomware ont augmenté de 255% en 2023.",
            "phishing": "Le phishing est une technique d'ingénierie sociale utilisée pour voler des informations sensibles. L'ANSSI rapporte que 80% des incidents de sécurité en France impliquent du phishing.",
            "anssi": "L'ANSSI (Agence nationale de la sécurité des systèmes d'information) est l'autorité française en matière de cybersécurité. Elle publie régulièrement des alertes et des recommandations.",
            "rgpd": "Le RGPD encadre la protection des données personnelles en Europe. Les violations peuvent entraîner des amendes jusqu'à 4% du chiffre d'affaires annuel mondial.",
            "malware": "Les malwares sont des logiciels malveillants conçus pour endommager ou compromettre les systèmes informatiques. La France fait face à une recrudescence des attaques malware ciblant les PME.",
        }

    def get_weather_report(self) -> str:
        """Génère un rapport météo cybercriminalité pour la France"""
        current_threats = {
            "Ransomware": "Niveau ÉLEVÉ - Activité intense détectée",
            "Phishing": "Niveau MOYEN - Campagnes ciblant les PME",
            "Malware Banking": "Niveau CRITIQUE - Nouvelle famille identifiée",
            "Vulnérabilités": "Niveau MOYEN - Patches disponibles",
            "Social Engineering": "Niveau ÉLEVÉ - Augmentation des tentatives",
        }

        report = "🌡️ **MÉTÉO CYBERCRIMINALITÉ FRANCE**\n\n"
        report += f"📅 **Date**: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        report += "🎯 **Principales menaces actuelles**:\n"

        for threat, level in current_threats.items():
            if "CRITIQUE" in level:
                emoji = "🔴"
            elif "ÉLEVÉ" in level:
                emoji = "🟠"
            else:
                emoji = "🟡"
            report += f"{emoji} **{threat}**: {level}\n"

        report += "\n📊 **Recommandations**:\n"
        report += "• Effectuer des sauvegardes régulières\n"
        report += "• Sensibiliser les équipes au phishing\n"
        report += "• Mettre à jour les systèmes de sécurité\n"
        report += "• Surveiller les activités suspectes\n"

        return report

    def respond_to_query(self, query: str) -> str:
        """Répond aux questions sur la cybersécurité"""
        query_lower = query.lower()

        if "météo" in query_lower or "weather" in query_lower:
            return self.get_weather_report()

        for keyword, info in self.knowledge_base.items():
            if keyword in query_lower:
                return f"ℹ️ **{keyword.upper()}**\n\n{info}"

        if "france" in query_lower:
            return "🇫🇷 **Cybersécurité en France**\n\nLa France fait face à une augmentation significative des cyberattaques. L'ANSSI coordonne la réponse nationale aux incidents de sécurité. Les secteurs les plus touchés sont la santé, l'éducation et les collectivités territoriales."

        return "🤖 Je peux vous aider avec des informations sur la cybersécurité, les menaces actuelles en France, ou générer un rapport météo cybercriminalité. Posez-moi une question spécifique !"

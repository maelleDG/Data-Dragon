import os
from datetime import datetime, timezone
from dotenv import load_dotenv
import google.generativeai as genai

# Import ton module d'articles
from packages.cyber_weather_module import cyber_weather

# Charger la clé Gemini
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


def fetch_fresh_articles():
    """
    Récupère les articles de cybersécurité en France pour contextualiser le rapport.
    """
    try:
        articles = cyber_weather.get_daily_cyber_articles(
            query="cybersécurité France", max_articles=50
        )
        print(f"✅ {len(articles)} articles récupérés pour le contexte.")
        return articles
    except Exception as e:
        print(f"❌ Erreur récupération articles : {e}")
        return []


def generate_cyber_weather_report(articles):
    """
    Génère un rapport météo cybersécurité synthétique et structuré en français
    à partir des articles fournis, en utilisant Gemini.
    """
    try:
        if articles:
            context_articles = "\n\n".join(
                f"- {a.get('title', 'Titre non disponible')} ({a.get('source', 'Source inconnue')}): {a.get('summary', 'Résumé non disponible')}"
                for a in articles
            )
        else:
            context_articles = "Aucun article disponible pour aujourd'hui."

        # Créer un prompt complet qui inclut l'instruction système
        full_prompt = f"""Tu es un expert en cybersécurité spécialisé en France. Utilise les informations suivantes pour générer un rapport de météo cybersécurité du jour :

Articles récents :
---
{context_articles}
---

Structure le rapport en :
1. Tendances générales
2. Menaces majeures observées
3. Recommandations pratiques pour entreprises et collectivités
4. Vulnérabilités ou incidents notables

Le rapport doit être synthétique, professionnel, faire quelques lignes et écrit en français.

Veuillez générer le rapport de météo cybersécurité du jour en France."""

        # Utiliser gemini-pro au lieu de gemini-2.0-pro qui pourrait ne pas être disponible
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Utiliser seulement le prompt (recommandé pour compatibilité)
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.5,
                max_output_tokens=1200,
                top_p=0.95,
            ),
        )

        # Vérifier que la réponse contient du texte
        if response and hasattr(response, "text"):
            report = response.text.strip()
            return report
        else:
            return "❌ Le modèle n'a pas retourné de texte."

    except Exception as e:
        print(f"❌ Erreur génération rapport : {e}")
        return f"❌ Impossible de générer le rapport aujourd'hui. Erreur: {e}"


if __name__ == "__main__":
    articles = fetch_fresh_articles()
    report = generate_cyber_weather_report(articles)

    # Sauvegarder le rapport automatiquement
    # today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # with open(f"cyber_weather_report_{today_str}.md", "w", encoding="utf-8") as f:
    #     f.write(report)

    # print("✅ Rapport généré et sauvegardé.")

import streamlit as st
import plotly.express as px
import pandas as pd


def security_vulnerabilities():
    # Charger les données
    df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")
    dfg = (
        df.loc[df["Country"] == "USA"]
        .groupby("Security Vulnerability Type")
        .count()
        .reset_index()
    )
    dfg = dfg.sort_values("Country", ascending=False)  # Tri par fréquence

    # Couleurs pour vos 4 types
    colors = ["#EB9292", "#85CC85", "#A7B2D4", "#C9BBAA"]

    # Créer le graphique
    fig = px.bar(
        dfg,
        x="Security Vulnerability Type",
        y="Country",
        title="Vulnérabilités de sécurité aux USA",
        color="Security Vulnerability Type",
        color_discrete_sequence=colors,
    )

    # Style sombre
    fig.update_layout(
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        title=dict(font=dict(size=18, color="white"), x=0.5),
        xaxis=dict(
            title="Type de vulnérabilité",
            tickfont=dict(color="white"),
            gridcolor="gray",
        ),
        xaxis_title_font=dict(color="white"),
        yaxis=dict(title="Nombre", tickfont=dict(color="white"), gridcolor="gray"),
        yaxis_title_font=dict(color="white"),
        showlegend=False,
    )

    # Ajouter les valeurs sur les barres
    fig.update_traces(texttemplate="%{y}", textposition="outside")

    return fig


# Pour Streamlit
def display_chart():
    st.title("Vulnérabilités de sécurité aux USA")
    fig = security_vulnerabilities()
    st.plotly_chart(fig, use_container_width=True)

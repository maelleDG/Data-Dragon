import streamlit as st
import plotly.express as px
import pandas as pd


# Fonction privée pour créer la figure
def _create_attack_figure():
    df = pd.read_csv("Global_Cybersecurity_Threats_2015-2024.csv")

    dfg = (
        df.loc[df["Country"] == "USA"]
        .groupby(["Year", "Attack Type"])
        .size()
        .reset_index(name="Nombre d'attaques")
    )

    attack_colors = {
        "Malware": "#FF4444",
        "Phishing": "#FF8C00",
        "Ransomware": "#DC143C",
        "DDoS": "#4169E1",
        "SQL Injection": "#32CD32",
        "Man-in-the-Middle": "#9932CC",
        "Zero-Day Exploit": "#FF1493",
        "Insider Threat": "#FFD700",
        "Advanced Persistent Threat": "#00CED1",
        "Social Engineering": "#FF6347",
        "Credential Stuffing": "#8A2BE2",
        "Botnet": "#00FF7F",
        "Cryptojacking": "#FF69B4",
        "Data Breach": "#20B2AA",
        "IoT Attack": "#FFA500",
        "Supply Chain Attack": "#DA70D6",
        "DNS Hijacking": "#87CEEB",
        "Email Spoofing": "#F0E68C",
        "Web Application Attack": "#CD853F",
        "Network Intrusion": "#40E0D0",
    }

    unique_attacks = dfg["Attack Type"].unique()
    color_sequence = [attack_colors.get(a, "#808080") for a in unique_attacks]

    fig = px.line(
        dfg,
        x="Year",
        y="Nombre d'attaques",
        color="Attack Type",
        markers=True,
        color_discrete_sequence=color_sequence,
    )

    fig.update_layout(
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        title=dict(
            text="Cyberattacks in the U.S. (2015–2024)",
            font=dict(size=16, color="white"),
            x=0.5,
        ),
        xaxis=dict(
            title="Year",
            tickfont=dict(color="white"),
            gridcolor="gray",
            gridwidth=0.5,
        ),
        xaxis_title_font=dict(color="white", size=12),
        yaxis=dict(
            title="Number of Attacks",
            tickfont=dict(color="white"),
            gridcolor="gray",
            gridwidth=0.5,
        ),
        yaxis_title_font=dict(color="white", size=12),
        legend=dict(
            font=dict(color="white"),
            title=dict(text="Attack Type", font=dict(color="white")),
        ),
        width=900,
        height=500,
    )

    fig.update_traces(line=dict(width=3), marker=dict(size=6))

    return fig


# Fonction publique à appeler dans Streamlit
def display_attacks_chart():
    st.header("🧨 Evolution of Cyberattack Types in the U.S.")
    st.markdown(
        "This chart shows the evolution of various cyberattack types in the United States between 2015 and 2024. "
        "It highlights the growing threat landscape and helps identify which vectors are increasing most rapidly."
    )
    fig = _create_attack_figure()
    st.plotly_chart(fig, use_container_width=True)

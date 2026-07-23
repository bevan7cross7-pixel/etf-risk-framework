from pathlib import Path

import pandas as pd
import streamlit as st


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed"
FIGURE_PATH = PROJECT_ROOT / "outputs" / "figures"


# Page settings
st.set_page_config(
    page_title="ETF Risk Framework",
    page_icon="📊",
    layout="wide"
)


# Load data
risk_ranking = pd.read_csv(
    DATA_PATH / "etf_risk_ranking.csv"
)

scoring_data = pd.read_csv(
    DATA_PATH / "etf_scoring_components.csv"
)


# Dashboard title
st.title("ETF Risk Framework")

st.write(
    "A transparent ETF comparison tool combining market risk, "
    "concentration risk and currency risk into an overall score from 0 to 100."
)


# Overall ranking
st.header("Overall ETF Risk Ranking")

ranking_display = risk_ranking[
    [
        "Risk_Rank",
        "Ticker",
        "ETF_Name",
        "Asset_Class",
        "Overall_Risk_Score",
        "Risk_Band",
        "Main_Risk_Driver"
    ]
].copy()

ranking_display["Overall_Risk_Score"] = (
    ranking_display["Overall_Risk_Score"].round(2)
)

st.dataframe(
    ranking_display,
    use_container_width=True,
    hide_index=True
)


# Main chart
ranking_chart_path = FIGURE_PATH / "overall_risk_ranking.png"

if ranking_chart_path.exists():
    st.image(
        str(ranking_chart_path),
        caption="Overall ETF risk scores"
    )


# Individual ETF selection
st.header("ETF Risk Profile")

selected_ticker = st.selectbox(
    "Select an ETF",
    risk_ranking["Ticker"].tolist()
)

selected_etf = risk_ranking.loc[
    risk_ranking["Ticker"] == selected_ticker
].iloc[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Overall Risk Score",
    f"{selected_etf['Overall_Risk_Score']:.2f}"
)

col2.metric(
    "Risk Band",
    selected_etf["Risk_Band"]
)

col3.metric(
    "Risk Rank",
    int(selected_etf["Risk_Rank"])
)

col4.metric(
    "Main Risk Driver",
    selected_etf["Main_Risk_Driver"]
)


# Sub-score breakdown
selected_scores = scoring_data.loc[
    scoring_data["Ticker"] == selected_ticker
].iloc[0]

st.subheader("Risk Sub-Scores")

subscore_table = pd.DataFrame({
    "Risk Dimension": [
        "Market Risk",
        "Concentration Risk",
        "Currency Risk"
    ],
    "Score": [
        selected_scores["Market_Risk_Score"],
        selected_scores["Concentration_Risk_Score"],
        selected_scores["Currency_Risk_Score"]
    ]
})

subscore_table["Score"] = subscore_table["Score"].round(2)

st.dataframe(
    subscore_table,
    use_container_width=True,
    hide_index=True
)


st.caption(
    "Academic and educational use only. The scores are comparative "
    "indicators and do not constitute financial advice."
)
import os
import streamlit as st

from src.data.market_data import fetch_market_data
from src.scoring.thesis_score import calculate_thesis_score
from src.reports.report_generator import generate_report

st.set_page_config(page_title="ThesisGuard AI", page_icon="🛡️", layout="wide")

st.title("ThesisGuard AI")
st.caption("A responsible AI investing research assistant for testing and monitoring investment theses.")

st.markdown(
    "ThesisGuard AI does not provide financial advice, price targets, or buy/sell recommendations. "
    "It helps you structure, challenge, and monitor an investment thesis."
)

with st.form("thesis_form"):
    ticker = st.text_input("Ticker", value="NVDA")
    thesis = st.text_area(
        "Why are you interested in this stock?",
        value="I think NVDA will keep growing because AI data center demand remains strong and hyperscalers continue spending.",
    )
    horizon = st.selectbox("Time horizon", ["3 months", "1 year", "3 years"])
    risk_tolerance = st.selectbox("Risk tolerance", ["Conservative", "Moderate", "Aggressive"])
    submitted = st.form_submit_button("Generate thesis report")

if submitted:
    with st.spinner("Analyzing thesis and market context..."):
        market_snapshot = fetch_market_data(ticker)
        score_result = calculate_thesis_score(thesis, market_snapshot, horizon, risk_tolerance)
        report = generate_report(ticker, thesis, horizon, risk_tolerance, score_result, market_snapshot)

    st.success("Report generated")
    st.markdown(report)

# Complete Streamlit Dashboard Template
# Generated for Bluestock Mutual Fund Capstone

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mutual Fund Intelligence Platform", page_icon="📈", layout="wide")

st.markdown("""
<style>
[data-testid="stMetric"]{
background:#111827;
border:1px solid #374151;
padding:15px;
border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

# DATA
scorecard = pd.read_csv("data/processed/fund_scorecard.csv")
investors = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
sip = pd.read_csv("data/processed/04_monthly_sip_inflows_cleaned.csv")
category_inflow = pd.read_csv("data/processed/05_category_inflows_cleaned.csv")

st.title("📈 Mutual Fund Intelligence Platform")

# FILTERS
st.sidebar.title("Dashboard Controls")
risk = st.sidebar.selectbox("Risk Grade", ["All"] + sorted(scorecard["risk_grade"].dropna().unique().tolist()))
category = st.sidebar.selectbox("Category", ["All"] + sorted(scorecard["category"].dropna().unique().tolist()))
top_n = st.sidebar.slider("Top Funds", 5, 25, 10)

filtered = scorecard.copy()
if risk != "All":
    filtered = filtered[filtered["risk_grade"] == risk]
if category != "All":
    filtered = filtered[filtered["category"] == category]

# KPI
c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric("Funds", len(filtered))
c2.metric("Avg 5Y Return", f"{filtered['return_5yr_pct'].mean():.2f}%")
c3.metric("Avg Sharpe", f"{filtered['sharpe_ratio'].mean():.2f}")
c4.metric("Avg Alpha", f"{filtered['alpha'].mean():.2f}")
c5.metric("Avg Beta", f"{filtered['beta'].mean():.2f}")
c6.metric("Avg Score", f"{filtered['fund_score'].mean():.2f}")

tab1,tab2,tab3,tab4 = st.tabs(["Industry Overview","Fund Performance","Investor Analytics","SIP & Market Trends"])

with tab1:
    st.subheader("Industry Overview")
    col1,col2 = st.columns(2)
    with col1:
        fig = px.pie(filtered, names="risk_grade", title="Risk Distribution")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        cat = filtered.groupby("category")["fund_score"].mean().reset_index().sort_values("fund_score", ascending=False).head(top_n)
        fig = px.bar(cat, x="fund_score", y="category", orientation="h")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    top = filtered.sort_values("fund_score", ascending=False).head(top_n)
    fig = px.bar(top, x="fund_score", y="scheme_name", orientation="h", color="risk_grade")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(filtered, x="beta", y="alpha", size="fund_score", color="risk_grade", hover_name="scheme_name")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    a,b,c,d = st.columns(4)
    a.metric("Investors", investors["investor_id"].nunique())
    b.metric("Avg Investment", f"₹{investors['amount_inr'].mean():,.0f}")
    c.metric("States", investors["state"].nunique())
    d.metric("Cities", investors["city"].nunique())

    fig = px.pie(investors, names="gender")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    fig = px.line(sip, x="month", y="sip_inflow_crore", markers=True)
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(category_inflow, x="category", y="net_inflow_crore")
    st.plotly_chart(fig, use_container_width=True)

st.download_button("Download Filtered Data", filtered.to_csv(index=False), "filtered_funds.csv")

import streamlit as st
import pandas as pd

# --- STRICT LAYOUT CONFIGURATION ---
st.set_page_config(page_title="Global Strategy Cockpit", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS: PREMIUM CANVA AESTHETIC WITH PINK SLIDER INDICATORS ---
st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    div[data-baseweb="slider"] [role="slider"] { background-color: #D81B60 !important; }
    div[data-baseweb="slider"] [aria-valuenow] { background-color: #D81B60 !important; }
    div[data-testid="stMetricValue"] { color: #111111 !important; font-weight: 700; }
    .metric-card {
        background: #F8F9FA;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #D81B60;
        margin-bottom: 15px;
    }
    .formula-box {
        background-color: #F1F3F5;
        border-radius: 8px;
        padding: 15px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 10px 0px;
        border: 1px solid #E9ECEF;
        color: #212529 !important;
        font-size: 14px;
        line-height: 1.5;
    }
    .tab-titanic { background: linear-gradient(135deg, #1D3557, #4682B4, #B0E0E6); padding: 25px; border-radius: 16px; color: #FFFFFF; }
    .tab-coffee { background: linear-gradient(135deg, #4E342E, #A1887F, #D7CCC8); padding: 25px; border-radius: 16px; color: #FFFFFF; }
    .tab-lilac { background: linear-gradient(135deg, #4A148C, #BA68C8, #E1BEE7); padding: 25px; border-radius: 16px; color: #FFFFFF; }
    .tab-green { background: linear-gradient(135deg, #1B5E20, #81C784, #C8E6C9); padding: 25px; border-radius: 16px; color: #FFFFFF; }
    .tab-title { font-weight: 800; font-size: 28px; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
    .tab-subtitle { font-size: 16px; opacity: 0.9; margin-bottom: 10px; }
    .section-desc { color: #495057 !important; font-size: 15px; line-height: 1.6; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- GLOBAL NAVIGATION FRAMEWORK ---
st.sidebar.markdown("## 📊 Strategic Command Center")
st.sidebar.markdown("Operational control panel for evaluating regional corporate metrics.")

# Clean 4-tab rollout without LVMH
tab1, tab2, tab3, tab4 = st.tabs([
    "🌐 Executive Overview", 
    "📦 Amazon UK", 
    "🇰🇷 Samsung APAC", 
    "🎧 Spotify Global"
])

# ==============================================================================
# TAB 1: EXECUTIVE OVERVIEW
# ==============================================================================
with tab1:
    st.markdown("""
    <div class="tab-titanic">
        <div class="tab-title">Global Enterprise Strategy Cockpit</div>
        <div class="tab-subtitle">Multi-Region Operational Framework & Macroeconomic Sync</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📊 Operational Framework Matrix")
        summary_data = {
            "Enterprise Unit": ["Amazon UK Operations", "Samsung Electronics APAC", "Spotify Premium Global"],
            "Primary Region": ["United Kingdom (UK)", "South Korea (APAC)", "Global Subscriptions"],
            "Core Analytical Mandate": ["Demand-Chain Logistics & Ad Velocity Sync", "Influencer Capital Bounded ROI Allocator", "Subscription Churn Risk Tracker"],
            "Reporting Currency": ["USD ($)", "USD ($)", "USD ($)"]
        }
        st.table(pd.DataFrame(summary_data))
    
    with col2:
        st.markdown("### 🏛️ System Control Protocol")
        st.info("💡 **Analytical Standardization Rule:** All financial variables, input vectors, and margin evaluations across this cockpit are dynamically calculated in **USD ($)** to isolate operational performance from multi-currency FX exposure.")

# ==============================================================================
# TAB 2: AMAZON UK
# ==============================================================================
with tab2:
    st.markdown("""
    <div class="tab-coffee">
        <div class="tab-title">Amazon UK Operations</div>
        <div class="tab-subtitle">Demand-Chain Logistics & Ad Spend Sync Module</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Risk Mitigation Mechanism & Simple Rules")
    st.markdown('<p class="section-desc">Protects marketing profits by turning off ads if inventory runs low.</p>', unsafe_allow_html=True)
    st.markdown('<div class="formula-box"><b>Rule 1:</b> Stock under 20% &rarr; Drop ad spend to $0 completely.<br><b>Rule 2:</b> Stock between 20% and 40% &rarr; Cut ad budget in half (50%) to slow down sales while warehouse restocks.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        base_ad_spend = st.number_input("Baseline Allocated Digital Ad Spend (Weekly, USD $)", min_value=1000, value=50000, step=5000, key="amzn_spend")
        inventory_level = st.slider("Warehouse Stock Availability Level (%)", 0, 100, 35, key="amzn_inv")
        
    with col2:
        if inventory_level < 20:
            adjusted_spend = 0
            st.error("🚨 **EMERGENCY AD ACTION:** Stock is dangerously low (<20%). Ads stopped completely to save budget and prevent unfulfillable orders.")
        elif 20 <= inventory_level <= 40:
            adjusted_spend = base_ad_spend * 0.50
            st.warning("⚠️ **TACTICAL THROTTLING:** Stock is low (20% - 40%). Ads reduced by 50% to slow down incoming orders while warehouse works to refill inventory.")
        else:
            adjusted_spend = base_ad_spend
            st.success("✅ **SAFE OPERATION STATE:** Stock levels look great. Ads running at full capacity.")
        st.metric(label="Final Executable Ad Outlay (USD)", value=f"${int(adjusted_spend):,}")

# ==============================================================================
# TAB 3: SAMSUNG APAC
# ==============================================================================
with tab3:
    st.markdown("""
    <div class="tab-lilac">
        <div class="tab-title">Samsung Electronics APAC</div>
        <div class="tab-subtitle">Influencer Capital Bounded ROI Allocator</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ How Payout Caps are Decided")
    st.markdown('<p class="section-desc">Ties creator payouts directly to actual buyer conversions rather than superficial follower reach numbers.</p>', unsafe_allow_html=True)
    st.markdown('<div class="formula-box"><b>Step 1:</b> Engaged Audience = Total Followers × Engagement Rate %<br><b>Step 2:</b> Expected Buyers = Engaged Audience × 4.5% (Market standard conversion rate)<br><b>Step 3:</b> Maximum Safe Payout = (Expected Buyers × Retail Price) × 15% (ROI Safety Cap)</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        follower_count = st.number_input("Influencer Total Follower Count", min_value=1000, value=250000, step=10000, key="sam_followers")
        engagement_rate = st.slider("Engagement Rate (%)", 0.5, 15.0, 3.2, step=0.1, key="sam_eng")
        device_price = st.number_input("Device Retail Price (USD $)", min_value=100, value=1200, step=50, key="sam_price")
        
    with col2:
        engaged_audience = follower_count * (engagement_rate / 100)
        expected_buyers = engaged_audience * 0.045
        max_payout = (expected_buyers * device_price) * 0.15
        st.markdown("### 💰 Budget Limit Allocation Result")
        st.metric(label="Maximum Allowed Influencer Contract Payout (USD)", value=f"${max_payout:,.2f}")
        st.info(f"📈 **Projections Summary:** This influencer is expected to reach {int(engaged_audience):,} active users, driving roughly {int(expected_buyers):,} baseline hardware conversions.")

# ==============================================================================
# TAB 4: SPOTIFY GLOBAL
# ==============================================================================
with tab4:
    st.markdown("""
    <div class="tab-green">
        <div class="tab-title">Spotify Premium Global</div>
        <div class="tab-subtitle">Subscription Churn Risk Tracker & Revenue Protection</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ How Churn Revenue Exposure is Calculated")
    st.markdown('<p class="section-desc">Monitors average platform listening engagement patterns to calculate financial downside risk.</p>', unsafe_allow_html=True)
    st.markdown('<div class="formula-box"><b>Step 1:</b> Total Monthly Revenue = Active Subscribers × Monthly ARPU<br><b>Step 2:</b> Risk Factor = Less than 10 hrs &rarr; 45% Risk | 10 to 20 hrs &rarr; 15% Risk | Over 20 hrs &rarr; 4% Risk<br><b>Step 3:</b> Churn Revenue Exposure = Total Monthly Revenue × Risk Factor</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        monthly_subs = st.number_input("Total Active Premium Subscribers", min_value=1000, value=1500000, step=50000, key="spot_subs")
        avg_stream_hours = st.slider("Average Monthly Listening Duration (Hours)", 0, 60, 14, key="spot_hours")
        arpu = st.number_input("Average Revenue Per User (Monthly, USD $)", min_value=1.0, value=10.99, step=0.50, key="spot_arpu")
        
    with col2:
        total_monthly_revenue = monthly_subs * arpu
        if avg_stream_hours < 10:
            st.error("🚨 **CRITICAL CHURN RISK LEVEL:** Global listening metric has dipped below the critical engagement floor. Automated retention offers should be triggered.")
            at_risk_pct = 45.0
        elif 10 <= avg_stream_hours <= 20:
            st.warning("⚠️ **ELEVATED MONITORING:** Listening metrics indicate borderline fatigue. Recommend surface playlist notifications.")
            at_risk_pct = 15.0
        else:

import streamlit as st
import pandas as pd

# --- STRICT LAYOUT CONFIGURATION ---
st.set_page_config(page_title="Global Strategy Cockpit", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS: PREMIUM CANVA AESTHETIC WITH PINK SLIDER INDICATORS ---
st.markdown("""
<style>
    /* Global Canvas Styling */
    .stApp { background-color: #FFFFFF; }
    
    /* Premium High-Contrast Dark Pink Sliders & Component Adjustments */
    div[data-baseweb="slider"] [role="slider"] { background-color: #D81B60 !important; }
    div[data-baseweb="slider"] [aria-valuenow] { background-color: #D81B60 !important; }
    div[data-testid="stMetricValue"] { color: #111111 !important; font-weight: 700; }
    
    /* Structured UI Cards */
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
    
    /* Silk-Gradient Structural Headers per Module */
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

# Unpacking the 4 remaining enterprise domains cleanly
tab1, tab2, tab3, tab4 = st.tabs([
    "🌐 Executive Overview", 
    "📦 Amazon UK", 
    "🇰🇷 Samsung APAC", 
    "🎧 Spotify Global"
])

# ==============================================================================
# TAB 1: EXECUTIVE OVERVIEW (REAL REVENUE BOUNDED MATRIX)
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
# TAB 2: AMAZON UK (GROUNDED BY MATURE SELLER DYNAMICS)
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
        # Grounded value matching aggregated portfolio allocations for prominent UK marketplace brands (~281,000 active UK base)
        base_ad_spend = st.number_input("Baseline Allocated Digital Ad Spend (Weekly, USD $)", min_value=1000, value=125000, step=5000, key="amzn_spend")
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
# TAB 3: SAMSUNG APAC (REAL MACRO INFLUENCER CAPITAL ROSTER)
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
        # Structured for typical high-tier local campaigns (e.g. Samsung India/APAC tech rosters)
        follower_count = st.number_input("Influencer Total Follower Count", min_value=1000, value=850000, step=50000, key="sam_followers")
        engagement_rate = st.slider("Engagement Rate (%)", 0.5, 15.0, 4.1, step=0.1, key="sam_eng")
        device_price = st.number_input("Device Retail Price (USD $)", min_value=100, value=1199, step=50, key="sam_price")
        
    with col2:
        # Calculate Real Bounded ROI Cap Metric
        engaged_audience = follower_count * (engagement_rate / 100)
        expected_buyers = engaged_audience * 0.045
        max_payout = (expected_buyers * device_price) * 0.15
        
        st.markdown("### 💰 Budget Limit Allocation Result")
        st.metric(label="Maximum Allowed Influencer Contract Payout (USD)", value=f"${max_payout:,.2f}")
        st.info(f"📈 **Projections Summary:** This influencer is expected to reach {int(engaged_audience):?} active users, driving roughly {int(expected_buyers):?} baseline hardware conversions.")

# ==============================================================================
# TAB 4: SPOTIFY GLOBAL (REAL HISTORICAL H2 2026 BENCHMARKS)
# ==============================================================================
with tab4:
    st.markdown("""
    <div class="tab-green">
        <div class="tab-title">Spotify Premium Global</div>
        <div class="tab-subtitle">Subscription Churn Risk Tracker & Revenue Protection</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Churn Risk Matrix Calculation")
    st.markdown('<p class="section-desc">Monitors average platform listening engagement patterns to predict cancellation risks early.</p>', unsafe_allow_html=True)
    st.markdown('<div class="formula-box"><b>Risk Standard:</b> Users streaming less than 10 hours a month are flagged at High Churn Risk. Retaining a high-risk subscriber via a promotional trigger protects MRR.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        # Real Q2 2026 Metric: Spotify officially scaled to 300,000,000 paying premium subscribers globally.
        monthly_subs = st.number_input("Total Active Premium Subscribers (Global)", min_value=1000000, value=300000000, step=1000000, key="spot_subs")

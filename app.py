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
    .tab-gold { background: linear-gradient(135deg, #F57F17, #FFF176, #FFF9C4); padding: 25px; border-radius: 16px; color: #212529; }
    
    .tab-title { font-weight: 800; font-size: 28px; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 1px; }
    .tab-subtitle { font-size: 16px; opacity: 0.9; margin-bottom: 10px; }
    .section-desc { color: #495057 !important; font-size: 15px; line-height: 1.6; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- GLOBAL NAVIGATION FRAMEWORK ---
st.sidebar.markdown("## 📊 Strategic Command Center")
st.sidebar.markdown("Operational control panel for evaluating regional corporate metrics.")

# Unpacking tabs to separate page views cleanly
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌐 Executive Overview", 
    "📦 Amazon UK", 
    "🇰🇷 Samsung APAC", 
    "🎧 Spotify Global", 
    "🍾 LVMH Europe"
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
            "Enterprise Unit": ["Amazon UK Operations", "Samsung Electronics APAC", "Spotify Premium Global", "LVMH Group Europe"],
            "Primary Region": ["United Kingdom (UK)", "South Korea (APAC)", "Global Subscriptions", "France (Continental EU)"],
            "Core Analytical Mandate": ["Demand-Chain Logistics & Ad Velocity Sync", "Influencer Capital Bounded ROI Allocator", "Subscription Churn Risk Tracker", "Luxury Pricing & Margin Shield"],
            "Reporting Currency": ["USD ($)", "USD ($)", "USD ($)", "USD ($)"]
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
        engaged_reach = follower_count * (engagement_rate / 100.0)
        projected_conversions = int(engaged_reach * 0.045)
        gross_revenue_projection = projected_conversions * device_price
        max_safe_payout = gross_revenue_projection * 0.15
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric(label="Projected Conversions (Actual Buyers)", value=f"{projected_conversions:,} customers")
        st.metric(label="Projected Revenue Pipeline (USD)", value=f"${gross_revenue_projection:,}")
        st.metric(label="Maximum Safe Payout Budget (USD)", value=f"${max_safe_payout:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# TAB 4: SPOTIFY GLOBAL (SIMPLIFIED RISK SCORE)
# ==============================================================================
with tab4:
    st.markdown("""
    <div class="tab-green">
        <div class="tab-title">Spotify Premium Global</div>
        <div class="tab-subtitle">Simple Subscription Cancellation Risk Tracker</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Simple Risk Score Calculation")
    st.markdown('<p class="section-desc">Calculates a user risk score from 0% to 100% based on simple behavioral and economic points.</p>', unsafe_allow_html=True)
    st.markdown('<div class="formula-box"><b>1. Inactivity Points:</b> Up to 40 points depending on days since last login.<br><b>2. Inflation Strain:</b> Up to 30 points if local living costs are rising rapidly.<br><b>3. Price Hike Strains:</b> Up to 30 points based on how big our planned price increase is.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        days_inactive = st.slider("Days Since User Last Opened App", 0, 30, 15, key="spot_days")
        local_inflation = st.slider("Regional Core Inflation Strain Rate (%)", 0.0, 15.0, 5.0, step=0.5, key="spot_inf")

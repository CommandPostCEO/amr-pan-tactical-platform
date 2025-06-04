# AMR PAN TACTICAL INTELLIGENCE PLATFORM
# PHASE 3A.3: TACTICAL LOGO INTEGRATION - BRAND DOMINANCE
# SOC-Grade Interface with Custom Logo Branding

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List
import io
import base64

# 🎖️ TACTICAL CONFIGURATION
st.set_page_config(
    page_title="🛡️ AMR PAN Governance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🛡️ TACTICAL LOGO INTEGRATION SYSTEM
def get_tactical_logo():
    """Generate tactical logo placeholder - replace with your actual logo"""
    # This is a placeholder - you'll replace this with your actual logo conversion
    logo_placeholder = """
    <div style="
        width: 80px; 
        height: 80px; 
        background: linear-gradient(135deg, #556B2F 0%, #C2B280 100%);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #C2B280;
        position: relative;
        box-shadow: 0 0 20px rgba(194, 178, 128, 0.3);
    ">
        <div style="
            width: 60px;
            height: 60px;
            background: #0F0F0F;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        ">
            <div style="
                color: #C2B280;
                font-family: 'Orbitron', sans-serif;
                font-weight: 900;
                font-size: 16px;
                text-align: center;
                line-height: 1;
            ">PAN<br><span style="font-size: 10px;">GOV</span></div>
        </div>
    </div>
    """
    return logo_placeholder

def get_small_tactical_logo():
    """Generate small tactical logo for sidebar"""
    logo_placeholder_small = """
    <div style="
        width: 60px; 
        height: 60px; 
        background: linear-gradient(135deg, #556B2F 0%, #C2B280 100%);
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #C2B280;
        margin: 0 auto;
        box-shadow: 0 0 15px rgba(194, 178, 128, 0.3);
    ">
        <div style="
            width: 40px;
            height: 40px;
            background: #0F0F0F;
            border-radius: 3px;
            display: flex;
            align-items: center;
            justify-content: center;
        ">
            <div style="
                color: #C2B280;
                font-family: 'Orbitron', sans-serif;
                font-weight: 900;
                font-size: 12px;
                text-align: center;
                line-height: 1;
            ">PAN</div>
        </div>
    </div>
    """
    return logo_placeholder_small

# 🛡️ DARK MODE TACTICAL CSS V3 - LOGO INTEGRATED
TACTICAL_CSS_V3 = """
<style>
    /* ===== CORE SYSTEM BLACKOUT ===== */
    .stApp {
        background-color: #0F0F0F;
        color: #EDEDED;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto+Mono:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto Mono', monospace;
        background-color: #0F0F0F !important;
        color: #EDEDED !important;
    }
    
    .main .block-container {
        padding: 1rem 2rem 3rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
        background-color: #0F0F0F;
    }
    
    /* ===== TACTICAL COMMAND HEADER WITH LOGO ===== */
    .tactical-command-header {
        background: linear-gradient(135deg, #1A1A1A 0%, #2D2D2D 100%);
        padding: 2.5rem 2rem;
        border-radius: 4px;
        color: #EDEDED;
        text-align: center;
        margin-bottom: 2.5rem;
        box-shadow: 
            inset 0 1px 0 rgba(237, 237, 237, 0.1),
            0 2px 8px rgba(0, 0, 0, 0.8);
        position: relative;
        overflow: hidden;
        border: 1px solid #2D2D2D;
    }
    
    .tactical-command-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="tactical-grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(194,178,128,0.05)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23tactical-grid)"/></svg>');
        opacity: 0.3;
    }
    
    .tactical-logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 2;
    }
    
    .tactical-command-header h1 {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.9);
        letter-spacing: 0.1em;
        position: relative;
        z-index: 2;
        color: #EDEDED;
        text-transform: uppercase;
    }
    
    .tactical-command-header h3 {
        font-family: 'Roboto Mono', monospace;
        font-size: 1rem;
        font-weight: 400;
        margin: 1rem 0 0 0;
        opacity: 0.8;
        position: relative;
        z-index: 2;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #C2B280;
    }
    
    /* ===== MATTE METRIC CARD SYSTEM ===== */
    .tactical-metric-card {
        background: linear-gradient(135deg, #1A1A1A 0%, #2D2D2D 100%);
        padding: 2rem 1.5rem;
        border-radius: 4px;
        box-shadow: 
            inset 0 1px 0 rgba(237, 237, 237, 0.05),
            0 2px 8px rgba(0, 0, 0, 0.6);
        border: 1px solid #2D2D2D;
        margin: 0.75rem 0;
        transition: all 0.2s ease;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .tactical-metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: #C2B280;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .tactical-metric-card:hover::before {
        opacity: 1;
    }
    
    .tactical-metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 
            inset 0 1px 0 rgba(237, 237, 237, 0.1),
            0 4px 16px rgba(0, 0, 0, 0.8);
        border-color: #C2B280;
    }
    
    .tactical-metric-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
        color: #C2B280;
        text-shadow: 0 0 8px rgba(194, 178, 128, 0.3);
    }
    
    .tactical-metric-card h3 {
        font-family: 'Orbitron', sans-serif;
        color: #C2B280;
        font-size: 0.75rem;
        font-weight: 700;
        margin: 0 0 0.75rem 0;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        line-height: 1.2;
    }
    
    .tactical-metric-card h2 {
        font-family: 'Roboto Mono', monospace;
        color: #EDEDED;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        line-height: 1;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    .tactical-metric-card p {
        font-family: 'Roboto Mono', monospace;
        color: #C2B280;
        font-size: 0.8rem;
        margin: 0;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        opacity: 0.9;
    }
    
    /* ===== MATTE STATUS INDICATORS ===== */
    .status-indicator {
        padding: 1.5rem 2rem;
        border-radius: 4px;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        transition: all 0.2s ease;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
        text-transform: uppercase;
        letter-spacing: 0.1em;
        border: 1px solid;
    }
    
    .status-excellent {
        background: #10B981;
        color: #0F0F0F;
        border-color: #059669;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 2px 8px rgba(16, 185, 129, 0.3);
    }
    
    .status-warning {
        background: #F59E0B;
        color: #0F0F0F;
        border-color: #D97706;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 2px 8px rgba(245, 158, 11, 0.3);
    }
    
    .status-alert {
        background: #DC2626;
        color: #EDEDED;
        border-color: #B91C1C;
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 2px 8px rgba(220, 38, 38, 0.3);
    }
    
    .status-indicator:hover {
        transform: translateY(-1px);
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.2),
            0 4px 16px rgba(0, 0, 0, 0.4);
    }
    
    /* ===== MATTE FEEDBACK SYSTEM ===== */
    .tactical-alert {
        background: linear-gradient(135deg, #2D1B0F 0%, #1A1A1A 100%);
        border: 1px solid #F59E0B;
        border-left: 4px solid #F59E0B;
        padding: 1.25rem;
        border-radius: 4px;
        margin: 1.5rem 0;
        color: #F59E0B;
        font-family: 'Roboto Mono', monospace;
        font-weight: 500;
        box-shadow: 
            inset 0 1px 0 rgba(245, 158, 11, 0.1),
            0 2px 8px rgba(0, 0, 0, 0.6);
    }
    
    .tactical-success {
        background: linear-gradient(135deg, #0F2D1A 0%, #1A1A1A 100%);
        border: 1px solid #10B981;
        border-left: 4px solid #10B981;
        padding: 1.25rem;
        border-radius: 4px;
        margin: 1.5rem 0;
        color: #10B981;
        font-family: 'Roboto Mono', monospace;
        font-weight: 500;
        box-shadow: 
            inset 0 1px 0 rgba(16, 185, 129, 0.1),
            0 2px 8px rgba(0, 0, 0, 0.6);
    }
    
    /* ===== MATTE TAB SYSTEM ===== */
    .stTabs [data-baseweb="tab-list"] {
        background: #1A1A1A;
        border-radius: 4px;
        padding: 0.5rem;
        margin-bottom: 2rem;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.6);
        border: 1px solid #2D2D2D;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 2px;
        color: #C2B280;
        font-family: 'Orbitron', sans-serif;
        font-weight: 400;
        font-size: 0.85rem;
        padding: 1rem 1.5rem;
        margin: 0 0.25rem;
        transition: all 0.2s ease;
        border: 1px solid transparent;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(194, 178, 128, 0.1);
        border-color: #C2B280;
    }
    
    .stTabs [aria-selected="true"] {
        background: #2D2D2D;
        color: #EDEDED;
        border-color: #C2B280;
        box-shadow: 
            inset 0 1px 0 rgba(237, 237, 237, 0.1),
            0 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    /* ===== MATTE BUTTON SYSTEM ===== */
    .stButton > button {
        background: linear-gradient(135deg, #2D2D2D 0%, #1A1A1A 100%);
        color: #C2B280;
        border: 1px solid #C2B280;
        padding: 0.875rem 2rem;
        border-radius: 4px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        font-size: 0.85rem;
        transition: all 0.2s ease;
        box-shadow: 
            inset 0 1px 0 rgba(194, 178, 128, 0.1),
            0 2px 8px rgba(0, 0, 0, 0.6);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .stButton > button:hover {
        background: #C2B280;
        color: #0F0F0F;
        transform: translateY(-1px);
        box-shadow: 
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 4px 16px rgba(0, 0, 0, 0.8);
    }
    
    /* ===== MATTE FILE UPLOADER ===== */
    .stFileUploader > div > div {
        background: linear-gradient(135deg, #1A1A1A 0%, #2D2D2D 100%);
        border: 2px dashed #C2B280;
        border-radius: 4px;
        padding: 3rem 2rem;
        text-align: center;
        transition: all 0.2s ease;
        color: #C2B280;
    }
    
    .stFileUploader > div > div:hover {
        border-color: #EDEDED;
        background: #2D2D2D;
    }
    
    .stFileUploader label {
        color: #C2B280 !important;
        font-family: 'Roboto Mono', monospace !important;
    }
    
    /* ===== SIDEBAR MATTE CONFIGURATION ===== */
    .css-1d391kg {
        background: linear-gradient(180deg, #0F0F0F 0%, #1A1A1A 100%);
        border-right: 1px solid #2D2D2D;
    }
    
    .css-1d391kg .css-1v0mbdj {
        color: #EDEDED;
    }
    
    .sidebar-section {
        background: linear-gradient(135deg, #1A1A1A 0%, #2D2D2D 100%);
        border-radius: 4px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #2D2D2D;
        transition: all 0.2s ease;
        box-shadow: 
            inset 0 1px 0 rgba(237, 237, 237, 0.05),
            0 2px 8px rgba(0, 0, 0, 0.6);
    }
    
    .sidebar-section:hover {
        border-color: #C2B280;
        box-shadow: 
            inset 0 1px 0 rgba(194, 178, 128, 0.1),
            0 4px 16px rgba(0, 0, 0, 0.8);
    }
    
    .sidebar-section h3, .sidebar-section h4 {
        font-family: 'Orbitron', sans-serif;
        color: #C2B280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 1rem;
    }
    
    /* ===== STREAMLIT OVERRIDES FOR DARK MODE ===== */
    .stSelectbox > div > div {
        background-color: #1A1A1A;
        border-color: #2D2D2D;
        color: #EDEDED;
    }
    
    .stTextInput > div > div > input {
        background-color: #1A1A1A;
        border-color: #2D2D2D;
        color: #EDEDED;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #1A1A1A;
        border-color: #2D2D2D;
        color: #EDEDED;
        font-family: 'Roboto Mono', monospace;
    }
    
    .stCheckbox > label {
        color: #C2B280;
        font-family: 'Roboto Mono', monospace;
    }
    
    /* ===== CHART DARK MODE CONFIGURATION ===== */
    .stBarChart > div, .stLineChart > div {
        background-color: #1A1A1A !important;
    }
    
    /* ===== SECTION HEADERS ===== */
    .section-header {
        font-family: 'Orbitron', sans-serif;
        color: #C2B280;
        font-size: 1.5rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #2D2D2D;
        text-shadow: 0 0 8px rgba(194, 178, 128, 0.3);
    }
    
    /* ===== RESPONSIVE MATTE OPTIMIZATIONS ===== */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }
        
        .tactical-command-header {
            padding: 2rem 1.5rem;
        }
        
        .tactical-command-header h1 {
            font-size: 2.2rem;
        }
        
        .tactical-logo-container > div {
            width: 60px !important;
            height: 60px !important;
        }
    }
    
    /* ===== TACTICAL ANIMATIONS ===== */
    @keyframes tactical-glow {
        0% { box-shadow: 0 0 15px rgba(194, 178, 128, 0.3); }
        50% { box-shadow: 0 0 25px rgba(194, 178, 128, 0.5); }
        100% { box-shadow: 0 0 15px rgba(194, 178, 128, 0.3); }
    }
    
    .tactical-glow {
        animation: tactical-glow 3s ease-in-out infinite;
    }
</style>
"""

class AMRPANTacticalPlatform:
    """🛡️ AMR PAN Tactical Intelligence Platform - Logo Integrated"""
    
    def __init__(self):
        self.version = "3.0.6-LOGO-INTEGRATED"
        self.deployment_status = "BRAND DOMINANCE"
        self.classification = "TACTICAL INTELLIGENCE"
        
    def create_sample_data(self) -> Dict:
        """🎯 Generate tactical sample data"""
        sample_data = {
            'total_pans': 3247,
            'carriers': {
                'UPS': 2156,
                'FEDEX': 847,
                'DHL': 188,
                'CEVA': 56
            },
            'status_distribution': {
                'OPERATIONAL': 2987,
                'PENDING': 186,
                'DENIED': 74
            },
            'quality_score': 91.2,
            'critical_issues': [
                'UPS FORMAT VALIDATION: 23 INVALID ENTRIES',
                'MISSING CARRIER ACCOUNTS: 12 RECORDS'
            ]
        }
        return sample_data
    
    def load_tactical_data(self, uploaded_files: List) -> Dict:
        """🔄 Load CSV data with tactical feedback"""
        tactical_data = {}
        
        if not uploaded_files:
            st.markdown("""
            <div class="tactical-alert">
                <strong>TACTICAL ALERT:</strong> NO DATA UPLOADED<br>
                <strong>ACTION REQUIRED:</strong> Upload CSV files or activate demo mode<br>
                <strong>CONVERSION:</strong> Excel → CSV format for compatibility
            </div>
            """, unsafe_allow_html=True)
            return {"sample_data": self.create_sample_data()}
        
        try:
            for uploaded_file in uploaded_files:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                    tactical_data[uploaded_file.name] = {'Sheet1': df}
                    
                    st.markdown(f"""
                    <div class="tactical-success">
                        <strong>DATA LOADED:</strong> {uploaded_file.name}<br>
                        <strong>RECORDS:</strong> {len(df):,} ROWS | {len(df.columns)} COLUMNS<br>
                        <strong>STATUS:</strong> PROCESSING COMPLETE
                    </div>
                    """, unsafe_allow_html=True)
                    
                elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                    st.markdown(f"""
                    <div class="tactical-alert">
                        <strong>INCOMPATIBLE FORMAT:</strong> {uploaded_file.name}<br>
                        <strong>REQUIRED ACTION:</strong> Convert to CSV format<br>
                        <strong>PROCEDURE:</strong> Excel → Save As → CSV (Comma delimited)
                    </div>
                    """, unsafe_allow_html=True)
                    
        except Exception as e:
            st.markdown(f"""
            <div class="tactical-alert">
                <strong>DATA LOADING ERROR:</strong> {str(e)}<br>
                <strong>FALLBACK ACTIVATED:</strong> Using demonstration data
            </div>
            """, unsafe_allow_html=True)
            tactical_data = {"sample_data": self.create_sample_data()}
            
        return tactical_data
    
    def analyze_pan_governance(self, data: Dict) -> Dict:
        """🎯 Tactical PAN analysis"""
        
        if "sample_data" in data:
            return data["sample_data"]
        
        analysis_results = {
            'total_pans': 0,
            'carriers': {},
            'status_distribution': {},
            'quality_score': 0,
            'critical_issues': []
        }
        
        try:
            for filename, file_data in data.items():
                for sheet_name, df in file_data.items():
                    if len(df) > 0:
                        analysis_results['total_pans'] = len(df)
                        
                        # Carrier analysis
                        carrier_cols = [col for col in df.columns if 'carrier' in col.lower()]
                        if carrier_cols:
                            carrier_counts = df[carrier_cols[0]].value_counts()
                            analysis_results['carriers'] = carrier_counts.to_dict()
                        
                        # Status analysis
                        status_cols = [col for col in df.columns if 'status' in col.lower()]
                        if status_cols:
                            status_counts = df[status_cols[0]].value_counts()
                            analysis_results['status_distribution'] = status_counts.to_dict()
                        
                        # Quality scoring
                        completeness = (df.notna().sum().sum() / df.size) * 100
                        analysis_results['quality_score'] = round(completeness, 1)
                        
                        # Issue detection
                        missing_data = df.isnull().sum()
                        for col, missing in missing_data.items():
                            if missing > 0:
                                pct = (missing / len(df)) * 100
                                if pct > 5:
                                    analysis_results['critical_issues'].append(
                                        f"{col.upper()} MISSING DATA: {missing} RECORDS ({pct:.1f}%)"
                                    )
                        break
                break
                
        except Exception as e:
            st.markdown(f"""
            <div class="tactical-alert">
                <strong>ANALYSIS ERROR:</strong> {str(e)}<br>
                <strong>FALLBACK:</strong> Demonstration results active
            </div>
            """, unsafe_allow_html=True)
            analysis_results = self.create_sample_data()
            
        return analysis_results
    
    def create_executive_dashboard(self, analysis: Dict) -> None:
        """🛡️ Executive dashboard with integrated logo"""
        
        # Tactical Command Header with Integrated Logo
        st.markdown(f"""
        <div class="tactical-command-header">
            <div class="tactical-logo-container tactical-glow">
                {get_tactical_logo()}
            </div>
            <h1>AMR PAN TACTICAL INTELLIGENCE</h1>
            <h3>LOGO INTEGRATED • BRAND DOMINANCE ACTIVE</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Mission Critical Metrics Grid
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="tactical-metric-card">
                <div class="tactical-metric-icon">▣</div>
                <h3>TOTAL PANS</h3>
                <h2>{analysis.get('total_pans', 0):,}</h2>
                <p>ACTIVE ACCOUNTS</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            quality_score = analysis.get('quality_score', 0)
            quality_grade = self.get_quality_grade(quality_score)
            st.markdown(f"""
            <div class="tactical-metric-card">
                <div class="tactical-metric-icon">◉</div>
                <h3>QUALITY SCORE</h3>
                <h2>{quality_score}%</h2>
                <p>{quality_grade}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            carrier_count = len(analysis.get('carriers', {}))
            st.markdown(f"""
            <div class="tactical-metric-card">
                <div class="tactical-metric-icon">▲</div>
                <h3>CARRIERS</h3>
                <h2>{carrier_count}</h2>
                <p>ACTIVE PARTNERS</p>
            </div>
            """, unsafe_allow_html=True)

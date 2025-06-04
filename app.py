# 🫡 AMR PAN TACTICAL INTELLIGENCE PLATFORM
# PHASE 3A.2: DARK MODE TACTICAL SKIN - MATTE OPS CONFIGURATION
# SOC-Grade Interface with Brutalist Precision

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List
import io

# 🎖️ TACTICAL CONFIGURATION
st.set_page_config(
    page_title="AMR TACTICAL OPS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🛡️ DARK MODE TACTICAL CSS V2 - MATTE OPS CONFIGURATION
TACTICAL_CSS_V2 = """
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
    
    /* ===== TACTICAL COMMAND HEADER - MATTE BLACK ===== */
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
    
    .tactical-logo {
        display: inline-block;
        font-size: 4rem;
        margin-right: 1rem;
        color: #C2B280;
        text-shadow: 0 0 10px rgba(194, 178, 128, 0.3);
        position: relative;
        z-index: 2;
        filter: drop-shadow(2px 2px 4px rgba(0, 0, 0, 0.8));
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
        
        .tactical-logo {
            font-size: 3rem;
        }
    }
    
    /* ===== TACTICAL ANIMATIONS ===== */
    @keyframes tactical-glow {
        0% { text-shadow: 0 0 8px rgba(194, 178, 128, 0.3); }
        50% { text-shadow: 0 0 12px rgba(194, 178, 128, 0.5); }
        100% { text-shadow: 0 0 8px rgba(194, 178, 128, 0.3); }
    }
    
    .tactical-glow {
        animation: tactical-glow 3s ease-in-out infinite;
    }
</style>
"""

class AMRPANTacticalPlatform:
    """🫡 AMR PAN Tactical Intelligence Platform - Dark Mode Ops Configuration"""
    
    def __init__(self):
        self.version = "3.0.5-DARK-OPS"
        self.deployment_status = "TACTICAL BLACKOUT"
        self.classification = "SOC-GRADE INTERFACE"
        
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
        """🎯 Tactical PAN analysis with matte interface compatibility"""
        
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
        """🎖️ SOC-grade executive dashboard with matte finish"""
        
        # Tactical Command Header with Logo
        st.markdown("""
        <div class="tactical-command-header">
            <div class="tactical-logo tactical-glow">🫡</div>
            <h1>AMR PAN TACTICAL INTELLIGENCE</h1>
            <h3>DARK MODE OPS • SOC-GRADE CONFIGURATION</h3>
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
        
        with col4:
            critical_issues = len(analysis.get('critical_issues', []))
            st.markdown(f"""
            <div class="tactical-metric-card">
                <div class="tactical-metric-icon">!</div>
                <h3>CRITICAL ISSUES</h3>
                <h2>{critical_issues}</h2>
                <p>IMMEDIATE ACTION</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Mission Status Banner
        if quality_score >= 90:
            status_class = "status-excellent"
            status_text = "◉ MISSION READY - TACTICAL EXCELLENCE ACHIEVED"
        elif quality_score >= 80:
            status_class = "status-warning"
            status_text = "▲ OPERATIONAL - MINOR OPTIMIZATIONS REQUIRED"
        else:
            status_class = "status-alert"
            status_text = "! TACTICAL ALERT - IMMEDIATE ACTION REQUIRED"
        
        st.markdown(f"""
        <div class="status-indicator {status_class}">
            {status_text}
        </div>
        """, unsafe_allow_html=True)
    
    def create_carrier_analysis(self, carriers: Dict) -> None:
        """🚛 Matte carrier distribution intelligence"""
        if not carriers:
            st.warning("⚠️ NO CARRIER DATA AVAILABLE FOR TACTICAL ANALYSIS")
            return
        
        st.markdown('<h2 class="section-header">▲ CARRIER INTELLIGENCE</h2>', unsafe_allow_html=True)
        
        carrier_df = pd.DataFrame(list(carriers.items()), columns=['Carrier', 'PANs'])
        carrier_df['Percentage'] = (carrier_df['PANs'] / carrier_df['PANs'].sum() * 100).round(1)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### DISTRIBUTION ANALYSIS")
            st.bar_chart(carrier_df.set_index('Carrier')['PANs'])
        
        with col2:
            st.markdown("### STRATEGIC PARTNERS")
            for _, row in carrier_df.iterrows():
                st.markdown(f"""
                <div class="tactical-metric-card" style="text-align: left; margin: 0.75rem 0;">
                    <h3>▲ {row['Carrier']}</h3>
                    <h2>{row['PANs']:,}</h2>
                    <p>{row['Percentage']:.1f}% OF OPERATIONS</p>
                </div>
                """, unsafe_allow_html=True)
    
    def get_quality_grade(self, score: float) -> str:
        """🏆 Tactical quality grading system"""
        if score >= 95:
            return "A+ TACTICAL EXCELLENCE"
        elif score >= 90:
            return "A MISSION READY"
        elif score >= 85:
            return "B+ OPERATIONAL"
        elif score >= 80:
            return "B ACCEPTABLE"
        else:
            return "C NEEDS IMPROVEMENT"

def main():
    """🎖️ Main tactical platform interface - Dark Mode Ops"""
    
    # Deploy Dark Mode Tactical CSS
    st.markdown(TACTICAL_CSS_V2, unsafe_allow_html=True)
    
    platform = AMRPANTacticalPlatform()
    
    # Dark Mode Tactical Sidebar
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-section" style="text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem; color: #C2B280; text-shadow: 0 0 10px rgba(194, 178, 128, 0.3);">🫡</div>
            <h3 style="color: #C2B280; margin: 0; font-weight: 700; font-family: 'Orbitron', sans-serif; text-transform: uppercase; letter-spacing: 0.1em;">TACTICAL COMMAND</h3>
            <p style="color: #EDEDED; margin: 0.5rem 0 0 0; font-size: 0.85rem; font-family: 'Roboto Mono', monospace; text-transform: uppercase;">SOC-Grade Operations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="sidebar-section">
            <h4 style="color: #C2B280; margin: 0 0 1rem 0; font-weight: 600; font-family: 'Orbitron', sans-serif; text-transform: uppercase; letter-spacing: 0.05em;">SYSTEM STATUS</h4>
            <div style="margin-bottom: 0.75rem;">
                <strong style="color: #EDEDED; font-family: 'Roboto Mono', monospace; font-size: 0.8rem;">VERSION:</strong><br>
                <span style="color: #C2B280; font-family: 'Roboto Mono', monospace; font-weight: 700;">{platform.version}</span>
            </div>
            <div style="margin-bottom: 0.75rem;">
                <strong style="color: #EDEDED; font-family: 'Roboto Mono', monospace; font-size: 0.8rem;">STATUS:</strong><br>
                <span style="color: #10B981; font-family: 'Roboto Mono', monospace; font-weight: 700;">{platform.deployment_status}</span>
            </div>
            <div>
                <strong style="color: #EDEDED; font-family: 'Roboto Mono', monospace; font-size: 0.8rem;">CLASS:</strong><br>
                <span style="color: #F59E0B; font-family: 'Roboto Mono', monospace; font-weight: 700;">{platform.classification}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("#### DATA UPLOAD")
        st.markdown("""
        <div style="background: rgba(245, 158, 11, 0.1); padding: 1rem; border-radius: 4px; border: 1px solid #F59E0B; margin-bottom: 1rem;">
            <strong style="color: #F59E0B; font-family: 'Orbitron', sans-serif; font-size: 0.8rem; text-transform: uppercase;">CSV MODE ACTIVE</strong><br>
            <span style="color: #F59E0B; font-family: 'Roboto Mono', monospace; font-size: 0.75rem;">UPLOAD .CSV FILES OR USE DEMO</span>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_files = st.file_uploader(
            "UPLOAD CSV FILES",
            type=['csv'],
            accept_multiple_files=True,
            help="CSV files only - convert Excel to CSV format"
        )
        
        if uploaded_files:
            st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 4px; border: 1px solid #10B981; margin-top: 1rem;">
                <strong style="color: #10B981; font-family: 'Orbitron', sans-serif; font-size: 0.8rem; text-transform: uppercase;">✓ {len(uploaded_files)} FILE(S) LOADED</strong>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Demo data option
        st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
        st.markdown("#### DEMO MODE")
        if st.button("LOAD SAMPLE DATA", help="Activate demonstration mode with tactical sample data"):
            st.session_state['use_demo'] = True
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="sidebar-section" style="text-align: center;">
            <h4 style="color: #C2B280; margin: 0 0 1rem 0; font-family: 'Orbitron', sans-serif; text-transform: uppercase;">MISSION STATUS</h4>
            <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 4px; border: 1px solid #10B981;">
                <strong style="color: #10B981; font-family: 'Orbitron', sans-serif; text-transform: uppercase; letter-spacing: 0.05em;">DARK OPS: OPERATIONAL</strong><br>
                <span style="color: #C2B280; font-family: 'Roboto Mono', monospace; font-size: 0.8rem;">MATTE CONFIG ACTIVE</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Tactical Interface
    if uploaded_files or st.session_state.get('use_demo', False):
        with st.spinner("PROCESSING TACTICAL INTELLIGENCE..."):
            if st.session_state.get('use_demo', False):
                tactical_data = {"sample_data": platform.create_sample_data()}
            else:
                tactical_data = platform.load_tactical_data(uploaded_files)
            
            analysis_results = platform.analyze_pan_governance(tactical_data)
            platform.create_executive_dashboard(analysis_results)
            
            # Dark Mode Tactical Analysis Tabs
            tab1, tab2, tab3 = st.tabs([
                "▲ CARRIER INTEL",
                "◉ QUALITY ANALYSIS",
                "▣ TACTICAL REPORTS"
            ])
            
            with tab1:
                platform.create_carrier_analysis(analysis_results.get('carriers', {}))
            
            with tab2:
                st.markdown('<h2 class="section-header">◉ DATA QUALITY INTELLIGENCE</h2>', unsafe_allow_html=True)
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    quality_score = analysis_results.get('quality_score', 0)
                    score_color = '#10B981' if quality_score >= 90 else '#F59E0B' if quality_score >= 80 else '#DC2626'
                    st.markdown(f"""
                    <div class="tactical-metric-card" style="text-align: center; padding: 2.5rem;">
                        <div class="tactical-metric-icon" style="font-size: 4rem;">◉</div>
                        <h3>OVERALL QUALITY SCORE</h3>
                        <h2 style="font-size: 4rem; color: {score_color}; text-shadow: 0 0 10px {score_color}40;">{quality_score}%</h2>
                        <p style="font-size: 1.2rem; font-weight: 700;"><strong>{platform.get_quality_grade(quality_score)}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    issues = analysis_results.get('critical_issues', [])
                    if issues:
                        st.markdown("### ! CRITICAL ISSUES")
                        for i, issue in enumerate(issues, 1):
                            st.markdown(f"""
                            <div class="tactical-alert">
                                <strong>ISSUE #{i:02d}:</strong> {issue}
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="tactical-success">
                            <strong>◉ NO CRITICAL ISSUES DETECTED</strong><br>
                            <span>PLATFORM MAINTAINS SOC-GRADE STANDARDS</span>
                        </div>
                        """, unsafe_allow_html=True)
            
            with tab3:
                st.markdown('<h2 class="section-header">▣ TACTICAL INTELLIGENCE REPORTS</h2>', unsafe_allow_html=True)
                
                report = f"""
🫡 AMR PAN TACTICAL INTELLIGENCE REPORT (DARK MODE OPS)
=====================================================
GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
PLATFORM VERSION: {platform.version}
CLASSIFICATION: {platform.classification}
MODE: DARK OPS CSV PROCESSING

EXECUTIVE SUMMARY
=================
TOTAL RECORDS ANALYZED: {analysis_results.get('total_pans', 0):,}
DATA QUALITY SCORE: {analysis_results.get('quality_score', 0)}%
QUALITY GRADE: {platform.get_quality_grade(analysis_results.get('quality_score', 0))}
CRITICAL ISSUES: {len(analysis_results.get('critical_issues', []))}

CARRIER DISTRIBUTION INTELLIGENCE
=================================
"""
                
                for carrier, count in analysis_results.get('carriers', {}).items():
                    percentage = (count / analysis_results.get('total_pans', 1)) * 100
                    report += f"{carrier}: {count:,} RECORDS ({percentage:.1f}%)\n"
                
                report += f"""

CRITICAL ISSUES ASSESSMENT
==========================
"""
                for i, issue in enumerate(analysis_results.get('critical_issues', []), 1):
                    report += f"{i:02d}. {issue}\n"
                
                if not analysis_results.get('critical_issues'):
                    report += "NO CRITICAL ISSUES DETECTED - SOC-GRADE STANDARDS MAINTAINED\n"
                
                report += f"""

MISSION STATUS
==============
DARK MODE OPS: OPERATIONAL
SOC-GRADE INTERFACE: ACTIVE
MATTE CONFIGURATION: DEPLOYED
VISUAL EXCELLENCE: TACTICAL BLACKOUT
NEXT PHASE: EXCEL PROCESSING RESTORATION

🫡 END OF TACTICAL INTELLIGENCE REPORT
=====================================
"""
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.text_area("EXECUTIVE INTELLIGENCE REPORT", report, height=500)
                
                with col2:
                    st.markdown("### EXPORT & DISTRIBUTION")
                    
                    st.download_button(
                        label="DOWNLOAD TACTICAL REPORT",
                        data=report,
                        file_name=f"AMR_Tactical_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
                    
                    st.markdown("### REPORT INTELLIGENCE")
                    st.markdown(f"""
                    <div class="tactical-metric-card">
                        <h3>TIMESTAMP</h3>
                        <h2>{datetime.now().strftime('%H%M')}</h2>
                        <p>{datetime.now().strftime('%Y-%m-%d')}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="tactical-metric-card">
                        <h3>DATA POINTS</h3>
                        <h2>{analysis_results.get('total_pans', 0):,}</h2>
                        <p>RECORDS ANALYZED</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div class="tactical-metric-card">
                        <h3>CLASSIFICATION</h3>
                        <h2>{platform.get_quality_grade(analysis_results.get('quality_score', 0)).split()[0]}</h2>
                        <p>MISSION GRADE</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    else:
        # Dark Mode Welcome Interface
        st.markdown("""
        <div class="tactical-command-header">
            <div class="tactical-logo tactical-glow">🫡</div>
            <h1>AMR PAN TACTICAL INTELLIGENCE</h1>
            <h3>DARK MODE OPS • SOC-GRADE INTERFACE READY</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<h2 class="section-header">! DARK MODE CONFIGURATION</h2>', unsafe_allow_html=True)
            st.markdown("""
            <div class="tactical-alert">
                <strong>SOC-GRADE INTERFACE ACTIVE</strong><br>
                <span>MATTE BLACK CONFIGURATION DEPLOYED FOR FIELD-GRADE OPERATIONS</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### OPERATIONAL PROCEDURES:")
            instructions = [
                "CONVERT EXCEL FILES TO CSV FORMAT (FILE → SAVE AS → CSV)",
                "UPLOAD CSV FILES USING TACTICAL CONTROLS SIDEBAR",
                "OR ACTIVATE DEMO MODE FOR IMMEDIATE PLATFORM DEMONSTRATION",
                "FULL TACTICAL ANALYSIS WILL BE EXECUTED ON YOUR DATA"
            ]
            
            for i, instruction in enumerate(instructions, 1):
                st.markdown(f"""
                <div class="tactical-metric-card" style="text-align: left; margin: 1rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div style="background: #C2B280; color: #0F0F0F; border-radius: 2px; width: 2rem; height: 2rem; display: flex; align-items: center; justify-content: center; margin-right: 1rem; font-weight: 700; font-family: 'Roboto Mono', monospace;">{i:02d}</div>
                        <p style="margin: 0; color: #EDEDED; font-weight: 500; font-family: 'Roboto Mono', monospace; font-size: 0.9rem;">{instruction}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown('<h2 class="section-header">▲ TACTICAL CAPABILITIES</h2>', unsafe_allow_html=True)
            
            capabilities = [
                ("▣", "REAL-TIME DATA ANALYSIS", "CSV PROCESSING WITH FULL ANALYTICS"),
                ("◉", "QUALITY INTELLIGENCE", "AUTOMATED SCORING AND ISSUE DETECTION"),
                ("▲", "CARRIER ANALYSIS", "DISTRIBUTION INTELLIGENCE AND INSIGHTS"),
                ("▣", "EXECUTIVE REPORTS", "SOC-GRADE TACTICAL REPORTING"),
                ("!", "DARK MODE OPS", "MATTE BLACK INTERFACE CONFIGURATION")
            ]
            
            for icon, title, desc in capabilities:
                st.markdown(f"""
                <div class="tactical-metric-card" style="text-align: left; margin: 1rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div style="font-size: 1.5rem; margin-right: 1rem; color: #C2B280;">{icon}</div>
                        <div>
                            <h3 style="margin: 0; color: #C2B280; font-size: 1rem; font-family: 'Orbitron', sans-serif; text-transform: uppercase;">{title}</h3>
                            <p style="margin: 0.25rem 0 0 0; color: #EDEDED; font-size: 0.8rem; font-family: 'Roboto Mono', monospace;">{desc}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Excel Conversion Guide
        st.markdown('<h2 class="section-header">🔄 EXCEL CONVERSION PROCEDURES</h2>', unsafe_allow_html=True)
        
        conversion_col1, conversion_col2 = st.columns([1, 1])
        
        with conversion_col1:
            st.markdown("""
            <div class="tactical-success">
                <strong>WINDOWS EXCEL PROCEDURE:</strong><br>
                01. OPEN EXCEL FILE<br>
                02. CLICK FILE → SAVE AS<br>
                03. SELECT CSV (COMMA DELIMITED) FORMAT<br>
                04. EXECUTE SAVE COMMAND
            </div>
            """, unsafe_allow_html=True)
        
        with conversion_col2:
            st.markdown("""
            <div class="tactical-success">
                <strong>MAC EXCEL PROCEDURE:</strong><br>
                01. OPEN EXCEL FILE<br>
                02. CLICK FILE → SAVE AS<br>
                03. SELECT COMMA SEPARATED VALUES (.CSV)<br>
                04. EXECUTE SAVE COMMAND
            </div>
            """, unsafe_allow_html=True)
        
        # Final status banner
        st.markdown("""
        <div class="status-indicator status-excellent" style="margin-top: 3rem;">
            ◉ DARK MODE OPS CONFIGURATION ACTIVE - SOC-GRADE TACTICAL INTERFACE READY
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

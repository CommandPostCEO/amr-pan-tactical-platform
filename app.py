# 🫡 AMR PAN TACTICAL INTELLIGENCE PLATFORM
# EMERGENCY CSV SOLUTION - STREAMLIT CLOUD COMPATIBLE
# Phase 3A: Visual Excellence with CSV Processing

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List
import io
import base64

# 🎖️ TACTICAL CONFIGURATION
st.set_page_config(
    page_title="🫡 AMR Tactical Intelligence",
    page_icon="🫡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🛡️ TACTICAL CSS STYLING SYSTEM
TACTICAL_CSS = """
<style>
    /* ===== CORE SYSTEM OVERRIDES ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        scroll-behavior: smooth;
    }
    
    .main .block-container {
        padding: 1rem 2rem 3rem 2rem;
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* ===== TACTICAL HEADER SYSTEM ===== */
    .tactical-command-header {
        background: linear-gradient(135deg, 
            #0f172a 0%, 
            #1e293b 25%, 
            #334155 50%, 
            #1e293b 75%, 
            #0f172a 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 2.5rem;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.3),
            0 0 0 1px rgba(255, 255, 255, 0.05),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .tactical-command-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: 
            radial-gradient(circle at 20% 80%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
        opacity: 0.7;
        animation: tactical-pulse 4s ease-in-out infinite alternate;
    }
    
    @keyframes tactical-pulse {
        0% { opacity: 0.5; }
        100% { opacity: 0.8; }
    }
    
    .tactical-command-header h1 {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
        letter-spacing: -0.025em;
        position: relative;
        z-index: 2;
        background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .tactical-logo {
        display: inline-block;
        font-size: 3.5rem;
        margin-right: 1rem;
        filter: drop-shadow(3px 3px 6px rgba(0, 0, 0, 0.6));
        position: relative;
        z-index: 2;
    }
    
    /* ===== ENHANCED METRIC CARD SYSTEM ===== */
    .tactical-metric-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%);
        padding: 2rem 1.5rem;
        border-radius: 14px;
        box-shadow: 
            0 4px 20px rgba(0, 0, 0, 0.08),
            0 1px 3px rgba(0, 0, 0, 0.05),
            inset 0 1px 0 rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(0, 0, 0, 0.04);
        margin: 0.75rem 0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .tactical-metric-card:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.15),
            0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .tactical-metric-card h3 {
        color: #334155;
        font-size: 0.85rem;
        font-weight: 700;
        margin: 0 0 0.75rem 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .tactical-metric-card h2 {
        color: #0f172a;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0 0 0.5rem 0;
        line-height: 1;
    }
    
    .tactical-metric-card p {
        color: #64748b;
        font-size: 0.9rem;
        margin: 0;
        font-weight: 500;
    }
    
    /* ===== STATUS INDICATOR SYSTEM ===== */
    .status-indicator {
        padding: 1.5rem 2rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
        font-size: 1.1rem;
        margin: 2rem 0;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .status-excellent {
        background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%);
        color: white;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
    }
    
    .status-warning {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #b45309 100%);
        color: white;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.4);
    }
    
    .status-alert {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 50%, #b91c1c 100%);
        color: white;
        box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
    }
    
    /* ===== FEEDBACK SYSTEM ===== */
    .tactical-alert {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border: 1px solid #f59e0b;
        border-left: 4px solid #f59e0b;
        padding: 1.25rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        color: #92400e;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
    }
    
    .tactical-success {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border: 1px solid #10b981;
        border-left: 4px solid #10b981;
        padding: 1.25rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        color: #065f46;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.15);
    }
    
    /* ===== BUTTON SYSTEM ===== */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%);
        color: white;
        border: none;
        padding: 0.875rem 2rem;
        border-radius: 10px;
        font-weight: 700;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 14px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
    }
    
    /* ===== FILE UPLOADER ===== */
    .stFileUploader > div > div {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border: 2px dashed #94a3b8;
        border-radius: 16px;
        padding: 3rem 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div > div:hover {
        border-color: #3b82f6;
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    }
</style>
"""

class AMRPANTacticalPlatform:
    """🫡 AMR PAN Tactical Intelligence Platform - Emergency CSV Solution"""
    
    def __init__(self):
        self.version = "3.0.4-EMERGENCY-CSV"
        self.deployment_status = "STREAMLIT CLOUD READY"
        self.classification = "TACTICAL INTELLIGENCE"
        
    def create_sample_data(self) -> Dict:
        """🎯 Generate sample tactical data for demonstration"""
        # Create realistic sample AMR PAN data
        sample_data = {
            'total_pans': 3247,
            'carriers': {
                'UPS': 2156,
                'FedEx': 847,
                'DHL': 188,
                'CEVA': 56
            },
            'status_distribution': {
                'completed': 2987,
                'pending': 186,
                'denied': 74
            },
            'quality_score': 91.2,
            'critical_issues': [
                'UPS invalid format count: 23',
                'Missing carrier account numbers: 12'
            ]
        }
        return sample_data
    
    def load_tactical_data(self, uploaded_files: List) -> Dict:
        """🔄 Load CSV data with fallback to sample data"""
        tactical_data = {}
        
        if not uploaded_files:
            # Show sample data message
            st.markdown("""
            <div class="tactical-alert">
                <strong>📊 Sample Data Mode:</strong> Upload CSV files or use demo data below<br>
                <strong>💡 Tip:</strong> Convert Excel files to CSV format for compatibility
            </div>
            """, unsafe_allow_html=True)
            return {"sample_data": self.create_sample_data()}
        
        try:
            for uploaded_file in uploaded_files:
                if uploaded_file.name.endswith('.csv'):
                    # Read CSV file
                    df = pd.read_csv(uploaded_file)
                    tactical_data[uploaded_file.name] = {'Sheet1': df}
                    
                    st.markdown(f"""
                    <div class="tactical-success">
                        <strong>✅ CSV Data Loaded:</strong> {uploaded_file.name}<br>
                        <strong>📊 Records:</strong> {len(df):,} rows, {len(df.columns)} columns
                    </div>
                    """, unsafe_allow_html=True)
                    
                elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                    st.markdown(f"""
                    <div class="tactical-alert">
                        <strong>⚠️ Excel File Detected:</strong> {uploaded_file.name}<br>
                        <strong>🔄 Solution:</strong> Please convert to CSV format for compatibility<br>
                        <strong>💡 How:</strong> Open in Excel → Save As → CSV (Comma delimited)
                    </div>
                    """, unsafe_allow_html=True)
                    
        except Exception as e:
            st.markdown(f"""
            <div class="tactical-alert">
                <strong>⚠️ Data Loading Error:</strong> {str(e)}<br>
                <strong>🛡️ Fallback:</strong> Using sample data for demonstration
            </div>
            """, unsafe_allow_html=True)
            tactical_data = {"sample_data": self.create_sample_data()}
            
        return tactical_data
    
    def analyze_pan_governance(self, data: Dict) -> Dict:
        """🎯 Analyze PAN data with CSV processing"""
        
        # If using sample data
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
                    # Try to find PAN-related data
                    if len(df) > 0:
                        analysis_results['total_pans'] = len(df)
                        
                        # Look for carrier column (flexible matching)
                        carrier_cols = [col for col in df.columns if 'carrier' in col.lower()]
                        if carrier_cols:
                            carrier_counts = df[carrier_cols[0]].value_counts()
                            analysis_results['carriers'] = carrier_counts.to_dict()
                        
                        # Look for status column
                        status_cols = [col for col in df.columns if 'status' in col.lower()]
                        if status_cols:
                            status_counts = df[status_cols[0]].value_counts()
                            analysis_results['status_distribution'] = status_counts.to_dict()
                        
                        # Calculate basic quality score
                        completeness = (df.notna().sum().sum() / df.size) * 100
                        analysis_results['quality_score'] = round(completeness, 1)
                        
                        # Basic quality issues
                        missing_data = df.isnull().sum()
                        for col, missing in missing_data.items():
                            if missing > 0:
                                pct = (missing / len(df)) * 100
                                if pct > 5:  # More than 5% missing
                                    analysis_results['critical_issues'].append(
                                        f"Missing data in {col}: {missing} records ({pct:.1f}%)"
                                    )
                        break
                break
                
        except Exception as e:
            st.markdown(f"""
            <div class="tactical-alert">
                <strong>⚠️ Analysis Error:</strong> {str(e)}<br>
                <strong>🛡️ Fallback:</strong> Using sample analysis results
            </div>
            """, unsafe_allow_html=True)
            analysis_results = self.create_sample_data()
            
        return analysis_results
    
    def create_executive_dashboard(self, analysis: Dict) -> None:
        """🎖️ Executive dashboard with tactical excellence"""
        
        # Tactical Command Header
        st.markdown("""
        <div class="tactical-command-header">
            <div class="tactical-logo">🫡</div>
            <h1>AMR PAN TACTICAL INTELLIGENCE</h1>
            <h3>Emergency CSV Mode • Streamlit Cloud Compatible</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Executive Metrics Grid
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="tactical-metric-card">
                <h3>📊 Total PANs</h3>
                <h2>{analysis.get('total_pans', 0):,}</h2>
                <p>Active Parcel Accounts</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            quality_score = analysis.get('quality_score', 0)
            quality_grade = self.get_quality_grade(quality_score)
            st.markdown(f"""
            <div class="tactical-metric-card">
                <h3>🎯 Quality Score</h3>
                <h2>{quality_score}%</h2>
                <p>{quality_grade}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            carrier_count = len(analysis.get('carriers', {}))
            st.markdown(f"""
            <div class="tactical-metric-card">
                <h3>🚛 Active Carriers</h3>
                <h2>{carrier_count}</h2>
                <p>Strategic Partners</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            critical_issues = len(analysis.get('critical_issues', []))
            st.markdown(f"""
            <div class="tactical-metric-card">
                <h3>⚠️ Critical Issues</h3>
                <h2>{critical_issues}</h2>
                <p>Immediate Action</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Mission Status Banner
        if quality_score >= 90:
            status_class = "status-excellent"
            status_text = "🎖️ MISSION READY - Tactical Excellence Achieved"
        elif quality_score >= 80:
            status_class = "status-warning"
            status_text = "⚡ OPERATIONAL - Minor Optimizations Needed"
        else:
            status_class = "status-alert"
            status_text = "🚨 TACTICAL ALERT - Immediate Action Required"
        
        st.markdown(f"""
        <div class="status-indicator {status_class}">
            {status_text}
        </div>
        """, unsafe_allow_html=True)
    
    def create_carrier_analysis(self, carriers: Dict) -> None:
        """🚛 Enhanced carrier distribution intelligence"""
        if not carriers:
            st.warning("⚠️ No carrier data available for tactical analysis")
            return
        
        st.markdown("## 🚛 Carrier Distribution Intelligence")
        
        carrier_df = pd.DataFrame(list(carriers.items()), columns=['Carrier', 'PANs'])
        carrier_df['Percentage'] = (carrier_df['PANs'] / carrier_df['PANs'].sum() * 100).round(1)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📈 PAN Distribution Analysis")
            st.bar_chart(carrier_df.set_index('Carrier')['PANs'])
        
        with col2:
            st.markdown("### 📊 Strategic Partner Summary")
            for _, row in carrier_df.iterrows():
                st.markdown(f"""
                <div class="tactical-metric-card" style="text-align: left; margin: 0.75rem 0;">
                    <h3>🚛 {row['Carrier']}</h3>
                    <h2>{row['PANs']:,}</h2>
                    <p>{row['Percentage']:.1f}% of operations</p>
                </div>
                """, unsafe_allow_html=True)
    
    def get_quality_grade(self, score: float) -> str:
        """🏆 Quality grading system"""
        if score >= 95:
            return "A+ Excellence"
        elif score >= 90:
            return "A Mission Ready"
        elif score >= 85:
            return "B+ Operational"
        elif score >= 80:
            return "B Acceptable"
        else:
            return "C Needs Improvement"

def main():
    """🎖️ Main tactical platform interface"""
    
    # Deploy Tactical CSS
    st.markdown(TACTICAL_CSS, unsafe_allow_html=True)
    
    platform = AMRPANTacticalPlatform()
    
    # Enhanced Tactical Sidebar
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 1rem; background: rgba(255,255,255,0.1); border-radius: 12px; margin-bottom: 2rem;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">🫡</div>
            <h3 style="color: white; margin: 0; font-weight: 700;">Tactical Command</h3>
            <p style="color: #cbd5e1; margin: 0.5rem 0 0 0; font-size: 0.9rem;">Emergency CSV Mode</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.08); padding: 1.5rem; border-radius: 12px; margin: 1rem 0;">
            <h4 style="color: #60a5fa; margin: 0 0 1rem 0;">Platform Status</h4>
            <div style="margin-bottom: 0.75rem;">
                <strong style="color: #e2e8f0;">Version:</strong><br>
                <span style="color: #60a5fa;">{platform.version}</span>
            </div>
            <div style="margin-bottom: 0.75rem;">
                <strong style="color: #e2e8f0;">Status:</strong><br>
                <span style="color: #10b981;">{platform.deployment_status}</span>
            </div>
            <div>
                <strong style="color: #e2e8f0;">Mode:</strong><br>
                <span style="color: #f59e0b;">CSV COMPATIBLE</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📁 Data Upload")
        st.markdown("""
        <div style="background: rgba(245, 158, 11, 0.1); padding: 1rem; border-radius: 8px; border: 1px solid #f59e0b; margin-bottom: 1rem;">
            <strong style="color: #f59e0b;">📋 CSV Mode Active</strong><br>
            <span style="color: #92400e;">Upload .csv files or use demo data</span>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_files = st.file_uploader(
            "Upload CSV Files",
            type=['csv'],
            accept_multiple_files=True,
            help="CSV files only - convert Excel files to CSV format"
        )
        
        if uploaded_files:
            st.markdown(f"""
            <div style="background: rgba(16, 185, 129, 0.2); padding: 1rem; border-radius: 8px; border: 1px solid #10b981; margin-top: 1rem;">
                <strong style="color: #10b981;">✅ {len(uploaded_files)} CSV file(s) loaded</strong>
            </div>
            """, unsafe_allow_html=True)
        
        # Demo data option
        st.markdown("#### 🎯 Demo Mode")
        if st.button("Load Sample Data", help="Use realistic AMR PAN demo data"):
            st.session_state['use_demo'] = True
        
        st.markdown("""
        <div style="background: rgba(16, 185, 129, 0.2); padding: 1rem; border-radius: 8px; text-align: center; margin-top: 2rem;">
            <strong style="color: #10b981;">Emergency Mode: OPERATIONAL</strong><br>
            <span style="color: #065f46;">CSV Processing Active</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Tactical Interface
    if uploaded_files or st.session_state.get('use_demo', False):
        with st.spinner("🔄 Processing tactical intelligence..."):
            if st.session_state.get('use_demo', False):
                tactical_data = {"sample_data": platform.create_sample_data()}
            else:
                tactical_data = platform.load_tactical_data(uploaded_files)
            
            analysis_results = platform.analyze_pan_governance(tactical_data)
            platform.create_executive_dashboard(analysis_results)
            
            # Tactical Analysis Tabs
            tab1, tab2, tab3 = st.tabs([
                "🚛 Carrier Intelligence",
                "📊 Data Analysis",
                "📋 Intelligence Report"
            ])
            
            with tab1:
                platform.create_carrier_analysis(analysis_results.get('carriers', {}))
            
            with tab2:
                st.markdown("## 📊 Data Quality Analysis")
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    quality_score = analysis_results.get('quality_score', 0)
                    st.markdown(f"""
                    <div class="tactical-metric-card" style="text-align: center; padding: 2.5rem;">
                        <h3>🎯 Quality Score</h3>
                        <h2 style="font-size: 3.5rem; color: {'#10b981' if quality_score >= 90 else '#f59e0b' if quality_score >= 80 else '#ef4444'};">{quality_score}%</h2>
                        <p style="font-size: 1.2rem;"><strong>{platform.get_quality_grade(quality_score)}</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    issues = analysis_results.get('critical_issues', [])
                    if issues:
                        st.markdown("### ⚠️ Critical Issues")
                        for i, issue in enumerate(issues, 1):
                            st.markdown(f"""
                            <div class="tactical-alert">
                                <strong>Issue #{i}:</strong> {issue}
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="tactical-success">
                            <strong>🎖️ No Critical Issues</strong><br>
                            Platform maintains excellence standards
                        </div>
                        """, unsafe_allow_html=True)
            
            with tab3:
                st.markdown("## 📋 Tactical Intelligence Report")
                
                report = f"""
🫡 AMR PAN TACTICAL INTELLIGENCE REPORT (Emergency CSV Mode)
==========================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Platform Version: {platform.version}
Mode: CSV Compatible Processing

EXECUTIVE SUMMARY
=================
Total Records Analyzed: {analysis_results.get('total_pans', 0):,}
Data Quality Score: {analysis_results.get('quality_score', 0)}%
Quality Grade: {platform.get_quality_grade(analysis_results.get('quality_score', 0))}
Critical Issues: {len(analysis_results.get('critical_issues', []))}

CARRIER DISTRIBUTION
===================
"""
                
                for carrier, count in analysis_results.get('carriers', {}).items():
                    percentage = (count / analysis_results.get('total_pans', 1)) * 100
                    report += f"{carrier}: {count:,} records ({percentage:.1f}%)\n"
                
                report += """

MISSION STATUS
==============
Emergency CSV Mode: OPERATIONAL
Streamlit Cloud: COMPATIBLE
Visual Excellence: ACTIVE
Next Phase: Excel Processing Restoration

🫡 END OF TACTICAL INTELLIGENCE REPORT
"""
                
                st.text_area("📄 Executive Report", report, height=400)
                
                st.download_button(
                    label="📥 Download Report",
                    data=report,
                    file_name=f"AMR_Tactical_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
    
    else:
        # Enhanced Welcome Interface
        st.markdown("""
        <div class="tactical-command-header">
            <div class="tactical-logo">🫡</div>
            <h1>AMR PAN TACTICAL INTELLIGENCE</h1>
            <h3>Emergency CSV Mode • Streamlit Cloud Compatible</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("## 🚨 Emergency CSV Mode")
            st.markdown("""
            <div class="tactical-alert">
                <strong>🛡️ Streamlit Cloud Compatibility Mode</strong><br>
                Due to openpyxl dependency issues, the platform is operating in CSV mode for maximum compatibility.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📋 How to Use:")
            instructions = [
                "Convert Excel files to CSV format (File → Save As → CSV)",
                "Upload CSV files using the sidebar",
                "Or click 'Load Sample Data' to see demo functionality",
                "Full tactical analysis will be performed on your data"
            ]
            
            for i, instruction in enumerate(instructions, 1):
                st.markdown(f"""
                <div class="tactical-metric-card" style="text-align: left; margin: 1rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div style="background: #3b82f6; color: white; border-radius: 50%; width: 2rem; height: 2rem; display: flex; align-items: center; justify-content: center; margin-right: 1rem; font-weight: bold;">{i}</div>
                        <p style="margin: 0; color: #1e293b; font-weight: 500;">{instruction}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("## 🎖️ Platform Capabilities")
            
            capabilities = [
                ("📊", "Real-time Data Analysis", "CSV processing with full analytics"),
                ("🎯", "Quality Intelligence", "Automated scoring and issue detection"),
                ("🚛", "Carrier Analysis", "Distribution intelligence and insights"),
                ("📋", "Executive Reports", "Professional tactical reporting"),
                ("⚡", "Visual Excellence", "Enterprise-grade interface design")
            ]
            
            for icon, title, desc in capabilities:
                st.markdown(f"""
                <div class="tactical-metric-card" style="text-align: left; margin: 1rem 0;">
                    <div style="display: flex; align-items: center;">
                        <div style="font-size: 1.5rem; margin-right: 1rem;">{icon}</div>
                        <div>
                            <h3 style="margin: 0; color: #1e293b; font-size: 1rem;">{title}</h3>
                            <p style="margin: 0.25rem 0 0 0; color: #64748b; font-size: 0.9rem;">{desc}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Excel to CSV Conversion Guide
        st.markdown("## 🔄 Excel to CSV Conversion Guide")
        
        conversion_col1, conversion_col2 = st.columns([1, 1])
        
        with conversion_col1:
            st.markdown("""
            <div class="tactical-success">
                <strong>🖥️ Windows Excel:</strong><br>
                1. Open your Excel file<br>
                2. Click "File" → "Save As"<br>
                3. Choose "CSV (Comma delimited)" format<br>
                4. Click "Save"
            </div>
            """, unsafe_allow_html=True)
        
        with conversion_col2:
            st.markdown("""
            <div class="tactical-success">
                <strong>🍎 Mac Excel:</strong><br>
                1. Open your Excel file<br>
                2. Click "File" → "Save As"<br>
                3. Select "Comma Separated Values (.csv)"<br>
                4. Click "Save"
            </div>
            """, unsafe_allow_html=True)
        
        # Sample Data Demo
        st.markdown("## 🎯 Demo Mode Available")
        st.markdown("""
        <div class="tactical-alert">
            <strong>📊 Try Sample Data:</strong> Click "Load Sample Data" in the sidebar to see the platform in action with realistic AMR PAN data including UPS, FedEx, DHL carrier analysis.
        </div>
        """, unsafe_allow_html=True)
        
        # Final status banner
        st.markdown("""
        <div class="status-indicator status-warning" style="margin-top: 3rem;">
            🚨 EMERGENCY CSV MODE ACTIVE - STREAMLIT CLOUD COMPATIBLE
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

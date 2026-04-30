import streamlit as st
import pandas as pd

# 1. إعدادات الهوية السيادية - النسخة الصافية
st.set_page_config(page_title="SOVEREIGN TRUTH LEDGER", page_icon="⚖️", layout="centered")

# 2. واجهة غرفة العمليات (Titanium High-Contrast)
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #1e293b 0%, #05080a 100%);
        color: #ffffff;
    }
    /* وضوح المؤشرات */
    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-size: 55px !important;
        font-weight: 900 !important;
        text-shadow: 0 0 20px rgba(0, 217, 255, 0.4);
    }
    div[data-testid="stMetricLabel"] p {
        color: #ffd700 !important;
        font-size: 16px !important;
        font-weight: 900;
        text-transform: uppercase;
    }
    /* كروت المواجهات الحقيقية */
    .match-card {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #ffd700;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .score-tag { color: #00ff88; font-weight: 900; font-size: 24px; }
    .team-name { color: #ffffff; font-size: 18px; font-weight: bold; }
    label { color: #ffd700 !important; font-weight: 900 !important; }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. جلب الأرشيف الحرفي (الناقل الصادق)
@st.cache_data
def load_historical_vault():
    try:
        return pd.read_csv('database.csv')
    except:
        return pd.DataFrame(columns=['date','league','home','away','o1','ox','o2','score','u25'])

df = load_historical_vault()

# 4. بناء الواجهة
st.markdown("<div style='text-align: center; margin-top:30px;'><h1 style='color:#ffd700; font-size:35px; letter-spacing:10px; margin-bottom:0;'>SOVEREIGN</h1><p style='color:#00ff88; font-weight:900;'>PURE FORENSIC ARCHIVE • V101.0</p></div>", unsafe_allow_html=True)

# اختيار الدوري
league_options = {"🇹🇳 تونس (LIGUE 1)": "tun", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 إنجلترا (PREMIER)": "pre", "🌍 العالم (GENERAL)": "gen"}
selected_league = st.selectbox("🎯 حدد خزنة الأرشيف:", list(league_options.keys()))
lg_code = league_options[selected_league]

# إحداثيات البحث المجهري
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: o1_in = st.number_input("1 (HOME)", min_value=1.0, value=1.0, step=0.01)
with c2: ox_in = st.number_input("X (DRAW)", min_value=1.0, value=1.0, step=0.01)
with c3: o2_in = st.number_input("2 (AWAY)", min_value=1.0, value=1.0, step=0.01)

# 5. محرك الجرد الحقيقي
if o1_in > 1.01 and ox_in > 1.01 and o2_in > 1.01:
    st.divider()
    # الفلترة الحرفية بنطاق 0.01
    results = df[
        (df['league'] == lg_code) & 
        (df['o1'].between(o1_in - 0.01, o1_in + 0.01)) &
        (df['o2'].between(o2_in - 0.01, o2_in + 0.01))
    ]

    if not results.empty:
        st.markdown(f"<p style='text-align:center; color:#00ff88; font-weight:900; font-size:18px;'>✅ جرد ناجح: تم العثور على {len(results)} مواجهات تاريخية</p>", unsafe_allow_html=True)
        
        # عرض النسب التاريخية الحقيقية
        u25_pct = (results['u25'].sum() / len(results)) * 100
        m1, m2 = st.columns(2)
        m1.metric("ARCHIVE U2.5", f"{int(u25_pct)}%")
        m2.metric("EXACT SAMPLES", len(results))

        st.markdown("<br><h3 style='color:#ffd700; text-align:center;'>📂 السجلات التاريخية المكتشفة</h3>", unsafe_allow_html=True)
        
        # سرد المواجهات الحقيقية
        for _, row in results.iterrows():
            st.markdown(f"""
            <div class='match-card'>
                <span style='color:#888; font-size:12px;'>📅 {row['date']}</span><br>
                <span class='team-name'>{row['home']} <span style='color:#ffd700;'>vs</span> {row['away']}</span><br>
                <span style='color:#555; font-size:12px;'>Odds: {row['o1']} - {row['ox']} - {row['o2']}</span><br>
                <span class='score-tag'>RESULT: {row['score']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ هذا النمط الرقمي لم يسجل له أي مباراة حقيقية في ملف الأرشيف الحالي.")
else:
    st.markdown("<p style='text-align:center; color:#637381; font-size:14px; margin-top:50px;'>بانتظار إحداثيات (1-X-2) لفتح سجلات الحقيقة.</p>", unsafe_allow_html=True)

st.markdown("<br><br><div style='text-align: center; color: #ffffff; font-size: 10px; font-weight:bold; opacity:0.2;'>PURE FORENSIC LEDGER • NO SYNC LINKS • V101.0</div>", unsafe_allow_html=True)

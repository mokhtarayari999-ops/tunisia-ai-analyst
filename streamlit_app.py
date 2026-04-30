import streamlit as st
import pandas as pd

# 1. إعدادات الكمال والشمولية
st.set_page_config(page_title="GLOBAL TRUTH LEDGER", page_icon="🌐", layout="centered")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1e293b 0%, #05080a 100%); color: white; }
    div[data-testid="stMetricValue"] { color: #ffffff !important; font-size: 45px !important; font-weight: 900; }
    .match-card { background: rgba(255, 255, 255, 0.03); border-left: 5px solid #ffd700; padding: 15px; border-radius: 12px; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.05); }
    .score-tag { color: #00ff88; font-weight: 900; font-size: 20px; }
    .league-badge { background: #ffd700; color: black; padding: 2px 8px; border-radius: 5px; font-size: 10px; font-weight: 900; }
    </style>
    """, unsafe_allow_html=True)

# 2. استدعاء الأرشيف الشامل
@st.cache_data
def load_global_archive():
    try:
        return pd.read_csv('database.csv')
    except:
        return pd.DataFrame(columns=['date','league','home','away','o1','ox','o2','score','u25'])

df = load_global_archive()

# 3. بناء الواجهة العالمية
st.markdown("<div style='text-align: center; margin-top:20px;'><h1 style='color:#ffd700; font-size:35px; letter-spacing:8px;'>SOVEREIGN</h1><p style='color:#00ff88; font-weight:900;'>V102.0 • GLOBAL HISTORICAL LEDGER</p></div>", unsafe_allow_html=True)

# قائمة الدوريات الشاملة
leagues = {
    "🌍 أرشيف العالم (General)": "gen",
    "🇹🇳 تونس (Ligue 1)": "tun",
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 إنجلترا (Premier League)": "pre",
    "🇪🇸 إسبانيا (La Liga)": "lal",
    "🇩🇪 ألمانيا (Bundesliga)": "bun",
    "🇮🇹 إيطاليا (Serie A)": "ita",
    "🇫🇷 فرنسا (Ligue 1)": "fra",
    "🇳🇱 هولندا (Eredivisie)": "ned"
}
selected_name = st.selectbox("🎯 اختر خزنة الأرشيف:", list(leagues.keys()))
lg_code = leagues[selected_name]

# إحداثيات البحث المجهري
c1, c2, c3 = st.columns(3)
with c1: o1_in = st.number_input("1 (HOME)", min_value=1.0, value=1.0, step=0.01)
with c2: ox_in = st.number_input("X (DRAW)", min_value=1.0, value=1.0, step=0.01)
with c3: o2_in = st.number_input("2 (AWAY)", min_value=1.0, value=1.0, step=0.01)

if o1_in > 1.01:
    st.divider()
    # محرك الجرد الشامل بنطاق 0.01
    # إذا بحثت في "العالم"، سيبحث في كل ملف الـ CSV، وإذا حددت دوري سيبحث فيه هو فقط.
    if lg_code == "gen":
        results = df[ (df['o1'].between(o1_in - 0.01, o1_in + 0.01)) & (df['o2'].between(o2_in - 0.01, o2_in + 0.01)) ]
    else:
        results = df[ (df['league'] == lg_code) & (df['o1'].between(o1_in - 0.01, o1_in + 0.01)) & (df['o2'].between(o2_in - 0.01, o2_in + 0.01)) ]

    if not results.empty:
        st.markdown(f"<p style='text-align:center; color:#00ff88; font-weight:900; font-size:18px;'>✅ تم جرد {len(results)} مواجهات تاريخية مطابقة</p>", unsafe_allow_html=True)
        
        u25_pct = (results['u25'].sum() / len(results)) * 100
        
        # عرض "خلاصة الحقيقة"
        col_a, col_b = st.columns(2)
        col_a.metric("U2.5 REALITY", f"{int(u25_pct)}%")
        
        # حساب النتيجة الأكثر تكراراً
        top_score = results['score'].mode()[0]
        col_b.metric("MOST FREQUENT", top_score)

        st.markdown("### 📂 السجلات الجنائية المكتشفة:")
        for _, row in results.iterrows():
            st.markdown(f"""
            <div class='match-card'>
                <span class='league-badge'>{row['league'].upper()}</span> 
                <span style='color:#888; font-size:11px; margin-left:10px;'>📅 {row['date']}</span><br>
                <span style='color:white; font-weight:bold;'>{row['home']} vs {row['away']}</span><br>
                <span class='score-tag'>RESULT: {row['score']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ هذا النمط الرقمي غير مسجل في أرشيف الـ 5 سنوات الأخيرة.")
else:
    st.info("أدخل إحداثيات الأودز لبدء الجرد العالمي.")
        

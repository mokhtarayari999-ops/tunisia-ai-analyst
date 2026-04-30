import streamlit as st
import pandas as pd

# 1. إعدادات الهوية الصادقة
st.set_page_config(page_title="THE TRUTH LEDGER", page_icon="⚖️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1e293b 0%, #05080a 100%); color: white; }
    .match-card { background: rgba(255,255,255,0.03); border-left: 5px solid #ffd700; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .score-tag { color: #00ff88; font-weight: 900; font-size: 20px; }
    .team-name { color: #ffffff; font-size: 14px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. جلب الأرشيف الحرفي
@st.cache_data
def load_truth_data():
    try:
        return pd.read_csv('database.csv')
    except:
        return pd.DataFrame(columns=['date','league','home','away','o1','ox','o2','score','u25'])

df = load_truth_data()

# 3. بناء الواجهة
st.title("⚖️ THE SOVEREIGN LEDGER")
st.markdown("<p style='color:#ffd700; font-weight:900;'>سجل الجرد التاريخي الحقيقي (مباريات فعلية)</p>", unsafe_allow_html=True)

selected_league = st.selectbox("🎯 اختر خزنة الدوري:", ["tun", "pre", "gen"])

# إحداثيات البحث
c1, c2, c3 = st.columns(3)
with c1: o1_in = st.number_input("1", min_value=1.0, value=1.0, step=0.01)
with c2: ox_in = st.number_input("X", min_value=1.0, value=1.0, step=0.01)
with c3: o2_in = st.number_input("2", min_value=1.0, value=1.0, step=0.01)

if o1_in > 1.01:
    # البحث المجهري الحقيقي (0.01)
    results = df[
        (df['league'] == selected_league) & 
        (df['o1'].between(o1_in - 0.01, o1_in + 0.01)) &
        (df['o2'].between(o2_in - 0.01, o2_in + 0.01))
    ]

    if not results.empty:
        st.success(f"✅ تم العثور على {len(results)} مباريات حقيقية في الأرشيف")
        
        # حساب الحقيقة من السجلات
        u25_pct = (results['u25'].sum() / len(results)) * 100
        st.metric("UNDER 2.5 REALITY", f"{int(u25_pct)}%")

        st.markdown("### 📂 سجل المواجهات التاريخية المطابقة:")
        
        for index, row in results.iterrows():
            st.markdown(f"""
            <div class='match-card'>
                <span style='color:#888; font-size:10px;'>{row['date']}</span><br>
                <span class='team-name'>{row['home']} vs {row['away']}</span><br>
                <span style='color:#ffd700; font-size:12px;'>Odds: {row['o1']} - {row['ox']} - {row['o2']}</span><br>
                <span class='score-tag'>RESULT: {row['score']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ هذا النمط الرقمي لم يسجل له أي مباراة حقيقية في الأرشيف حتى الآن.")

st.divider()
st.link_button("📡 المزامنة مع المصدر (BETEXPLORER)", f"https://betexplorer.com{o1_in},{ox_in},{o2_in}")
         

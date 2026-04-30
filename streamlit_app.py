import streamlit as st
import pandas as pd

# 1. إعدادات الهوية الملكية - نسخة القرن
st.set_page_config(page_title="SOVEREIGN LEDGER V100", page_icon="⚖️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1e293b 0%, #05080a 100%); color: white; }
    .match-card { background: rgba(255,255,255,0.03); border-left: 5px solid #ffd700; padding: 15px; border-radius: 10px; margin-bottom: 15px; }
    .score-tag { color: #00ff88; font-weight: 900; font-size: 22px; }
    .team-name { color: #ffffff; font-size: 16px; font-weight: bold; }
    
    /* ستايل الرابط الكاسر للحظر */
    .master-sync-link {
        display: block; width: 100%; background: #ffd700; color: #000 !important;
        text-align: center; padding: 20px; border-radius: 20px;
        font-weight: 900; text-decoration: none; margin-top: 25px;
        font-size: 16px; text-transform: uppercase;
        box-shadow: 0 10px 30px rgba(255, 215, 0, 0.3);
    }
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
st.markdown("<div style='text-align: center; margin-top:20px;'><h1 style='color:#ffd700; font-size:35px; letter-spacing:10px;'>SOVEREIGN</h1><p style='color:#00ff88; font-weight:900;'>V100.0 • UNBLOCKABLE MIRROR</p></div>", unsafe_allow_html=True)

selected_league = st.selectbox("🎯 مصدر البيانات:", ["tun", "pre", "gen"])

# إحداثيات البحث
c1, c2, c3 = st.columns(3)
with c1: o1_in = st.number_input("1", min_value=1.0, value=1.0, step=0.01)
with c2: ox_in = st.number_input("X", min_value=1.0, value=1.0, step=0.01)
with c3: o2_in = st.number_input("2", min_value=1.0, value=1.0, step=0.01)

if o1_in > 1.01 and ox_in > 1.01 and o2_in > 1.01:
    st.divider()
    # البحث المجهري الحقيقي (0.01)
    results = df[
        (df['league'] == selected_league) & 
        (df['o1'].between(o1_in - 0.01, o1_in + 0.01)) &
        (df['o2'].between(o2_in - 0.01, o2_in + 0.01))
    ]

    if not results.empty:
        st.success(f"✅ تم العثور على {len(results)} مواجهات حقيقية")
        
        # عرض النسب
        u25_pct = (results['u25'].sum() / len(results)) * 100
        st.metric("UNDER 2.5 REALITY", f"{int(u25_pct)}%")

        st.markdown("### 📂 السجلات التاريخية المكتشفة:")
        
        for index, row in results.iterrows():
            st.markdown(f"""
            <div class='match-card'>
                <span style='color:#888; font-size:11px;'>{row['date']}</span><br>
                <span class='team-name'>{row['home']} vs {row['away']}</span><br>
                <span style='color:#ffd700; font-size:13px;'>Odds: {row['o1']} - {row['ox']} - {row['o2']}</span><br>
                <span class='score-tag'>RESULT: {row['score']}</span>
            </div>
            """, unsafe_allow_html=True)
            
        # الرابط الذهبي الكاسر للحظر (استخدام target="_top")
        final_url = f"https://betexplorer.com{o1_in},{ox_in},{o2_in}"
        st.markdown(f'<a href="{final_url}" target="_top" class="master-sync-link">📡 فتح المصدر الأصلي (تجاوز الحظر)</a>', unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ هذا الأودز غير مسجل حالياً في الأرشيف.")
        final_url = f"https://betexplorer.com{o1_in},{ox_in},{o2_in}"
        st.markdown(f'<a href="{final_url}" target="_top" class="master-sync-link">🔍 بحث يدوي في BetExplorer</a>', unsafe_allow_html=True)

else:
    st.info("أدخل الأرقام الثلاثة لفتح سجلات الحقيقة.")
    

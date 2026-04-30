import streamlit as st
import pandas as pd

# 1. إعدادات قمرة القيادة
st.set_page_config(page_title="SOVEREIGN ARCHIVE SEARCH", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1e293b 0%, #05080a 100%); color: white; }
    div[data-testid="stMetricValue"] { color: #ffffff !important; font-size: 50px !important; font-weight: 900; }
    /* الجدول الذهبي الاحترافي */
    .archive-table { width: 100%; border-collapse: collapse; margin: 20px 0; border-radius: 15px; overflow: hidden; background: rgba(255, 255, 255, 0.02); border: 1px solid #ffd700; }
    .archive-table thead { background-color: #ffd700; }
    .archive-table th { padding: 12px; color: #000; font-weight: 900; text-transform: uppercase; }
    .archive-table td { padding: 15px; text-align: center; font-weight: 800; font-size: 19px; border-bottom: 1px solid rgba(255,255,255,0.05); }
    .score-res { color: #00d9ff !important; }
    .freq-res { color: #00ff88 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. جلب الأرشيف (الناقل الحقيقي)
@st.cache_data
def load_full_archive():
    try:
        return pd.read_csv('database.csv')
    except:
        return pd.DataFrame(columns=['league', 'o1', 'ox', 'o2', 'score', 'u25'])

df = load_full_archive()

# 3. بناء الواجهة
st.markdown("<div style='text-align: center; margin-top:30px;'><h1 style='color:#ffd700; font-size:32px; letter-spacing:5px;'>SOVEREIGN</h1><p style='color:#00ff88; font-weight:900;'>MAXIMUM HISTORICAL LEDGER • V96.0</p></div>", unsafe_allow_html=True)

league_map = {"🇹🇳 تونس • الرابطة الأولى": "tun", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 إنجلترا • الممتاز": "pre", "🌍 العالم • أرشيف عام": "gen"}
selected_league = st.selectbox("🎯 استدعاء أرشيف الدوري:", list(league_map.keys()))
lg_code = league_map[selected_league]

# إحداثيات البحث المجهري 0.01
c1, c2, c3 = st.columns(3)
with c1: o1_in = st.number_input("HOME", min_value=1.0, value=1.0, step=0.01)
with c2: ox_in = st.number_input("DRAW", min_value=1.0, value=1.0, step=0.01)
with c3: o2_in = st.number_input("AWAY", min_value=1.0, value=1.0, step=0.01)

if o1_in > 1.01 and ox_in > 1.01 and o2_in > 1.01:
    # البحث الحرفي داخل الـ Big Data
    hits = df[
        (df['league'] == lg_code) & 
        (df['o1'].between(o1_in - 0.01, o1_in + 0.01)) &
        (df['o2'].between(o2_in - 0.01, o2_in + 0.01))
    ]

    if not hits.empty:
        st.markdown(f"<p style='text-align:center; color:#00ff88; font-weight:900;'>✅ جرد ناجح: تم العثور على {len(hits)} تطابق في سجلات {selected_league}</p>", unsafe_allow_html=True)
        
        u25_pct = (hits['u25'].sum() / len(hits)) * 100
        
        col_a, col_b = st.columns(2)
        col_a.metric("U2.5 RECORD", f"{int(u25_pct)}%")
        col_b.metric("SAMPLES", len(hits))

        # جرد النتائج (الأمانة المطلقة في النقل)
        st.markdown("<br><h3 style='font-size:18px; color:#ffd700; text-align:center;'>📂 جرد السكور التاريخي الملتصق</h3>", unsafe_allow_html=True)
        counts = hits['score'].value_counts(normalize=True) * 100
        
        rows = ""
        for i, (score, freq) in enumerate(counts.items()):
            rows += f"<tr><td>#{i+1}</td><td class='score-res'>{score}</td><td class='freq-res'>{int(freq)}%</td></tr>"
        
        st.markdown(f'<table class="archive-table"><thead><tr><th>Rank</th><th>Result</th><th>Freq</th></tr></thead><tbody>{rows}</tbody></table>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ هذا الأودز لم يُسجل له تطابق حرفي في الأرشيف الحالي.")
    
    st.divider()
    st.link_button("📡 SYNC WITH BETEXPLORER SOURCE", f"https://betexplorer.com{o1_in},{ox_in},{o2_in}")

else:
    st.info("بانتظار اكتمال الأرقام لفتح الخزنة التاريخية.")
    

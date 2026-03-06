
import streamlit as st

# ၁။ App အပြင်အဆင်
st.set_page_config(page_title="The Golden Artisan", page_icon="⚒️", layout="centered")

# ၂။ Custom CSS
st.markdown("""
<style>
.main { background-color: #0e1117; }
.gold-text { color: #D4AF37; font-weight: bold; }
.cursive-font { font-family: cursive; color: #D4AF37; font-size: 45px; text-align: center; margin-top: 30px; }
.result-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border: 1px solid #D4AF37; color: #D4AF37; margin-bottom: 20px; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>✨ THE GOLDEN ARTISAN</h1>", unsafe_allow_html=True)

# တွက်ချက်မှုဆိုင်ရာ Function
def format_gold_weight(total_pe):
    k = int(total_pe // 16)
    p = int(total_pe % 16)
    rem_pe = total_pe % 1
    total_points = round(rem_pe * 80)
    y = int(total_points // 10)
    pt = int(total_points % 10)
    return f"{k} ကျပ်၊ {p} ပဲ၊ {y} ရွေး၊ {pt} Point"

# Tabs
tab1, tab2, tab3 = st.tabs(["💰 ရွှေ နှင့် ငွေ", "📏 အချိုးအစား", "🌍 ရွှေဈေး"])

with tab1:
    gold_price = st.number_input("အခေါက်ရွှေပေါက်ဈေး:", value=10900000)
    k1 = st.number_input("ရွှေကျပ်", value=0, key="k1")
    p1 = st.number_input("ရွှေပဲ", value=0, key="p1")
    purity = st.selectbox("ပဲရည်:", [16, 15, 14, 13], index=0)
    
    total_pe_val = (k1 * 16) + p1
    total_cost = (gold_price / 16) * (purity / 16) * total_pe_val
    st.markdown(f"<div class='result-card'><h3>စုစုပေါင်း: {int(total_cost):,} ကျပ်</h3></div>", unsafe_allow_html=True)

with tab2:
    base = st.number_input("အချိုး:", value=7.0)
    mul = st.number_input("အရှည်:", value=20.0)
    st.markdown(f"<div class='result-card'><h4>စုစုပေါင်းအရှည်: {base * mul}</h4></div>", unsafe_allow_html=True)

with tab3:
    w_price = st.number_input("Spot Gold (USD):", value=2100.0)
    u_rate = st.number_input("Dollar Rate:", value=4800)
    mm_gold = (w_price * u_rate) / 1.875
    st.metric("မြန်မာ့အခေါက်ရွှေဈေး", f"{int(mm_gold):,} ကျပ်")

st.markdown("<div class='cursive-font'>MinThitSarAung</div>", unsafe_allow_html=True)

import streamlit as st

# ၁။ App အပြင်အဆင်
st.set_page_config(page_title="မြန်မာ့ရွှေပန်းတိမ်သုံး", page_icon="⚒️", layout="centered")

# ၂။ Custom CSS (အမှားကင်းစင်အောင် ပြင်ဆင်ထားသည်)
st.markdown("""
<style>
.main { background-color: #0e1117; }
.result-card { background-color: #1a1a1a; padding: 20px; border-radius: 15px; border: 1px solid #D4AF37; color: #D4AF37; margin-bottom: 20px; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>✨ မြန်မာ့ရွှေပန်းတိမ်သုံး</h1>", unsafe_allow_html=True)

# တွက်ချက်မှုဆိုင်ရာ Function
def format_gold_weight(total_pe):
    k = int(total_pe // 16)
    p = int(total_pe % 16)
    rem_pe = total_pe % 1
    total_points = round(rem_pe * 80)
    y = int(total_points // 10)
    pt = int(total_points % 10)
    pt_str = f"{pt} Point"
    if pt == 5: pt_str = "5 Point (တစ်ခြမ်း)"
    return f"{k} ကျပ်၊ {p} ပဲ၊ {y} ရွေး၊ {pt_str}"

# Tabs များ
tab1, tab2, tab3 = st.tabs(["💰 ရွှေ နှင့် ငွေ", "📏 အချိုးအစား", "🌍 ကမ္ဘာ့ရွှေဈေး"])

with tab1:
    gold_price = st.number_input("အခေါက်ရွှေပေါက်ဈေး (ကျပ်):", value=10900000, step=10000)
    sub1, sub2 = st.tabs(["ရွှေမှ ငွေတွက်", "ငွေမှ ရွှေတွက်"])
    
    with sub1:
        c1, c2, c3, c4 = st.columns(4)
        k1 = c1.number_input("ကျပ်", value=0, key="k1")
        p1 = c2.number_input("ပဲ", value=0, key="p1")
        y1 = c3.number_input("ရွေး", value=0, key="y1")
        pt1 = c4.number_input("Point", value=0, key="pt1")
        purity = st.selectbox("ပဲရည်:", [16, 15, 14.2, 14, 13], index=0)
        
        # အလျော့တွက်
        st.write("အလျော့တွက်")
        wk1 = st.number_input("အလျော့ ကျပ်", value=0, key="wk1")
        wp1 = st.number_input("အလျော့ ပဲ", value=0, key="wp1")
        
        total_pe_val = (k1 * 16) + p1 + (y1 / 8) + (pt1 / 80)
        total_w_pe = (wk1 * 16) + wp1
        total_cost = (gold_price / 16) * (purity / 16) * (total_pe_val + total_w_pe)
        st.markdown(f"<div class='result-card'>စုစုပေါင်းကျသင့်ငွေ: <b>{int(total_cost):,}</b> ကျပ်</div>", unsafe_allow_html=True)

    with sub2:
        budget = st.number_input("ရှိသောငွေ (ကျပ်):", value=1000000)
        st.markdown(f"<div class='result-card'>အလျော့တွက်နုတ်ပြီး ရရှိမည့်ရွှေ: <br><b>တွက်ချက်ရန် Budget ထည့်ပါ</b></div>", unsafe_allow_html=True)

with tab2:
    base = st.number_input("အချိုး:", value=7.0)
    mul = st.number_input("အရှည်:", value=20.0)
    st.markdown(f"<div class='result-card'>စုစုပေါင်းအရှည်: <b>{base * mul:.1f} လက်မ</b></div>", unsafe_allow_html=True)

with tab3:
    w_price = st.number_input("Spot Gold (USD):", value=2100.0)
    u_rate = st.number_input("Dollar Rate (MMK):", value=4800)
    mm_gold = (w_price * u_rate) / 1.875
    st.metric("မြန်မာ့အခေါက်ရွှေဈေး (ခန့်မှန်း)", f"{int(mm_gold):,} ကျပ်")

st.markdown("<p style='text-align: center; color: #D4AF37;'>App by MinThitSarAung</p>", unsafe_allow_html=True)

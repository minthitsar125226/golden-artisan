import streamlit as st

# ၁။ App အပြင်အဆင်နှင့် နာမည်
st.set_page_config(page_title="မြန်မာ့ရွှေပန်းတိမ်သုံး", page_icon="⚒️", layout="centered")

# ၂။ Custom CSS (UI လှပစေရန်နှင့် Font များ ထည့်သွင်းရန်)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    <style>
    .main { background-color: #0e1117; }
    .gold-text { color: #D4AF37; font-weight: bold; }
    .cursive-font { font-family: 'Dancing Script', cursive; color: #D4AF37; font-size: 35px; text-align: center; margin-top: 30px; }
    .result-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border: 1px solid #D4AF37; color: #D4AF37; margin-bottom: 20px; text-align: center;}
    .stNumberInput label, .stSelectbox label { color: #D4AF37 !important; font-weight: bold; }
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
    if pt == 5:
        pt_str = "5 Point (တစ်ခြမ်း)"
    return f"{k} ကျပ်၊ {p} ပဲ၊ {y} ရွေး၊ {pt_str}"

# ၃။ Tabs များ ခွဲခြားခြင်း
tab1, tab2, tab3, tab4, = st.tabs(["💰 ရွှေ နှင့် ငွေ", "📏 အချိုးအစားတွက်စက်", "🌍 ကမ္ဘာ့ရွှေဈေး"])

with tab1:
    st.subheader("💰 ရွှေ နှင့် ငွေ လဲလှယ်ခြင်း")
    gold_price = st.number_input("ယနေ့ အခေါက်ရွှေပေါက်ဈေး (ကျပ်):", value=10900000, step=10000)
    
    sub1, sub2 = st.tabs(["ရွှေမှ ငွေတွက်ရန်", "ငွေမှ ရွှေတွက်ရန်"])
    
    with sub1:
        st.write("**ရွှေအသား အလေးချိန်**")
        c1, c2, c3, c4 = st.columns(4)
        k1 = c1.number_input("ကျပ်", value=0, key="k1")
        p1 = c2.number_input("ပဲ", value=0, max_value=15, key="p1")
        y1 = c3.number_input("ရွေး", value=0, max_value=7, key="y1")
        pt1 = c4.number_input("Point", value=0, max_value=9, key="pt1")
        
        st.write("**အလျော့တွက် အလေးချိန်**")
        wc1, wp1, wy1, wpt1 = st.columns(4)
        wk1 = wc1.number_input("ကျပ်", value=0, key="wk1")
        wp1_v = wp1.number_input("ပဲ", value=0, key="wp1")
        wy1_v = wy1.number_input("ရွေး", value=0, key="wy1")
        wpt1_v = wpt1.number_input("Point", value=0, key="wpt1")
        
        purity = st.selectbox("ရွှေအရည်အသွေး (ပဲရည်):", [16, 15, 14.2, 14, 13], index=0)
        
        total_pe_val = (k1 * 16) + p1 + (y1 / 8) + (pt1 / 80)
        total_w_pe_val = (wk1 * 16) + wp1_v + (wy1_v / 8) + (wpt1_v / 80)
        
        total_cost = (gold_price / 16) * (purity / 16) * (total_pe_val + total_w_pe_val)
        st.markdown(f"<div class='result-card'><h3>စုစုပေါင်းကျသင့်ငွေ: {int(total_cost):,} ကျပ်</h3></div>", unsafe_allow_html=True)

    with sub2:
        budget = st.number_input("ရှိသောငွေ (ကျပ်):", value=1000000, step=10000)
        st.write("**နုတ်ယူမည့် အလျော့တွက်**")
        wc2, wp2, wy2, wpt2 = st.columns(4)
        wk2 = wc2.number_input("ကျပ်", value=0, key="wk2")
        wp2_v = wp2.number_input("ပဲ", value=0, key="wp2")
        wy2_v = wy2.number_input("ရွေး", value=0, key="wy2")
        wpt2_v = wpt2.number_input("Point", value=0, key="wpt2")
        
        purity2 = st.selectbox("ဝယ်ယူမည့် ပဲရည်:", [16, 15, 14.2, 14, 13], index=0, key="pur2")
        
        one_pe_price = (gold_price / 16) * (purity2 / 16)
        total_pe_possible = budget / one_pe_price if one_pe_price > 0 else 0
        wastage_pe = (wk2 * 16) + wp2_v + (wy2_v / 8) + (wpt2_v / 80)
        actual_gold_pe = total_pe_possible - wastage_pe if total_pe_possible > wastage_pe else 0
        
        st.markdown(f"<div class='result-card'><h3>ရရှိမည့်ရွှေအသား: <br>{format_gold_weight(actual_gold_pe)}</h3></div>", unsafe_allow_html=True)

with tab2:
    st.subheader("📏 ပန်းတိမ်သုံး အလျားနှင့် အလေးချိန်")
    st.markdown("#### ၁။ အလျားမြှောက်ခြင်း")
    col_a, col_b = st.columns(2)
    base_unit = col_a.number_input("အချိုး (ဥပမာ- ၇):", value=7.0)
    multiplier = col_b.number_input("မြှောက်မည့် အရှည် (ဥပမာ- ၂၀):", value=20.0)
    total_inches = base_unit * multiplier
    ft = int(total_inches // 12)
    rem_in = total_inches % 12
    st.markdown(f"<div class='result-card'><h4>စုစုပေါင်းအရှည်: {ft} ပေ {rem_in:.1f} လက်မ</h4></div>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("#### ၂။ လက်မအလိုက် ရွှေအလေးချိန်")
    col_c, col_d, col_e = st.columns(3)
    inch_in = col_c.number_input("အရှည် (လက်မ):", value=20.0, key="inch_in")
    y_per_in = col_d.number_input("၁ လက်မစာ ရွေး:", value=0, key="y_per_in")
    pt_per_in = col_e.number_input("၁ လက်မစာ Point:", value=1, key="pt_per_in")
    total_pe_inch = inch_in * ((y_per_in / 8) + (pt_per_in / 80))
    st.markdown(f"<div class='result-card'><h4>ရလဒ် အလေးချိန်: <br>{format_gold_weight(total_pe_inch)}</h4></div>", unsafe_allow_html=True)

with tab3:
    st.subheader("🌍 World Gold to Myanmar")
    w_price = st.number_input("Spot Gold (USD):", value=2100.0)
    u_rate = st.number_input("Dollar Rate (MMK):", value=4800)
    mm_gold = (w_price * u_rate) / 1.875
    st.metric("မြန်မာ့အခေါက်ရွှေဈေး (ခန့်မှန်း)", f"{int(mm_gold):,} ကျပ်")

# --- Tab 4: လက်စွပ်တိုင်း (Ring Sizer) ---
with tab4:
    st.subheader("💍 လက်စွပ်တိုင်း တွက်ချက်ခြင်း")
    
    # Unit ပြောင်းလဲခြင်း (mm to inch)
    st.markdown("#### ၁။ အတိုင်းအတာ ပြောင်းလဲခြင်း")
    mm_input = st.number_input("လုံးပတ် (မီလီမီတာ - mm):", value=50.0, step=0.1)
    inch_val = mm_input / 25.4
    st.info(f"ရလဒ် (လက်မ - inch): {inch_val:.2f} လက်မ")
    
    st.divider()
    
    # လက်စွပ်တိုင်း ဇယားရှာဖွေခြင်း
    st.markdown("#### ၂။ လက်စွပ် နံပါတ်ရှာရန်")
    user_inch = st.slider("သင့်လက်စွပ် လုံးပတ် (လက်မ):", 1.5, 2.5, 1.97, 0.01)
    
    # ဇယားအတိုင်း ခန့်မှန်းတွက်ချက်ခြင်း
    if user_inch < 1.75: ring_no = 4
    elif user_inch < 1.85: ring_no = 6
    elif user_inch < 1.93: ring_no = 8
    elif user_inch < 2.01: ring_no = 10
    elif user_inch < 2.09: ring_no = 12
    elif user_inch < 2.17: ring_no = 14
    elif user_inch < 2.24: ring_no = 16
    else: ring_no = 18
    
    st.markdown(f"<div class='result-card'><h3>ခန့်မှန်း လက်စွပ်နံပါတ်: {ring_no}</h3></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='cursive-font'>App by MinThitSarAung</div>", unsafe_allow_html=True)

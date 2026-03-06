import streamlit as st

# ၁။ App အပြင်အဆင် (Error ကင်းစင်စေရန် ပထမဆုံးစာကြောင်းမှစ၍ အကွာအဝေးညှိထားပါသည်)
st.set_page_config(page_title="The Golden Artisan - MinThitSarAung", page_icon="⚒️", layout="centered")

# ၂။ Custom CSS (ပန်းတိမ်သုံး Gold Style)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
    <style>
    .main { background-color: #0e1117; }
    .gold-text { color: #D4AF37; font-weight: bold; }
    .cursive-font { font-family: 'Dancing Script', cursive; color: #D4AF37; font-size: 45px; text-align: center; margin-top: 30px; text-shadow: 2px 2px 5px rgba(0,0,0,0.5); }
    .result-card { background-color: #1a1a1a; padding: 25px; border-radius: 15px; border: 1px solid #D4AF37; color: #D4AF37; margin-bottom: 20px; text-align: center;}
    .stNumberInput label, .stSelectbox label, .stRadio label { color: #D4AF37 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>✨ THE GOLDEN ARTISAN</h1>", unsafe_allow_html=True)

# --- တွက်ချက်မှုဆိုင်ရာ Function (၁ ပဲ = ၈ ရွေး = ၈၀ Point) ---
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
tab1, tab2, tab3 = st.tabs(["💰 ရွှေ နှင့် ငွေ", "📏 အချိုးအစားတွက်စက်", "🌍 ကမ္ဘာ့ရွှေဈေး"])

# --- Tab 1: ရွှေ နှင့် ငွေ (ပုံမှန်ပဲရည်ရွေးစနစ် + အလျော့တွက်ပါဝင်သည်) ---
with tab1:
    st.subheader("💰 ရွှေ နှင့် ငွေ လဲလှယ်ခြင်း")
    gold_price = st.number_input("ယနေ့ အခေါက်ရွှေပေါက်ဈေး (ကျပ်):", value=10900000, step=10000)
    
    sub1, sub2 = st.tabs(["ရွှေမှ ငွေတွက်ရန်", "ငွေမှ ရွှေတွက်ရန်"])
    
    with sub1:
        st.write("**ရွှေအသား အလေးချိန်**")
        c1, c2, c3, c4 = st.columns(4)
        with c1: k1 = st.number_input("ကျပ်", value=0, key="k1")
        with c2: p1 = st.number_input("ပဲ", value=0, max_value=15, key="p1")
        with c3: y1 = st.number_input("ရွေး", value=0, max_value=7, key="y1")
        with c4: pt1 = st.number_input("Point", value=0, max_value=9, key="pt1")
        
        st.write("**အလျော့တွက် အလေးချိန်**")
        wc1, wp1, wy1, wpt1 = st.columns(4)
        with wc1: wk1 = st.number_input("ကျပ်", value=0, key="wk1")
        with wp1: wp1_v = st.number_input("ပဲ", value=0, key="wp1")
        with wy1: wy1_v = st.number_input("ရွေး", value=0, key="wy1")
        with wpt1: wpt1_v = st.number_input("Point", value=0, key="wpt1")
        
        purity = st.selectbox("ရွှေအရည်အသွေး (ပဲရည်):", [16, 15, 14.2, 14, 13], index=0)
        
        total_pe_val = (k1 * 16) + p1 + (y1 / 8) + (pt1 / 80)
        total_w_pe_val = (wk1 * 16) + wp1_v + (wy1_v / 8) + (wpt1_v / 80)
        
        total_cost = (gold_price / 16) * (purity / 16) * (total_pe_val + total_w_pe_val)
        st.markdown(f"<div class='result-card'><h3>စုစုပေါင်းကျသင့်ငွေ: {int(total_cost):,} ကျပ်</h3></div>", unsafe_allow_html=True)

    with sub2:
        budget = st.number_input("ရှိသောငွေ (ကျပ်):", value=1000000, step=10000)
        
        st.write("**နုတ်ယူမည့် အလျော့တွက်**")
        wc2, wp2, wy2, wpt2 = st.columns(4)
        with wc2: wk2 = st.number_input("ကျပ်", value=0, key="wk2")
        with wp2: wp2_v = st.number_input("ပဲ", value=0, key="wp2")
        with wy2: wy2_v = st.number_input("ရွေး", value=0, key="wy2")
        with wpt2: wpt2_v = st.number_input("Point", value=0, key="wpt2")
        
        purity2 = st.selectbox("ဝယ်ယူမည့် ပဲရည်:", [16, 15, 14.2, 14, 13], index=0, key="pur2")
        
        one_pe_price = (gold_price / 16) * (purity2 / 16)
        total_pe_possible = budget / one_pe_price if one_pe_price > 0 else 0
        wastage_pe = (wk2 * 16) + wp2_v + (wy2_v / 8) + (wpt2_v / 80)
        actual_gold_pe = total_pe_possible - wastage_pe if total_pe_possible > wastage_pe else 0
        
        st.markdown(f"<div class='result-card'><h3>အလျော့တွက်နုတ်ပြီး ရရှိမည့်ရွှေအသား: <br>{format_gold_weight(actual_gold_pe)}</h3></div>", unsafe_allow_html=True)

# --- Tab 2: အချိုးအစား (၁၀ Point = ၁ ရွေး) ---
with tab2:
    st.subheader("📏 ပန်းတိမ်သုံး အလျားနှင့် အလေးချိန်")
    st.markdown("#### ၁။ အလျားမြှောက်ခြင်း")
    col_a, col_b = st.columns(2)
    with col_a:
        base_unit = st.number_input("အချိုး (ဥပမာ- ၇):", value=7.0)
    with col_b:
        multiplier = st.number_input("မြှောက်မည့် အရှည် (ဥပမာ- ၂၀):", value=20.0)
    
    total_inches = base_unit * multiplier
    ft = int(total_inches // 12)
    rem_in = total_inches % 12
    st.markdown(f"<div class='result-card'><h4>စုစုပေါင်းအရှည်: {ft} ပေ {rem_in:.1f} လက်မ</h4></div>", unsafe_allow_html=True)

    st.divider()

    st.markdown("#### ၂။ လက်မအလိုက် ရွှေအလေးချိန်")
    col_c, col_d, col_e = st.columns(3)
    with col_c: inch_in = st.number_input("အရှည် (လက်မ):", value=20.0, key="inch_in")
    with col_d: y_per_in = st.number_input("၁ လက်မစာ ရွေး:", value=0, key="y_per_in")
    with col_e: pt_per_in = st.number_input("၁ လက်မစာ Point:", value=1, key="pt_per_in")
    
    # ၁ ပဲ = ၈၀ Point ဖြစ်သောကြောင့် (ရွေး/၈ + Point/၈၀)
    total_pe_inch = inch_in * ((y_per_in / 8) + (pt_per_in / 80))
    st.markdown(f"<div class='result-card'><h4>ရလဒ် အလေးချိန်: <br>{format_gold_weight(total_pe_inch)}</h4></div>", unsafe_allow_html=True)

# --- Tab 3: ကမ္ဘာ့ရွှေဈေး ---
with tab3:
    st.subheader("🌍 World Gold to Myanmar")
    w_price = st.number_input("Spot Gold (USD):", value=2100.0)
    u_rate = st.number_input("Dollar Rate (MMK):", value=4800)
    mm_gold = (w_price * u_rate) / 1.875
    st.metric("မြန်မာ့အခေါက်ရွှေဈေး (ခန့်မှန်း)", f"{int(mm_gold):,} ကျပ်")

# --- Footer (Pro Signature) ---
st.markdown("---")
st.markdown("<div class='cursive-font'>App by MinThitSarAung</div>", unsafe_allow_html=True)

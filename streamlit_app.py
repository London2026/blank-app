import streamlit as st
from PIL import Image

st.set_page_config(page_title="PropertyPost AI", layout="wide")
st.title("📱 PropertyPost AI")
st.markdown("*Perfect 15s Instagram Reels - Screen Record Ready*")

# Branding
st.sidebar.header("🏢 Agency")
agent_name = st.sidebar.text_input("Agency Name", "Prime Properties")

# Compact form
st.subheader("Quick Reel Generator")
col1, col2, col3 = st.columns(3)
with col1:
    address = st.text_input("Address", "123 High St, London")
with col2:
    price = st.number_input("Price", 850000, 100000, 5000000, 50000)
with col3:
    beds = st.number_input("Beds", 1, 8, 3)

feature = st.text_input("Feature", "South garden | No chain")

# Hero photo
photo = st.file_uploader("Hero Photo", type=['jpg','jpeg','png'])

# Animation CSS + Reel
if st.button("🎥 GENERATE REEL", type="primary", use_container_width=True):
    if photo:
        col1, col2 = st.columns([1,3])
        with col1:
            img = Image.open(photo).resize((280, 480))
            st.image(img, caption="Hero", use_column_width=True)
        
        with col2:
            st.markdown("""
            <style>
            @keyframes boom {0% {transform: scale(0.2); opacity:0;} 70% {transform: scale(1.3);} 100% {transform: scale(1); opacity:1;}}
            @keyframes slide {0% {transform: translateX(100%); opacity:0;} 100% {transform: translateX(0); opacity:1;}}
            .reel {width:360px; height:640px; background:linear-gradient(#0f0f23,#1a1a3e); border-radius:28px; padding:50px 25px; margin:auto; box-shadow:0 25px 50px #0004;}
            .price-boom {font-size:100px; color:#fff; font-weight:800; text-align:center; margin:25px 0; animation:boom 2s ease-out; text-shadow:2px 2px 8px #0008; letter-spacing:2px;}
            .beds-slide {font-size:65px; color:#00d4ff; font-weight:700; text-align:center; margin:15px 0; animation:slide 1.5s 0.7s both;}
            .feature {font-size:38px; color:#fff; text-align:center; margin:20px 0;}
            .agency {font-size:32px; color:#ffd700; font-weight:700; text-align:center; margin:15px 0; text-shadow:0 0 15px #ffd70050;}
            .cta {background:linear-gradient(45deg,#ff4757,#ff6b7a); color:white; border:none; padding:15px 40px; font-size:26px; font-weight:700; border-radius:40px; cursor:pointer; margin:25px auto; display:block; box-shadow:0 10px 30px #ff475740;}
            </style>
            <div class="reel">
                <div class="price-boom">""" + f"£{price:,}" + """</div>
                <div class="beds-slide">""" + f"{beds} BED" + """</div>
                <div class="feature">""" + feature + """</div>
                <div class="agency">""" + agent_name + """</div>
                <button class="cta">📞 BOOK NOW</button>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("🎉 REEL READY!")
            st.info("""
            **📱 POST NOW:**
            1. Screen Record (15s)
            2. Instagram Reels → Upload
            3. Copy caption below
            """)
            
            caption = f"""🏠 {address} | £{price:,} | {beds} Beds
{feature}

📲 {agent_name} | Views today!
#Property #London #Reels #ForSale"""
            st.text_area("Instagram Caption", caption, height=120)
    else:
        st.warning("📸 Upload photo")

st.markdown("---")
st.caption("Screen record → Post → Sell!")

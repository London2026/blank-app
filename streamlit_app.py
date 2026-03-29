import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="PropertyPost AI", initial_sidebar_state="expanded")
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Arial Black', Arial, sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📱 PropertyPost AI")
st.markdown("***Instagram-ready Reels in 15s***")

# Perfect Instagram CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
    
    .instagram-reel {{
        width: 360px !important;
        height: 640px !important;
        margin: 20px auto !important;
        background: linear-gradient(180deg, #000428 0%, #004e92 100%) !important;
        border-radius: 24px !important;
        padding: 40px 20px 30px !important;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4) !important;
        position: relative !important;
        overflow: hidden !important;
        font-family: 'Poppins', sans-serif !important;
    }}
    
    @keyframes priceExplode {{
        0% {{ transform: scale(0.2) rotate(-180deg); opacity: 0; }}
        60% {{ transform: scale(1.3); }}
        100% {{ transform: scale(1) rotate(0deg); opacity: 1; }}
    }}
    
    @keyframes bedSlide {{
        0% {{ transform: translateX(120%) skew(-20deg); opacity: 0; }}
        100% {{ transform: translateX(0) skew(0); opacity: 1; }}
    }}
    
    @keyframes featureGlow {{
        0%, 100% {{ text-shadow: 0 0 20px #00d4ff; }}
        50% {{ text-shadow: 0 0 40px #00d4ff, 0 0 60px #00d4ff; }}
    }}
    
    .price-boom {{
        font-size: 100px !important;
        font-weight: 700 !important;
        color: #fff !important;
        text-align: center !important;
        margin: 20px 0 !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8) !important;
        animation: priceExplode 2s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
        letter-spacing: 4px !important;
    }}
    
    .beds-animate {{
        font-size: 70px !important;
        color: #00d4ff !important;
        font-weight: 700 !important;
        text-align: center !important;
        margin: 15px 0 !important;
        animation: bedSlide 1.8s ease-out 0.5s both !important;
    }}
    
    .feature-glow {{
        font-size: 45px !important;
        color: #fff !important;
        text-align: center !important;
        margin: 20px 0 !important;
        animation: featureGlow 2s infinite 1.2s !important;
    }}
    
    .agency-flash {{
        font-size: 38px !important;
        color: #ffd700 !important;
        text-align: center !important;
        font-weight: 700 !important;
        text-shadow: 0 0 15px #ffd700 !important;
        animation: featureGlow 2.5s infinite 1.8s !important;
    }}
    
    .cta-button {{
        background: linear-gradient(45deg, #ff6b6b, #feca57) !important;
        color: white !important;
        border: none !important;
        padding: 15px 40px !important;
        font-size: 28px !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        cursor: pointer !important;
        display: block !important;
        margin: 25px auto !important;
        box-shadow: 0 10px 30px rgba(255,107,107,0.4) !important;
        transition: all 0.3s !important;
    }}
    
    .cta-button:hover {{
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 40px rgba(255,107,107,0.6) !important;
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar branding
st.sidebar.header("🏢 Agency")
agent_name = st.sidebar.text_input("Your Agency", "Prime Properties")
st.sidebar.markdown("---")
st.sidebar.info("**Pro Reels:** £29/month")

# Main form
col1, col2 = st.columns([1,1])
with col1:
    st.subheader("📍 Property Details")
    address = st.text_input("Full Address", "123 High Street, London SW1A 1AA")
    price = st.number_input("Asking Price", value=850000, step=25000)
with col2:
    beds = st.number_input("Bedrooms", value=3, min_value=1)
    feature = st.text_input("Hero Feature", "South-facing garden")

# Hero photo
st.subheader("📸 Hero Photo")
photo = st.file_uploader("Best property image", type=['jpg','jpeg','png'])

# GENERATE BUTTON
if st.button("🎥 GENERATE REEL", type="primary", use_container_width=True, help="Creates Instagram-ready animation"):
    if photo:
        # Display hero image
        img = Image.open(photo).resize((300, 500), Image.Resampling.LANCZOS)
        st.image(img, caption="Hero shot", use_column_width="auto")
        
        # INSTAGRAM REEL ANIMATION
        st.markdown(f"""
        <div class="instagram-reel">
            <div class="price-boom">£{price:,}</div>
            <div class="beds-animate">{beds} BED MASTERPIECE</div>
            <div class="feature-glow">{feature}</div>
            <div class="agency-flash">{agent_name}</div>
            <button class="cta-button" onclick="alert('📱 Book viewing now!')">📞 VIEWING</button>
            <div style="font-size: 32px; color: #60a5fa; text-align: center; margin-top: 20px;">
                SWIPE UP ⬆️
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Screen record instructions
        st.success("🎉 **REEL READY!**")
        st.markdown("""
        **📱 Post instructions:**
        1. **Screen Record** (iPhone: Control Center → Record)
        2. Record 15 seconds of animation above
        3. **Instagram Reels** → Upload recording
        4. Copy caption below
        
        **💡 Pro tip:** Add your voiceover "Dream home alert!"
        """)
        
        # PERFECT CAPTION
        caption = f"""🏠 **{address}** | £{price:,} | {beds} Beds
✨ {feature}

Prime location • Modern luxury • Must view!
📲 {agent_name} • 24hr viewings

#PropertyForSale #LondonEstateAgent #Reels #LuxuryHomes
#InvestmentProperty #SW1 #ForSale"""

        st.code(caption)
        
        # Share buttons
        col1, col2 = st.columns(2)
        col1.metric("Instagram", "15s Reel")
        col2.metric("TikTok", "Ready!")
        
    else:
        st.warning("📸 **Upload hero photo first**")

# Phone frame mockup
st.markdown("""
<div style="text-align: center; margin: 50px 0;">
    <div style="display: inline-block; background: #000; 
                padding: 25px; border-radius: 45px; 
                box-shadow: 0 25px 50px rgba(0,0,0,0.5);">
        <div style="background: #111; border-radius: 35px; 
                    padding: 70px 25px 50px; position: relative;
                    width: 360px; height: 640px; margin: auto;">
            <div style="position: absolute; top: 25px; left: 50%; 
                        transform: translateX(-50%); width: 160px; 
                        height: 8px; background: #333; border-radius: 4px;"></div>
            <div style="color: #aaa; font-size: 20px; text-align: center; margin-top: 30px;">
                📱 YOUR INSTAGRAM REEL
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("*Screen record → Post → Sell! | Pro MP4 export coming*")

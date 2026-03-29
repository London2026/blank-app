import streamlit as st
from PIL import Image

st.set_page_config(page_title="PropertyPost AI", layout="wide")
st.title("📱 PropertyPost AI")
st.markdown("**15s Instagram Reels - Screen Record Ready**")

# PRO Instagram CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    
* {{
    font-family: 'Poppins', sans-serif !important;
}}

.reel-phone {{
    max-width: 400px !important;
    margin: 30px auto !important;
    position: relative !important;
}}

.reel-screen {{
    width: 360px !important;
    height: 640px !important;
    background: linear-gradient(180deg, #0f0f23 0%, #1a1a3e 50%, #2d1b69 100%) !important;
    border-radius: 28px !important;
    padding: 50px 25px 40px !important;
    margin: auto !important;
    box-shadow: 
        0 25px 50px rgba(0,0,0,0.6),
        inset 0 1px 0 rgba(255,255,255,0.1) !important;
    overflow: hidden !important;
    position: relative !important;
}}

.reel-screen::before {{
    content: '';
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 140px;
    height: 6px;
    background: linear-gradient(90deg, #333, #555, #333);
    border-radius: 3px;
}}

@keyframes priceBlast {{
    0% {{ 
        transform: scale(0.1) rotate(360deg); 
        opacity: 0; 
        filter: blur(20px);
    }}
    70% {{ 
        transform: scale(1.2); 
        filter: blur(0px);
    }}
    100% {{ 
        transform: scale(1) rotate(0deg); 
        opacity: 1;
    }}
}}

@keyframes bedsRush {{
    0% {{ 
        transform: translateX(150%) rotate(-10deg); 
        opacity: 0;
    }}
    100% {{ 
        transform: translateX(0) rotate(0deg); 
        opacity: 1;
    }}
}}

@keyframes featurePulse {{
    0%, 100% {{ 
        text-shadow: 0 0 20px #00d4ff, 0 0 30px #00d4ff;
        transform: scale(1);
    }}
    50% {{ 
        text-shadow: 0 0 40px #00d4ff, 0 0 60px #00d4ff;
        transform: scale(1.05);
    }}
}}

@keyframes agencyShine {{
    0%, 100% {{ color: #ffd700; }}
    50% {{ color: #fff200; text-shadow: 0 0 30px #ffd700; }}
}}

.price-explosion {{
    font-size: 110px !important;
    font-weight: 800 !important;
    color: #fff !important;
    line-height: 0.9 !important;
    margin: 30px 0 !important;
    text-align: center !important;
    text-shadow: 0 4px 12px rgba(0,0,0,0.8) !important;
    letter-spacing: 3px !important;
    animation: priceBlast 2.2s cubic-bezier(0.25,0.46,0.45,0.94) !important;
}}

.beds-storm {{
    font-size: 75px !important;
    font-weight: 700 !important;
    background: linear-gradient(45deg, #00d4ff, #0099cc) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    margin: 20px 0 !important;
    text-align: center !important;
    animation: bedsRush 1.5s ease-out 0.8s both !important;
}}

.feature-wave {{
    font-size: 42px !important;
    color: #fff !important;
    text-align: center !important;
    margin: 25px 0 !important;
    animation: featurePulse 2s infinite 1.5s !important;
    font-weight: 600 !important;
}}

.agency-gold {{
    font-size: 36px !important;
    font-weight: 700 !important;
    color: #ffd700 !important;
    text-align: center !important;
    margin: 20px 0 !important;
    text-shadow: 0 2px 10px rgba(255,215,0,0.5) !important;
    animation: agencyShine 2s infinite 2s !important;
}}

.cta-fire {{
    background: linear-gradient(45deg, #ff4757, #ff6b7a) !important;
    color: white !important;
    border: none !important;
    padding: 18px 50px !important;
    font-size: 32px !important;
    font-weight: 700 !important;
    border-radius: 50px !important;
    cursor: pointer !important;
    display: block !important;
    margin: 30px auto 20px !important;
    box-shadow: 0 12px 35px rgba(255,71,87,0.4) !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
}}

.cta-fire:hover {{
    transform: translateY(-5px) scale(1.05) !important;
    box-shadow: 0 20px 45px rgba(255,71,87,0.6) !important;
}}
</style>
""", unsafe_allow_html=True)

# Branding sidebar
with st.sidebar:
    st.header("🏢 Agency")
    agent_name = st.text_input("Agency Name", "Prime Properties London")
    st.markdown("---")
    st.info("**Screen record 15s → Post!**")

# Compact form (single column)
st.subheader("🔥 Quick Reel Generator")
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    address = st.text_input("Property Address", "123 High Street, London SW1")
with col2:
    price = st.number_input("Price", value=850000, step=50000, format="£%,d")
with col3:
    beds = st.number_input("Beds", value=3, min_value=1)

feature = st.text_input("Key Feature", "South-facing garden | No chain")

# Single hero photo
photo = st.file_uploader("📸 Hero Photo (best angle)", type=['jpg','jpeg','png'])

# GENERATE
if st.button("🎥 CREATE REEL", type="primary", use_container_width=True):
    if photo:
        col1, col2 = st.columns([1, 3])
        with col1:
            img = Image.open(photo).resize((250, 420), Image.Resampling.LANCZOS)
            st.image(img, caption="Hero", use_column_width=True)
        
        with col2:
            st.markdown(f"""
            <div class="reel-phone">
                <div class="reel-screen">
                    <div class="price-explosion">£{price:,}</div>
                    <div class="beds-storm">{beds} BED</div>
                    <div class="feature-wave">{feature}</div>
                    <div class="agency-gold">{agent_name}</div>
                    <button class="cta-fire">📞 BOOK NOW</button>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("🎉 **15s REEL READY!**")
            st.markdown("""
            **📱 INSTANT POST:**
            1. **Screen Record** (Control Center → Circle icon)
            2. Record animation above (15 seconds)
            3. **Instagram Reels** → Upload → Add music
            4. Copy caption below
            
            **Pro result guaranteed!** 🔥
            """)
            
            caption = f"""🏠 **{address}** | £{price:,}
{beds} Beds | {feature}

🔥 UNDER OFFER FAST! 
📲 {agent_name}

#PropertyForSale #London #Reels #EstateAgent"""
            
            st.code(caption, language=None)
            
    else:
        st.warning("📸 Upload 1 hero photo")

st.markdown("---")
st.caption("*Screen record → Instagram → Leads! | Pro MP4 export soon*")

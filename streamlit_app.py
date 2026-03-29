import streamlit as st
from PIL import Image
import io

st.set_page_config(layout="wide", page_title="PropertyPost AI Pro")
st.title("🎬 PropertyPost AI Pro")
st.markdown("**Motion graphics Reels for estate agents**")

# Custom CSS animations
st.markdown("""
<style>
    @keyframes pricePop {
        0% { transform: scale(0.3); opacity: 0; }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); opacity: 1; }
    }
    @keyframes bedSlide {
        0% { transform: translateX(100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    @keyframes agentGlow {
        0%, 100% { text-shadow: 0 0 20px #10b981; }
        50% { text-shadow: 0 0 40px #10b981; }
    }
    .price-hero {
        font-size: 140px !important; 
        color: white !important; 
        font-weight: bold !important;
        text-shadow: 3px 3px 6px black !important;
        animation: pricePop 2s ease-out !important;
        text-align: center !important;
        margin: 20px 0 !important;
    }
    .beds-slide {
        font-size: 90px !important;
        color: #10b981 !important;
        font-weight: bold !important;
        animation: bedSlide 1.5s ease-out !important;
        text-align: center !important;
    }
    .agent-glow {
        font-size: 60px !important;
        color: white !important;
        animation: agentGlow 3s infinite !important;
        text-align: center !important;
    }
    .reel-container {
        background: linear-gradient(45deg, #1e3a8a, #1e40af);
        padding: 40px;
        border-radius: 20px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Branding
st.sidebar.header("🎨 Your Branding")
agent_name = st.sidebar.text_input("Agency Name", "John Doe Estates")
color = st.sidebar.color_picker("Accent Color", "#10b981")

# Property form
col1, col2 = st.columns(2)
with col1:
    st.subheader("📍 Property")
    address = st.text_input("Address", "123 High Street, London SW1")
    price = st.number_input("Price £", value=850000, step=50000)
with col2:
    st.subheader("Highlights")
    beds = st.number_input("Bedrooms", value=3)
    feature = st.text_input("Key Feature", "South-facing garden")

# Photos
st.subheader("📸 Hero Image")
photos = st.file_uploader("", type=['jpg','png','jpeg'], accept_multiple_files=False)

# GENERATE REEL
if st.button("🚀 GENERATE INSTAGRAM REEL", type="primary", use_container_width=True):
    if photos:
        # Show photo
        img = Image.open(photos).resize((400, 700), Image.Resampling.LANCZOS)
        st.image(img, caption="Your property → Reel", use_column_width=True)
        
        # MOTION GRAPHICS REEL
        st.markdown(f"""
        <div class="reel-container">
            <div class="price-hero">£{price:,}</div>
            <div class="beds-slide">{beds} BED LUXURY</div>
            <div style="font-size: 70px; color: white; text-align: center; margin: 20px 0;">
                {address}
            </div>
            <div class="agent-glow">{agent_name}</div>
            <div style="color: #60a5fa; font-size: 50px; text-align: center; margin-top: 30px;">
                {feature} ✨ SOLD FAST!
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Screenshot instructions
        st.success("📱 **REEL READY!**")
        st.markdown("""
        **✅ To post:**
        1. **Screen record** this animation (iPhone: swipe down → Record)
        2. OR **Screenshot** → Canva → Add motion
        3. Copy caption below → Instagram
        
        **Pro tip:** 15s screen recording = perfect Reel!
        """)
        
        # Pro caption
        caption = f"""🚨 **{address}** | £{price:,} | {beds} Beds 🏠
{feature}

Prime location • Modern finish • Viewing essential!
📞 {agent_name} • No chain

#LondonProperty #ForSale #EstateAgent #Reels
#PropertyInvestment #LuxuryHomes"""
        
        st.code(caption, language="markdown")
        
    else:
        st.warning("📸 Upload hero photo first!")

# Phone mockup
st.markdown("""
<div style="text-align: center; margin: 40px 0;">
    <div style="background: black; padding: 20px; border-radius: 40px; 
                display: inline-block; max-width: 400px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
        <div style="background: #000; border-radius: 30px; padding: 60px 20px 40px; position: relative;">
            <div style="position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
                        width: 150px; height: 6px; background: #333; border-radius: 3px;"></div>
            📱 **Instagram Reel Preview**
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("*Pro animated MP4s coming | Screen record for now*")

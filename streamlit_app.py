import streamlit as st
from PIL import Image

st.set_page_config(page_title="PropertyPost AI", layout="centered")
st.title("📱 PropertyPost AI")
st.markdown("*Instagram Reel Generator - Record & Post*")

# Compact branding
agent_name = st.text_input("🏢 Agency", "Prime Properties", key="agency")

# Ultra-simple form
address = st.text_input("🏠 Address", "123 High St, London", key="addr")
price = st.text_input("💰 Price", "£850,000", key="price")
beds = st.selectbox("🛏️ Beds", ["1", "2", "3", "4", "5"], key="beds")
feature = st.text_input("✨ Feature", "South garden", key="feat")

# Single photo
photo = st.file_uploader("📸 Photo", type=['jpg','jpeg','png'])

if st.button("🎥 GENERATE REEL", type="primary", use_container_width=True):
    st.markdown("---")
    
    if photo:
        # Hero image (centered)
        img = Image.open(photo).resize((400, 600), Image.Resampling.LANCZOS)
        st.image(img, caption="Hero shot", use_container_width=True)
        
        # SINGLE COLUMN REEL ANIMATION
        st.markdown(f"""
        <div style="max-width: 380px; margin: 30px auto; text-align: center;">
            <style>
            @keyframes explode {{0% {{transform:scale(0.1);opacity:0;}}70% {{transform:scale(1.2);}}100% {{transform:scale(1);opacity:1;}}}}
            @keyframes slidein {{0% {{transform:translateX(100%);opacity:0;}}100% {{transform:translateX(0);opacity:1;}}}}
            .reel-bg {{background:linear-gradient(135deg,#1e1e3f 0%,#2a1d4e 50%,#0f0f23 100%);border-radius:25px;padding:45px 25px;margin:auto;box-shadow:0 20px 60px rgba(0,0,0,0.7);}}
            .price-big {{font-size:85px;font-weight:900;color:#fff;line-height:0.9;margin:20px 0;text-shadow:0 3px 12px #0008;animation:explode 2s ease-out;letter-spacing:2px;}}
            .beds-anim {{font-size:55px;color:#00d9ff;font-weight:800;margin:12px 0;animation:slidein 1.3s 0.6s both;}}
            .feat-glow {{font-size:32px;color:#fff;font-weight:600;margin:18px 0;text-shadow:0 0 20px #00d9ff40;}}
            .agency-shine {{font-size:28px;color:#ffd700;font-weight:800;margin:15px 0;text-shadow:0 0 18px #ffd70060;}}
            .view-btn {{background:linear-gradient(45deg,#ff4d4d,#ff7a7a);color:white;border:none;padding:14px 32px;font-size:22px;font-weight:800;border-radius:35px;cursor:pointer;margin:25px auto;display:block;box-shadow:0 8px 25px #ff4d4d40;transition:all 0.3s;}}
            .view-btn:hover {{transform:translateY(-3px);box-shadow:0 12px 35px #ff4d4d60;}}
            </style>
            <div class="reel-bg">
                <div class="price-big">{price}</div>
                <div class="beds-anim">{beds} BED</div>
                <div class="feat-glow">{feature}</div>
                <div class="agency-shine">{agent_name}</div>
                <button class="view-btn">📞 VIEW NOW</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("🎉 **INSTAGRAM REEL READY!**")
        st.markdown("""
        **📱 3-Step Post:**
        1. **Screen Record** (15 seconds above)
        2. Instagram **Reels** → Upload video  
        3. **Copy caption** → Done!
        
        **💡 Add trending music for 10x views**
        """)
        
        caption = f"""🚨 {address} | {price} | {beds} Bed
{feature}

📲 {agent_name} | Book today!
#PropertyForSale #London #Reels #EstateAgent"""
        
        st.code(caption, language=None)
        
        # Record reminder
        st.balloons()
        
    else:
        st.error("📸 **Upload 1 photo first**")

# Footer mockup
st.markdown("""
<div style="text-align:center;margin-top:40px;padding:20px;background:#f8f9fa;border-radius:15px;">
    <div style="font-size:28px;color:#666;margin-bottom:10px;">📱 Instagram Reel Preview</div>
    <div style="font-size:14px;color:#999;">Screen record the animation above → Post → Sell!</div>
</div>
""", unsafe_allow_html=True)

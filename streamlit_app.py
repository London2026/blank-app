import streamlit as st
from PIL import Image

st.set_page_config(page_title="PropertyPost AI", layout="wide")
st.title("📱 PropertyPost AI")
st.markdown("*Instagram Reels - Screen Record Ready*")

# Sidebar
st.sidebar.header("🏢 Agency")
agent_name = st.sidebar.text_input("Name", "Prime Properties")

# Simple form - NO number input errors
st.subheader("Reel Generator")
col1, col2, col3 = st.columns(3)
with col1:
    address = st.text_input("Address", "123 High St, London")
with col2:
    price = st.text_input("Price", "£850,000")  # Text = no errors
with col3:
    beds = st.selectbox("Beds", [1,2,3,4,5])

feature = st.text_input("Feature", "South garden")

# Photo
photo = st.file_uploader("Hero Photo", type=['jpg','jpeg','png'])

# Generate
if st.button("🎥 CREATE REEL", type="primary", use_container_width=True):
    if photo:
        col1, col2 = st.columns([1,3])
        with col1:
            img = Image.open(photo).resize((280, 480))
            st.image(img, use_column_width=True)
        
        with col2:
            st.markdown(f"""
            <style>
            @keyframes boom {{0% {{transform:scale(0.2);opacity:0;}}70% {{transform:scale(1.3);}}100% {{transform:scale(1);opacity:1;}}}}
            @keyframes slide {{0% {{transform:translateX(100%);opacity:0;}}100% {{transform:translateX(0);opacity:1;}}}}
            .reel {{width:360px;height:640px;background:linear-gradient(#0f0f23,#1a1a3e);border-radius:28px;padding:50px 25px;margin:auto;box-shadow:0 25px 50px #0004;}}
            .price {{font-size:95px;color:#fff;font-weight:800;text-align:center;margin:25px 0;animation:boom 2s ease-out;text-shadow:2px 2px 8px #0008;letter-spacing:2px;}}
            .beds {{font-size:65px;color:#00d4ff;font-weight:700;text-align:center;margin:15px 0;animation:slide 1.5s 0.7s both;}}
            .feat {{font-size:36px;color:#fff;text-align:center;margin:20px 0;}}
            .agency {{font-size:32px;color:#ffd700;font-weight:700;text-align:center;margin:15px 0;text-shadow:0 0 15px #ffd70050;}}
            .cta {{background:linear-gradient(45deg,#ff4757,#ff6b7a);color:white;border:none;padding:15px 35px;font-size:24px;font-weight:700;border-radius:35px;cursor:pointer;margin:20px auto;display:block;box-shadow:0 8px 25px #ff475740;}}
            </style>
            <div class="reel">
                <div class="price">{price}</div>
                <div class="beds">{beds} BED</div>
                <div class="feat">{feature}</div>
                <div class="agency">{agent_name}</div>
                <button class="cta">📞 VIEW NOW</button>
            </div>
            """, unsafe_allow_html=True)
            
            st.success("🎉 **REEL READY!**")
            st.info("""
            **📱 Instagram:**
            1. Screen Record (15s)
            2. Reels → Upload recording  
            3. Copy caption → Post!
            """)
            
            caption = f"""🏠 {address} | {price} | {beds} Beds
{feature}

📲 {agent_name}
#Property #Reels #London #ForSale"""
            st.code(caption)
    else:
        st.warning("📸 Photo needed")

st.markdown("---")
st.caption("*Record screen → Post → Sell houses!*")

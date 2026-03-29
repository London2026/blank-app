import streamlit as st
from PIL import Image
import io
import base64

st.set_page_config(layout="wide")
st.title("🏠 PropertyPost AI")
st.markdown("**Instant Instagram posts for UK estate agents**")

# Form
col1, col2 = st.columns(2)
with col1:
    address = st.text_input("📍 Address", "123 High Street, London")
    price = st.number_input("💰 Price £", 850000)
with col2:
    beds = st.number_input("🛏️ Beds", 3)

photos = st.file_uploader("📸 Photos", accept_multiple_files=True)

if st.button("🚀 GENERATE POST", type="primary"):
    if photos:
        st.success("✅ **POST READY!**")
        
        # Show optimized images
        cols = st.columns(3)
        for i, photo in enumerate(photos[:3]):
            with cols[i]:
                img = Image.open(photo).resize((400, 700), Image.Resampling.LANCZOS)
                st.image(img, use_column_width=True, caption=f"Slide {i+1}")
        
        # Ready caption
        caption = f"""
🚨 **{address}** | £{price:,} | {beds} Beds 🏠
Modern perfection in prime location!
DM to view • No chain • EPC C

#LondonProperty #ForSale #EstateAgent #Reels
        """
        st.markdown("**📱 Copy-paste caption:**")
        st.code(caption)
        
        st.balloons()
    else:
        st.warning("📸 Upload photos!")

st.info("**Pro version:** Animated videos + auto-posting")
st.markdown("*Share: your-app.streamlit.app*")

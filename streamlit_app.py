import streamlit as st
from PIL import Image

st.set_page_config(page_title="PropertyPost AI", layout="wide")
st.title("📱 PropertyPost AI")
st.markdown("**15s Instagram Reels - Screen Record & Post**")

# Instagram-optimized CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif !important; }

.reel-preview {
    max-width: 400px !important;
    margin: 30px auto !important;
}

.reel-screen {
    width: 360px !important;
    height: 640px !important;
    background: linear-gradient(180deg, #0f0f23 0%, #1a1a3e 50%, #2d1b69 100%) !important;
    border-radius: 28px !important;
    padding: 50px 25px 40px !important;
    margin: auto !important;
    box-shadow: 0 25px 50px rgba(0,0,0,0.6) !important;
    position

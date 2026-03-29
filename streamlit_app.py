import streamlit as st
import numpy as np
from PIL import Image
from moviepy.editor import *
import io

st.set_page_config(layout="wide", page_title="PropertyPost AI")
st.title("🏠 PropertyPost AI")
st.markdown("**Instant animated posts for UK estate agents**")

# Sidebar
st.sidebar.header("🎨 Branding")
agent_name = st.sidebar.text_input("Agency", "John Doe Estates")

# Form
col1, col2 = st.columns(2)
with col1:
    st.subheader("📍 Property")
    address = st.text_input("Address", "123 High Street, London")
    price = st.number_input("Price £", value=850000)
with col2:
    beds = st.number_input("Beds", 3)

# Photos
st.subheader("📸 Upload Photos")
photos = st.file_uploader("", type=['jpg','png','jpeg'], accept_multiple_files=True)

if st.button("🚀 GENERATE VIDEO", type="primary", use_container_width=True):
    if not photos:
        st.error("📸 Upload photos first!")
    else:
        with st.spinner("🎬 Creating Reel..."):
            try:
                clips = []
                for photo in photos[:3]:
                    # FIXED: PIL ANTIALIAS issue
                    img = Image.open(photo).convert('RGB')
                    img_resized = img.resize((1080, 1920), Image.Resampling.LANCZOS)
                    
                    # Create clip
                    clip = ImageClip(np.array(img_resized)).set_duration(4)
                    
                    # Price overlay
                    price_txt = TextClip(f"£{price:,}", fontsize=120, color='white',
                                       stroke_color='black', stroke_width=2)\
                               .set_position(('center', 300)).set_duration(4)
                    
                    beds_txt = TextClip(f"{beds} BEDS", fontsize=70, color='#10b981')\
                              .set_position(('center', 'bottom')).set_duration(4)
                    
                    final_clip = CompositeVideoClip([clip, price_txt, beds_txt])
                    clips.append(final_clip)
                
                # Combine
                final_video = concatenate_videoclips(clips).subclip(0, 12)
                
                # Export
                buf = io.BytesIO()
                final_video.write_videofile(buf, fps=24, audio=False, 
                                          verbose=False, logger=None)
                buf.seek(0)
                
                st.success("✅ **REEL READY!**")
                st.video(buf)
                st.download_button("💾 DOWNLOAD MP4", buf.getvalue(),
                                 "property_reel.mp4", "video/mp4")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Try fewer photos or JPEG format")

st.markdown("---")
st.markdown("*Live SaaS for estate agents | Share: your-app.streamlit.app*")

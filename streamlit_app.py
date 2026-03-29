import streamlit as st
import numpy as np
from PIL import Image
from moviepy.editor import *
import io

st.set_page_config(layout="wide", page_title="PropertyPost AI")
st.title("🏠 PropertyPost AI")
st.markdown("**Animated social posts for UK estate agents**")

# Sidebar branding
st.sidebar.header("🎨 Agency Branding")
agent_name = st.sidebar.text_input("Agency", "John Doe Estates")

# Main form
col1, col2 = st.columns([1,1])
with col1:
    st.subheader("📍 Property Details")
    address = st.text_input("Address", "123 High Street, London SW1")
    price = st.number_input("Asking Price £", value=850000, step=50000)
with col2:
    st.subheader("Key Features")
    beds = st.number_input("Bedrooms", value=3)
    baths = st.number_input("Bathrooms", value=2)

# Photo upload
st.subheader("📸 Property Photos")
photos = st.file_uploader("Drag & drop 3-5 images", 
                         type=['jpg','jpeg','png'], 
                         accept_multiple_files=True)

# Generate button
if st.button("🚀 CREATE INSTAGRAM POST", type="primary", use_container_width=True):
    if len(photos) == 0:
        st.error("📸 Please upload photos first!")
    else:
        with st.spinner("🎬 Generating professional video... (15s)"):
            try:
                clips = []
                for i, photo_file in enumerate(photos[:3]):
                    # Process image
                    image = Image.open(photo_file).convert('RGB').resize((1080, 1920))
                    
                    # Base clip with zoom
                    clip = ImageClip(np.array(image)).set_duration(4)
                    clip = clip.resize(lambda t: 1 + 0.15 * t / 4)
                    
                    # Price animation
                    price_text = TextClip(f"£{price:,}", fontsize=130, color='white',
                                        stroke_color='black', stroke_width=3, 
                                        font='Arial-Bold').set_position(('center', 350))
                    price_text = price_text.set_duration(4).set_start(0.5)
                    
                    # Beds text
                    beds_text = TextClip(f"{beds} BED PERFECTION", fontsize=70, 
                                       color='#10b981', font='Arial-Bold')\
                               .set_position(('center', 'bottom')).set_duration(4)
                    
                    # Agency branding
                    brand_text = TextClip(agent_name, fontsize=50, color='white')\
                                 .set_position(('center', 'bottom+80')).set_duration(4)
                    
                    # Composite
                    final_clip = CompositeVideoClip([clip, price_text, beds_text, brand_text])
                    clips.append(final_clip)
                
                # Final video
                final_video = concatenate_videoclips(clips).subclip(0, 12)
                
                # Export to buffer
                buf = io.BytesIO()
                final_video.write_videofile(buf, fps=24, codec='libx264',
                                          verbose=False, logger=None, audio=False)
                buf.seek(0)
                
                # Show result
                st.success("✅ **POST READY!** Perfect for Instagram Reels/TikTok")
                st.video(buf)
                st.download_button("💾 DOWNLOAD MP4", buf.getvalue(),
                                 f"{address.replace(' ','_')}_reel.mp4", "video/mp4")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. **Fill property details** (address, price, beds)
    2. **Drag 3+ photos** from your listings
    3. **Click GENERATE** 
    4. **Download MP4** → Post to Instagram/TikTok!
    
    **Pro tips:**
    - Use vertical photos (1080x1920 best)
    - 15s perfect for Reels
    - Add your logo in sidebar
    """)

st.markdown("---")
st.markdown("*Built for UK estate agents | Free to use*")

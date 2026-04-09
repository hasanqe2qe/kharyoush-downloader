import streamlit as st
import yt_dlp
import os

# إعدادات الصفحة والجمالية
st.set_page_config(page_title="KHARYOUSH PRO", page_icon="🔮", layout="centered")

# CSS لتصميم بنفسجي عصري ولامع (Glassmorphism)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0b2e 0%, #3d1a6d 100%);
        font-family: 'Tajawal', sans-serif;
        color: #ffffff;
    }
    
    .main-title {
        font-size: 55px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(to right, #e0aaff, #bc98ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 20px rgba(188, 152, 255, 0.5);
        margin-bottom: 5px;
    }
    
    .sub-title {
        text-align: center;
        color: #e0aaff;
        font-size: 16px;
        margin-bottom: 40px;
        letter-spacing: 2px;
    }

    /* تنسيق الحقول */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border: 1px solid #bc98ff;
        border-radius: 12px;
        padding: 15px;
    }

    /* الزر اللامع */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #7b2cbf, #9d4edd);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: bold;
        padding: 20px;
        transition: 0.3s;
        box-shadow: 0px 0px 15px rgba(157, 78, 221, 0.4);
    }
    
    .stButton>button:hover {
        box-shadow: 0px 0px 25px rgba(157, 78, 221, 0.8);
        transform: translateY(-2px);
    }

    /* إخفاء العناصر غير الضرورية */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    
    <div class="main-title">KHARYOUSH PRO</div>
    <div class="sub-title">THE INTELLIGENT MEDIA ENGINE</div>
    """, unsafe_allow_html=True)

# المدخلات
url = st.text_input("", placeholder="صق رابط الفيديو هنا...")

if url:
    try:
        # إعدادات تخطي الحظر والجودة
        ydl_opts_info = {
            'quiet': True, 
            'noplaylist': True,
            'extractor_args': {'youtube': {'player_client': ['android', 'web']}} 
        }
        
        with st.container():
            with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # عرض معلومات مختصرة وعصرية
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(info.get('thumbnail'), use_column_width=True)
                with col2:
                    st.markdown(f"**{info.get('title')[:50]}...**")
                    st.caption(f"👤 {info.get('uploader')} | 👁️ {info.get('view_count', 0):,}")

            st.markdown("---")
            format_choice = st.selectbox("صيغة التحميل", ["Video (MP4)", "Audio (MP3)"], label_visibility="collapsed")

            if st.button("DOWNLOAD NOW"):
                with st.spinner('Processing...'):
                    # إعدادات التحميل النهائية
                    common_opts = {
                        'extractor_args': {'youtube': {'player_client': ['android', 'ios']}},
                        'nocheckcertificate': True,
                        'quiet': True
                    }

                    if "MP3" in format_choice:
                        ydl_opts = {**common_opts, 'format': 'bestaudio/best', 'outtmpl': 'k_audio',
                                    'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}
                        final_file, mime = "k_audio.mp3", "audio/mpeg"
                    else:
                        ydl_opts = {**common_opts, 'format': 'best[ext=mp4]/best', 'outtmpl': 'k_video.mp4'}
                        final_file, mime = "k_video.mp4", "video/mp4"

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                    with open(final_file, "rb") as f:
                        st.download_button(label="SAVE TO DEVICE", data=f, file_name=final_file, mime=mime)
                    os.remove(final_file)

    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("<br><p style='text-align:center; opacity:0.5; font-size:12px;'>KHARYOUSH PRO © 2026</p>", unsafe_allow_html=True)

import streamlit as st
import yt_dlp
import os

# إعدادات الواجهة البنفسجية العصرية
st.set_page_config(page_title="KHARYOUSH PRO", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0b2e 0%, #3d1a6d 100%);
        font-family: 'Tajawal', sans-serif;
        color: #ffffff;
    }
    .main-title {
        font-size: 50px; font-weight: 800; text-align: center;
        background: linear-gradient(to right, #e0aaff, #bc98ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 20px rgba(188, 152, 255, 0.5);
    }
    .stTextInput>div>div>input { background-color: rgba(255,255,255,0.05); color: white; border: 1px solid #bc98ff; border-radius: 12px; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #7b2cbf, #9d4edd); color: white; border-radius: 12px; font-weight: bold; padding: 15px; border: none; box-shadow: 0px 0px 15px rgba(157, 78, 221, 0.4); }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    <div class="main-title">KHARYOUSH PRO</div>
    <p style='text-align:center; color:#e0aaff;'>The Intelligent Media Engine</p>
    """, unsafe_allow_html=True)

url = st.text_input("", placeholder="صق رابط الفيديو هنا...")

if url:
    try:
        # إعدادات "التمويه" لتخطي الحظر
        common_opts = {
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            },
            'extractor_args': {'youtube': {'player_client': ['ios', 'web', 'android']}},
        }

        with st.spinner('جاري جلب معلومات الفيديو...'):
            with yt_dlp.YoutubeDL(common_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                st.image(info.get('thumbnail'), use_column_width=True)
                st.markdown(f"<p style='text-align:center;'>{info.get('title')}</p>", unsafe_allow_html=True)

        st.markdown("---")
        format_choice = st.selectbox("", ["Video (MP4)", "Audio (MP3)"], label_visibility="collapsed")

        if st.button("DOWNLOAD NOW"):
            with st.spinner('جاري التحميل...'):
                if "MP3" in format_choice:
                    opts = {**common_opts, 'format': 'bestaudio/best', 'outtmpl': 'k_audio',
                            'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]}
                    final_file, mime = "k_audio.mp3", "audio/mpeg"
                else:
                    # نستخدم جودة 720p أو أقل لأنها الأكثر استقراراً في التجاوز
                    opts = {**common_opts, 'format': 'best[ext=mp4]/best', 'outtmpl': 'k_video.mp4'}
                    final_file, mime = "k_video.mp4", "video/mp4"

                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])

                with open(final_file, "rb") as f:
                    st.download_button(label="SAVE TO DEVICE", data=f, file_name=final_file, mime=mime)
                os.remove(final_file)

    except Exception as e:
        st.error(f"يوتيوب يحاول حظر السيرفر. جرب رابطاً آخر أو انتظر دقيقة. الخطأ: {e}")

st.markdown("<br><p style='text-align:center; opacity:0.5; font-size:12px;'>KHARYOUSH PRO © 2026</p>", unsafe_allow_html=True)

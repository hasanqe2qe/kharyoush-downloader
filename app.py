import streamlit as st
import yt_dlp
import os

# تصميم الواجهة البنفسجية اللامعة
st.set_page_config(page_title="KHARYOUSH PRO", page_icon="🔮")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0b2e 0%, #3d1a6d 100%);
        font-family: 'Tajawal', sans-serif;
        color: #ffffff;
    }
    .main-title {
        font-size: 50px; font-weight: 800; text-align: center;
        background: linear-gradient(to right, #e0aaff, #bc98ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(188, 152, 255, 0.4);
    }
    .stTextInput>div>div>input { background-color: rgba(255,255,255,0.05); color: white; border: 1px solid #bc98ff; border-radius: 12px; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #7b2cbf, #9d4edd); color: white; border-radius: 12px; font-weight: bold; border: none; box-shadow: 0px 0px 15px rgba(157, 78, 221, 0.3); }
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    <div class="main-title">KHARYOUSH PRO</div>
    """, unsafe_allow_html=True)

url = st.text_input("", placeholder="صق الرابط هنا...")

if url:
    try:
        # إعدادات التمويه القصوى
        ydl_opts_base = {
            'quiet': True,
            'no_warnings': True,
            'format': 'best', # طلب ملف مدمج جاهز لتفادي الحظر
            'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0',
            }
        }

        with st.spinner('يتم الآن فحص الفيديو...'):
            with yt_dlp.YoutubeDL(ydl_opts_base) as ydl:
                info = ydl.extract_info(url, download=False)
                st.image(info.get('thumbnail'), use_column_width=True)
                st.markdown(f"<p style='text-align:center;'>{info.get('title')}</p>", unsafe_allow_html=True)

        choice = st.radio("النوع:", ["فيديو MP4", "صوت MP3"], horizontal=True)

        if st.button("DOWNLOAD NOW"):
            with st.spinner('محاولة كسر حظر يوتيوب...'):
                if "صوت" in choice:
                    opts = {**ydl_opts_base, 'format': 'bestaudio/best', 'outtmpl': 'k.mp3',
                            'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '128'}]}
                    file_name = "k.mp3"
                else:
                    opts = {**ydl_opts_base, 'format': 'best[ext=mp4]', 'outtmpl': 'k.mp4'}
                    file_name = "k.mp4"

                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([url])

                with open(file_name, "rb") as f:
                    st.download_button("💾 اضغط هنا للحفظ", f, file_name=f"KHARYOUSH_{file_name}")
                os.remove(file_name)

    except Exception as e:
        st.warning("⚠️ يبدو أن يوتيوب حظر السيرفر مؤقتاً. جرب بعد 5 دقائق أو جرب رابطاً من قناة أخرى.")

st.markdown("<p style='text-align:center; opacity:0.3; font-size:10px; margin-top:50px;'>KHARYOUSH PRO 2026</p>", unsafe_allow_html=True)

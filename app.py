import streamlit as st
import yt_dlp
import os

# إعدادات الصفحة
st.set_page_config(page_title="KHARYOUSH PRO", page_icon="🎥", layout="centered")

# تنسيق الواجهة
st.markdown("""
    <style>
    .main-title { color: #FF0000; text-align: center; font-size: 45px; font-weight: bold; font-family: 'Arial'; }
    .stButton>button { width: 100%; border-radius: 15px; background-color: #FF0000; color: white; font-weight: bold; }
    .video-info { background-color: #f0f2f6; padding: 20px; border-radius: 15px; margin-bottom: 20px; direction: rtl; }
    </style>
    <div class="main-title">KHARYOUSH PRO</div>
    <p style='text-align:center;'>المحرك الذكي لتحميل الوسائط</p>
    """, unsafe_allow_html=True)

# مدخل الرابط
url = st.text_input("أدخل رابط الفيديو هنا:", placeholder="https://www.youtube.com/watch?v=...")

if url:
    try:
        with st.spinner('جاري جلب معلومات الفيديو...'):
            # إعدادات جلب المعلومات فقط بدون تحميل
            ydl_opts_info = {'quiet': True, 'noplaylist': True}
            with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # عرض معلومات الفيديو بشكل أنيق
                st.markdown(f"""
                <div class="video-info">
                    <h4>📺 {info.get('title')}</h4>
                    <p>👤 <b>القناة:</b> {info.get('uploader')}</p>
                    <p>👁️ <b>المشاهدات:</b> {info.get('view_count', 0):,}</p>
                    <p>⏱️ <b>المدة:</b> {int(info.get('duration', 0)/60)} دقيقة</p>
                </div>
                """, unsafe_allow_html=True)
                
                # إظهار الصورة المصغرة
                st.image(info.get('thumbnail'), use_column_width=True)

        # خيارات التحميل
        st.markdown("---")
        format_choice = st.selectbox("اختر صيغة التحميل:", ["فيديو (Video + Audio)", "صوت فقط (MP3)"])

        if st.button("بدء التحميل الآن"):
            with st.spinner('جاري التحميل والمعالجة...'):
                if format_choice == "صوت فقط (MP3)":
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': 'KHARYOUSH_audio',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                else:
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio/best',
                        'outtmpl': 'KHARYOUSH_video.%(ext)s',
                    }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                    # تحديد اسم الملف النهائي
                    if format_choice == "صوت فقط (MP3)":
                        final_file = "KHARYOUSH_audio.mp3"
                    else:
                        # جلب الامتداد الصحيح للفيديو
                        file_info = ydl.extract_info(url, download=False)
                        ext = file_info.get('ext', 'mp4')
                        final_file = f"KHARYOUSH_video.{ext}"

                # زر حفظ الملف النهائي
                with open(final_file, "rb") as f:
                    st.download_button(
                        label=f"💾 حفظ الـ {format_choice} على جهازك",
                        data=f,
                        file_name=final_file,
                        mime="video/mp4" if "فيديو" in format_choice else "audio/mpeg"
                    )
                # حذف الملف من السيرفر بعد انتهاء العملية
                if os.path.exists(final_file):
                    os.remove(final_file)

    except Exception as e:
        st.error(f"عذراً، حدث خطأ: {e}")

# عداد زوار بسيط في الأسفل
st.markdown("---")
st.markdown("![Visitor Count](https://profile-counter.glitch.me/kharyoush/count.svg)")
st.caption("KHARYOUSH PRO - 2026")
import streamlit as st
import time

# إعدادات الصفحة والكلمات المفتاحية لمحركات البحث (SEO)
st.set_page_config(
    page_title="حكايات خريوش السحرية - قصص أطفال ذكية",
    page_icon="✨",
    initial_sidebar_state="collapsed"
)

# تصميم بنفسجي طفولي وعصري في نفس الوقت
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #2d1b4e 0%, #1b0b2e 100%);
        font-family: 'Tajawal', sans-serif;
        color: white;
        direction: rtl;
    }
    .main-title {
        font-size: 45px; text-align: center;
        background: linear-gradient(to right, #f0abfc, #c084fc);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(192, 132, 252, 0.4);
        margin-top: -50px;
    }
    .story-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 20px;
        border: 1px solid #c084fc;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
        line-height: 1.8; font-size: 18px;
    }
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #9333ea, #c084fc);
        color: white; border-radius: 15px; border: none; font-weight: bold; padding: 15px;
    }
    </style>
    <div class="main-title">✨ حكايات خريوش السحرية</div>
    <p style='text-align:center; color:#e9d5ff;'>اصنع قصتك الفريدة بلمسة واحدة</p>
    """, unsafe_allow_html=True)

# واجهة الاختيارات
col1, col2 = st.columns(2)
with col1:
    hero = st.selectbox("اختر بطل القصة:", ["الأرنب القافز", "الروبوت اللطيف", "السمكة المغامرة", "نجم السحر"])
with col2:
    place = st.selectbox("أين تدور الأحداث؟", ["في الغابة السرية", "فوق السحاب", "في جزيرة الكنز", "في مدرسة الأذكياء"])

if st.button("🪄 ابدأ السحر واصنع الحكاية"):
    with st.spinner('جاري كتابة الحكاية...'):
        time.sleep(2) # محاكاة تفكير الذكاء الاصطناعي
        
        # قالب القصص (يمكنك توسيعه لاحقاً بربطه بذكاء اصطناعي حقيقي)
        story_templates = {
            "الأرنب القافز": f"كان يا ما كان، في {place}، أرنب صغير يحب القفز عالياً. في يوم من الأيام اكتشف سراً عظيماً غير حياته وحياة أصدقائه...",
            "الروبوت اللطيف": f"في أعماق {place}، استيقظ روبوت صغير له قلب من ذهب. لم يكن يعرف كيف يلعب، حتى قابل طفلاً علمه أن الصداقة هي أجمل لغة...",
            "السمكة المغامرة": f"تحت أمواج {place}، كانت هناك سمكة ملونة تحلم برؤية العالم. قادتها شجاعتها لخوض مغامرة لم يسبقها إليها أحد...",
            "نجم السحر": f"في سماء {place}، سقط نجم صغير عن طريق الخطأ. كان عليه أن يجد طريق العودة بمساعدة أصدقاء جدد التقى بهم هناك..."
        }
        
        st.markdown(f"""
        <div class="story-card">
            <h3 style='color:#f0abfc; text-align:center;'>📖 قصة {hero}</h3>
            {story_templates[hero]}
            <br><br>
            <b>العبرة:</b> الشجاعة والتعاون يصنعان المعجزات!
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# الكلمات المفتاحية لمحركات البحث (مخفية)
st.markdown("""
    <div style='display:none;'>
        قصص أطفال، حكايات قبل النوم، قصص تعليمية، موقع خريوش للأطفال، ذكاء اصطناعي للأطفال.
    </div>
    """, unsafe_allow_html=True)

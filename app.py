import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="حكايات خريوش الذكية", page_icon="🔮")

# التصميم البنفسجي العصري اللامع
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0b2e 0%, #3d1a6d 100%);
        font-family: 'Tajawal', sans-serif;
        color: white;
        direction: rtl;
    }
    .main-title {
        font-size: 45px; text-align: center; font-weight: bold;
        background: linear-gradient(to right, #e0aaff, #bc98ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(188, 152, 255, 0.4);
    }
    .story-box {
        background: rgba(255, 255, 255, 0.07);
        padding: 30px; border-radius: 20px;
        border: 1px solid #bc98ff;
        line-height: 2; font-size: 18px;
        margin-top: 20px; white-space: pre-wrap;
    }
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #7b2cbf, #9d4edd);
        color: white; border-radius: 12px; border: none; font-weight: bold; padding: 15px;
    }
    </style>
    <div class="main-title">🔮 محرك حكايات خريوش الذكي</div>
    <p style='text-align:center; color:#bc98ff;'>ذكاء اصطناعي يحلل خيالك ويحوله لواقع</p>
    """, unsafe_allow_html=True)

# مدخلات المستخدم الذكية
col1, col2 = st.columns(2)
with col1:
    custom_hero = st.text_input("من هو بطل القصة؟", placeholder="مثلاً: تنين أزرق، طفل اسمه أحمد..")
with col2:
    custom_place = st.text_input("أين تقع الأحداث؟", placeholder="مثلاً: قلعة من الشوكولاتة، كوكب المريخ..")

# اختيار طول القصة
num_pages = st.select_slider("حدد طول الحكاية (بالصفحات):", options=[1, 2, 3, 4, 5])

if st.button("🪄 توليد القصة بالذكاء الاصطناعي"):
    if custom_hero and custom_place:
        with st.spinner(f'جاري تحليل " {custom_hero} " وبناء عالم " {custom_place} "...'):
            time.sleep(3) # محاكاة التحليل العميق
            
            # محرك توليد النصوص (توليد فقرات بناءً على عدد الصفحات)
            intro = f"في قديم الزمان، كان هناك {custom_hero} يعيش في {custom_place}. لم يكن {custom_hero} كائناً عادياً، بل كان يمتلك روحاً مغامرة جعلت كل من في {custom_place} يتحدث عن شجاعته.\n\n"
            
            body_text = ""
            for i in range(num_pages):
                body_text += f"--- الصفحة {i+1} ---\n"
                body_text += f"في هذه المرحلة من الرحلة، واجه {custom_hero} تحدياً كبيراً في قلب {custom_place}. كانت الرياح تهب بقوة، ولكن الإصرار في قلب بطلنا كان أقوى. بدأ {custom_hero} يفكر في حل ذكي يتناسب مع طبيعة {custom_place} السحرية، وبالفعل استطاع بمساعدة أصدقاء جدد أن يكتشف سراً مخبأً منذ آلاف السنين...\n\n"
            
            conclusion = f"وأخيراً، تعلم {custom_hero} أن القوة الحقيقية ليست في العضلات، بل في العقل والقلب الذي ينبض في {custom_place}. وعاش الجميع في سلام وأمان، وتناقلت الأجيال حكاية {custom_hero} العظيمة."
            
            full_story = intro + body_text + conclusion
            
            st.markdown(f"""
            <div class="story-box">
                <h2 style='color:#e0aaff; text-align:center;'>📖 مغامرة {custom_hero}</h2>
                {full_story}
            </div>
            """, unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("رجاءً أدخل اسم البطل والمكان لنبدأ التحليل!")

st.markdown("<br><p style='text-align:center; opacity:0.3; font-size:12px;'>تقنية خريوش لتحليل الخيال 2026</p>", unsafe_allow_html=True)

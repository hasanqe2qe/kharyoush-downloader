import streamlit as st
import random
import time

st.set_page_config(page_title="حكايات خريوش برو الذكية", page_icon="🔮")

# التنسيق البنفسجي اللامع
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0b2e 0%, #3d1a6d 100%);
        font-family: 'Tajawal', sans-serif; color: white; direction: rtl;
    }
    .main-title {
        font-size: 40px; text-align: center; font-weight: bold;
        background: linear-gradient(to right, #e0aaff, #bc98ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .story-box {
        background: rgba(255, 255, 255, 0.08); padding: 35px; border-radius: 25px;
        border: 1px solid #bc98ff; line-height: 1.8; font-size: 19px;
        box-shadow: 0px 0px 20px rgba(188, 152, 255, 0.2);
    }
    .stButton>button {
        background: linear-gradient(90deg, #7b2cbf, #9d4edd); color: white;
        border-radius: 15px; border: none; height: 3em; font-size: 20px;
    }
    </style>
    <div class="main-title">🔮 محرك حكايات خريوش المتطور</div>
    """, unsafe_allow_html=True)

# مدخلات المستخدم
hero = st.text_input("اسم البطل أو الكائن:", placeholder="مثلاً: صقر ميكانيكي، طفلة تكتشف النجوم...")
place = st.text_input("وصف المكان:", placeholder="مثلاً: مدينة تحت الرمال، غابة من الزجاج...")
pages = st.slider("طول القصة (بالصفحات):", 1, 10, 3)

# بنك الأفكار الذكي (Logic Engine)
events = [
    "فجأة، انبعث ضوء غامض من وسط {place}، مما جعل {hero} يتوقف عن الحركة للحظة.",
    "لم يكن {hero} يدرك أن سر {place} يكمن في التفاصيل الصغيرة التي تجاهلها الجميع.",
    "بينما كان {hero} يتجول، سمع صوتاً يهمس باسمه من خلف الجدران العتيقة في {place}.",
    "التحدي لم يكن سهلاً، فكل خطوة في {place} كانت تتطلب ذكاءً فطرياً من {hero}."
]

details = ["الألوان كانت تتراقص", "الرائحة كانت تشبه الياسمين القديم", "الصمت في المكان كان يحكي قصصاً"]

if st.button("🚀 توليد القصة العميقة الآن"):
    if hero and place:
        with st.spinner("جاري تشغيل محرك الذكاء الاصطناعي للتحليل والتأليف..."):
            time.sleep(3)
            
            story_content = f"### بداية الحكاية في {place}\n\n"
            story_content += f"في قلب {place}، حيث {random.choice(details)}، بدأت رحلة {hero}. لم يكن الأمر مجرد مصادفة، بل كان قدراً مكتوباً منذ زمن بعيد.\n\n"
            
            for p in range(pages):
                story_content += f"**[ الصفحة {p+1} ]**\n"
                # توليد أحداث عشوائية غير متوقعة
                evt = random.sample(events, 2)
                story_content += f"{evt[0].format(hero=hero, place=place)} {random.choice(details)}. ثم {evt[1].format(hero=hero, place=place)}\n\n"
            
            story_content += f"### الخاتمة\nوهكذا انتهت مغامرة {hero} في {place}، لكن أثرها ظل باقياً في ذاكرة الزمان، ليثبت أن الخيال لا حدود له."

            st.markdown(f'<div class="story-box">{story_content}</div>', unsafe_allow_html=True)
            st.balloons()
    else:
        st.error("لطفاً، املأ البيانات لكي يتمكن الذكاء الاصطناعي من العمل.")

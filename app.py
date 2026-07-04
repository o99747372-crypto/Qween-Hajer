import streamlit as st
from datetime import date
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Hajer's Kingdom",
    page_icon="👑",
    layout="wide"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(125deg, #000000, #2d0036, #6a0572, #ff0080, #ff8da1);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

header {
    visibility: hidden;
}

.glass-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,192,203,0.3);
    border-radius: 25px;
    padding: 25px;
    margin-bottom: 20px;
}

h1, h2, h3 {
    color: white !important;
    text-align: center;
}

.special-word {
    background: rgba(255,255,255,0.08);
    border-right: 4px solid #ff0080;
    padding: 12px;
    margin: 8px 0;
    border-radius: 12px;
    color: #ffe0ed;
    direction: rtl;
    font-size: 18px;
}

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #ff0080, #ffc0cb);
}

.stat-label {
    color: white;
    font-weight: bold;
    display: flex;
    justify-content: space-between;
    direction: rtl;
    margin-bottom: 5px;
}

div[data-testid="stExpander"] {
    background: rgba(255,255,255,0.07);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    overflow: hidden;
    margin-bottom: 20px;
}

div[data-testid="stExpander"] details summary p {
    font-size: 24px;
    color: white !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ---------------- IMAGE FUNCTION ----------------
def display_img(path):
    alts = [
        path,
        path + ".jpg",
        path + ".jpeg",
        path + ".png",
        path + ".JPG",
        path + ".JPEG",
        path + ".PNG"
    ]
    found = next((p for p in alts if os.path.exists(p)), None)
    if found:
        st.image(found, use_container_width=True)
    else:
        st.markdown(
            f"<div style='color:#ffc0cb;text-align:center;'> {path} not found</div>",
            unsafe_allow_html=True
        )


# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "viewing_private" not in st.session_state:
    st.session_state.viewing_private = False


# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:
    st.markdown("<div style='height:20vh;'></div>", unsafe_allow_html=True)
    _, center, _ = st.columns([1, 1.4, 1])
    with center:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h1 style='font-size:55px;'> LOGIN </h1>",
            unsafe_allow_html=True
        )
        username = st.text_input("Username", value="Hajer walid")
        password = st.text_input("Password", type="password")
        if st.button("ENTER", use_container_width=True):
            if username == "Hajer walid" and password == "642010":
                st.session_state.logged_in = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PRIVATE VAULT ----------------
elif st.session_state.viewing_private:
    st.markdown(
        "<h1 style='font-size:55px;'> PRIVATE VAULT </h1>",
        unsafe_allow_html=True
    )
    if st.button("Back"):
        st.session_state.viewing_private = False
        st.rerun()

    tabs = st.tabs(["Photos", "Our Words"])

    # -------- PRIVATE PHOTOS (14) --------
    with tabs[0]:
        for i in range(0, 14, 4):
            cols = st.columns(4)
            for j in range(4):
                if (i + j) < 14:
                    with cols[j]:
                        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                        display_img(f"private{i+j+1}")
                        st.markdown('</div>', unsafe_allow_html=True)

    # -------- PRIVATE WORDS (Full List No Emojis) --------
    with tabs[1]:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        private_words = [
            "انتي كبرتي في نظري اوي يا هاجر",
            "مش شايفه لمعه عيني وانا ببصلك",
            "طب بصي في حاجه مش عارف اقولهالك ازاي شكلي هحبك يلا روحي بقي",
            "ترجييعع",
            "دكر البط حجي",
            "جووزيي راجلي و شايله اسمه",
            "يابنت نجلاء الجامده",
            "يابن صباح الشحرورة",
            "بحبك رغم انك دماغك ناشفه زيي و عصبي و ياابن القادره",
            "دول بيصورمو مني",
            "هاتي بوسه بقي",
            "بطتيييي",
            "وريني فخادك",
            "همبرجر",
            "عايزة اكل حواوشي",
            "ياابو كرش يامبطون",
            "كل ده بتشخ",
            "تعالي وصلني المدرسه",
            "عايزة اخلف توأم",
            "بحبك اوي يا دكر البط بتاعي",
            "قولي كلام حب",
            "سييييين",
            "ربنا معاك يكوتي توتي موتي بوتي",
            "طلعلي حبوب في وشي يااسامه",
            "لو مقولتليش هيبقي نكد ليڤل الوحش",
            "انا بكرهك",
            "تدفع كام ؟",
            "عايزة ابقي الاميرة شفق",
            "امك صحبتي",
            "اععععععع",
            "انا الي دماغي معاقه انت عارف",
            "عشان لما نتجوز اكون حوشتلك بوس كتير",
            "انا متخانقه مع امي",
            "ادعيلك ؟",
            "اعملي فيديو",
            "هتخطبني امتي",
            "ايه رأيك نضرب ورقتين عرفي",
            "كتب الكتاب امتي",
            "افتح مطعم عشان اجي اكل عندك",
            "تعالي هاتلي اندومي",
            "بتفرج علي مسلسل",
            "انت عامل حساب للدنيا كلها وانا برا حساباتك",
            "هو انا المفروض اوريك شعري امتي ؟",
            "هات 500 جنيه واعملك الي انت عايزو",
            "خلي عندك كرامه بقي",
            "اعملهااااااا بلوووووك",
            "ملكش دعوة ياشخه الكلب"
        ]
        for word in private_words:
            st.markdown(f'<div class="special-word">{word}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ---------------- MAIN DASHBOARD ----------------
else:
    st.markdown(
        "<h1 style='font-size:65px;'> HAJER WORLD </h1>",
        unsafe_allow_html=True
    )

    # ---------------- GALLERY (5) ----------------
    with st.expander(" Gallery", expanded=False):
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                display_img(f"photo{i+1}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- ART (4) ----------------
    with st.expander(" Creativity", expanded=False):
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        cols = st.columns(4)
        for i in range(4):
            with cols[i]:
                display_img(f"art{i+1}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- FOOD (9) ----------------
    with st.expander(" Food Corner", expanded=False):
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        for r in range(0, 9, 3):
            cols = st.columns(3)
            for j in range(3):
                with cols[j]:
                    display_img(f"food{r+j+1}")
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- ANALYTICS ----------------
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h2> Performance Analytics</h2>", unsafe_allow_html=True)
    s1, s2 = st.columns(2)
    with s1:
        st.markdown('<div class="stat-label"><span>الحنية</span><span>100%</span></div>', unsafe_allow_html=True)
        st.progress(1.0)
        st.markdown('<div class="stat-label"><span>الحب</span><span>1000%</span></div>', unsafe_allow_html=True)
        st.progress(1.0)
        st.markdown('<div class="stat-label"><span>خفة الدم</span><span>100000%</span></div>', unsafe_allow_html=True)
        st.progress(1.0)
    with s2:
        st.markdown('<div class="stat-label"><span>الجمال</span><span>100000000%</span></div>', unsafe_allow_html=True)
        st.progress(1.0)
        st.markdown('<div class="stat-label"><span>النكد</span><span>100000000000%</span></div>', unsafe_allow_html=True)
        st.progress(1.0)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- SECRET VAULT ----------------
    st.markdown('<div class="glass-card" style="border:2px solid #ff0080;">', unsafe_allow_html=True)
    st.markdown("<h2> Secret Vault</h2>", unsafe_allow_html=True)
    vault_key = st.text_input("سمي الله و افتحي", type="password")
    if st.button("Open Vault", use_container_width=True):
        if vault_key == "3122025":
            st.session_state.viewing_private = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
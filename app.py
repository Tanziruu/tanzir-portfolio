import streamlit as st

# ১. পেজ কনফিগ - ডার্ক থিম মোড
st.set_page_config(page_title="Tanzir Ahmed", layout="centered")

# ২. অ্যাপল-স্টাইল ডার্ক মোড ও মডার্ন লেআউট সিএসএস
st.markdown("""
    <style>
    .stApp {background-color: #000000; color: #ffffff;}
    h1, h2, h3 {color: #ffffff !important; font-weight: 600 !important;}

    /* বাটন ডিজাইন - অ্যাপল স্টাইল */
    div.stButton > button {
        background-color: #1c1c1e;
        color: white;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 10px 20px;
        transition: 0.4s;
    }
    div.stButton > button:hover {
        background-color: #333;
        transform: scale(1.05);
    }
    /* লিংক বাটনের জন্য একই ডিজাইন */
    a[href] {text-decoration: none !important;}

    /* হাইড ব্র্যান্ডিং */
    [data-testid="stToolbarActions"], footer, [data-testid="stFooter"], header {display: none;}
    </style>
""", unsafe_allow_html=True)

# ৩. নেভিগেশন
menu = st.sidebar.radio("Navigate", ["Home", "Skills", "Projects", "Contact"])

# ৪. হোম পেজ (ফ্যান্সি লুক)
if menu == "Home":
    st.markdown("<h1 style='text-align: center; font-size: 50px;'>Tanzir Ahmed</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>CSE Student | Developer | Innovator</p>",
                unsafe_allow_html=True)

    st.write("\n\n")
    # স্মুথ অ্যানিমেটেড টেক্সট ইফেক্ট
    st.markdown("""
    <div style='text-align: center; padding: 20px; border-left: 2px solid #0071e3;'>
        <h3 style='color: #0071e3;'>Welcome to my domain.</h3>
        <p>Crafting high-performance digital experiences with C++, Python, and modern web tech.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("\n\n")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Projects"):
            st.switch_page("app.py")  # এখানে নেভিগেশন লজিক
    with col2:
        if st.button("📩 Contact Me"):
            st.balloons()

# ৫. স্কিলস ও প্রজেক্টের জন্য মডার্ন কার্ড ডিজাইন
elif menu == "Skills":
    st.title("My Arsenal")
    cols = st.columns(3)
    skills = ["Python", "C++", "Cybersecurity"]
    for i, skill in enumerate(skills):
        cols[i].markdown(
            f"<div style='background:#1c1c1e; padding:20px; border-radius:10px; text-align:center;'>{skill}</div>",
            unsafe_allow_html=True)

# ৬. প্রজেক্টস
elif menu == "Projects":
    st.title("Work Showcase")
    st.info("Explore my GitHub to see the code behind the magic.")
    st.link_button("View on GitHub", "https://github.com/Tanziruu")
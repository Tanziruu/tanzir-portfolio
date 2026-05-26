import streamlit as st

# --- ১. পেজ কনফিগারেশন (ব্রাউজার ট্যাব নাম ও আইকন) ---
st.set_page_config(page_title="Tanzir's Portfolio", page_icon="💻", layout="centered")

# --- ২. সিএসএস ট্রিক (সব পেজের জন্য ব্র্যান্ডিং হাইড করার চেষ্টা) ---
hide_streamlit_style = """
            <style>
            /* ওপরে ডানদিকের Fork, GitHub লোগো এবং থ্রি-ডট মেনু হাইড করার জন্য */
            [data-testid="stToolbarActions"] {visibility: hidden; display: none;}
            .stAppToolbar {visibility: hidden; display: none;}

            /* নিচের সেই লাল রঙের Hosted with Streamlit ফুটার এবং কিং আইকন সরানোর জন্য */
            footer {visibility: hidden; display: none;}
            [data-testid="stFooter"] {visibility: hidden; display: none;}
            div[class^="st-emotion-cache"] footer {visibility: hidden; display: none;}

            /* ওপরের এক্সট্রা সাদা/কালো হেডার স্পেস মুছে ফেলার জন্য */
            header {visibility: hidden; display: none;}
            [data-testid="stHeader"] {visibility: hidden; display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- ৩. সাইডবার নেভিগেশন ---
menu = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Contact"])

# ================= HOME PAGE =================
if menu == "Home":
    st.title("Hi, I'm Tanzir Ahmed")
    st.subheader("Computer Science & Engineering Student")

    st.write(
        """
        Welcome to my personal portfolio! I am a passionate CSE student and programmer 
        who loves exploring new technologies, solving analytical problems, and building 
        custom coding solutions. 

        Currently, I am actively honing my skills in Python, C++, and various technical software 
        tools to build impactful projects.
        """
    )
    st.info("Use the sidebar menu on the left to navigate through my skills and projects.")

    # --- কাস্টম HTML Lottie অ্যানিমেশন (কোনো এক্সট্রা লাইব্রেরি লাগবে না) ---
    lottie_html = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <lottie-player src="https://lottie.host/9f518a4a-1dfc-473d-9d4a-9db171c6dd6d/YI9zU8M7e7.json" 
            background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay>
        </lottie-player>
    </div>
    """
    st.components.v1.html(lottie_html, height=330)

    st.markdown("---")

    # --- ইন্টারঅ্যাক্টিভ বাটন এবং ক্লিক অ্যাকশন (ম্যাজিক ইফেক্ট) ---
    st.subheader("Connect With Me ✨")
    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "🌐 Visit My GitHub Profile",
            "https://github.com/Tanziruu",
            use_container_width=True,
        )

    with col2:
        if st.button("Click for Magic! 🎈", use_container_width=True):
            st.balloons()
            st.success("Welcome to my tech space!")

# ================= SKILLS PAGE =================
elif menu == "Skills":
    st.title("My Technical Skills")

    st.markdown("### Programming Languages")
    st.write("- **C++** (Core Programming, OOP & Problem Solving)")
    st.write("- **Python** (Automation, Scripting & Web Apps)")
    st.write("- **Dart** (App Development)")

    st.markdown("### Tools & Software")
    st.write("- **IDEs:** PyCharm, VS Code, Code::Blocks")
    st.write("- **Version Control:** Git & GitHub")
    st.write("- **Technical Tools:** PSpice (Circuit Analysis)")
    st.write("- **Multimedia Tools:** Adobe Premiere Pro, OBS Studio, FL Studio")

# ================= PROJECTS PAGE =================
elif menu == "Projects":
    st.title("My Projects")

    # Project 1
    st.markdown("### 1. Personal Portfolio Website")
    st.write("A clean, modern personal portfolio built using Python and Streamlit, completely hosted on the cloud.")
    st.link_button("View Source Code (GitHub)", "https://github.com/Tanziruu", key="p1")

    st.markdown("---")

    # Project 2
    st.markdown("### 2. Circuit Analysis Simulation")
    st.write(
        "Conducted detailed circuit analysis and DC Sweep simulations using PSpice software for academic milestones.")
    st.button("View Details", key="p2")

# ================= CONTACT PAGE =================
elif menu == "Contact":
    st.title("Get In Touch")
    st.write("Feel free to reach out to me for collaboration, project ideas, or just a tech chat!")

    st.write("- **Location:** Demra, Dhaka, Bangladesh")
    st.write("- **GitHub:** [github.com/Tanziruu](https://github.com/Tanziruu)")
    st.write("- **LinkedIn:** [linkedin.com/in/tanzir-ahmed](https://linkedin.com)")
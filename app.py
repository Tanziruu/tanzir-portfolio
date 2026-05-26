import streamlit as st

# --- ১. পেজ কনফিগারেশন ---
st.set_page_config(page_title="Tanzir's Portfolio", page_icon="💻", layout="centered")

# --- ২. সিএসএস ট্রিক (সব ব্র্যান্ডিং হাইড করার জন্য) ---
hide_streamlit_style = """
            <style>
            [data-testid="stToolbarActions"], .stAppToolbar, footer, 
            [data-testid="stFooter"], header, [data-testid="stHeader"] 
            {visibility: hidden; display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- ৩. সাইডবার ---
menu = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Contact"])

# --- ৪. হোম পেজ (অ্যানিমেশনসহ) ---
if menu == "Home":
    st.title("Hi, I'm Tanzir Ahmed")
    st.subheader("Computer Science & Engineering Student")
    st.write("Welcome to my personal portfolio! Passionate about coding and building custom solutions.")

    # HTML Lottie Animation (সবচেয়ে স্মুথ ও আধুনিক পদ্ধতি)
    lottie_html = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <div style="display: flex; justify-content: center;">
        <lottie-player src="https://assets10.lottiefiles.com/packages/lf20_4sp5w0d9.json" 
            background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay>
        </lottie-player>
    </div>
    """
    st.components.v1.html(lottie_html, height=320)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🌐 GitHub Profile", "https://github.com/Tanziruu", use_container_width=True)
    with col2:
        if st.button("Click for Magic! 🎈", use_container_width=True):
            st.balloons()
            st.success("Welcome!")

# --- ৫. বাকি পেজগুলো ---
elif menu == "Skills":
    st.title("My Technical Skills")
    st.write("- **C++** (Core Programming)\n- **Python** (Automation)\n- **Dart** (App Dev)")

elif menu == "Projects":
    st.title("My Projects")
    st.write("### 1. Portfolio Website")
    st.link_button("View Source", "https://github.com/Tanziruu")

elif menu == "Contact":
    st.title("Get In Touch")
    st.write("Email: tanzir@example.com")
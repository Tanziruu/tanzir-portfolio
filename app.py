import streamlit as st

# Website Browser Tab Settings
st.set_page_config(page_title="Tanzir's Portfolio", page_icon="💻", layout="centered")

# Sidebar Navigation (Removed complex emojis to fix box icons)
menu = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Contact"])

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
    st.markdown("---")
    st.info("Use the sidebar menu on the left to navigate through my skills and projects.")

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

elif menu == "Projects":
    st.title("My Projects")

    # Project 1
    st.markdown("### 1. Personal Portfolio Website")
    st.write("A clean, modern personal portfolio built using Python and Streamlit, completely hosted on the cloud.")
    st.button("View Source Code (GitHub)", key="p1")

    st.markdown("---")

    # Project 2
    st.markdown("### 2. Circuit Analysis Simulation")
    st.write(
        "Conducted detailed circuit analysis and DC Sweep simulations using PSpice software for academic milestones.")
    st.button("View Details", key="p2")

elif menu == "Contact":
    st.title("Get In Touch")
    st.write("Feel free to reach out to me for collaboration, project ideas, or just a tech chat!")

    st.write("- **Location:** Demra, Dhaka, Bangladesh")
    st.write("- **GitHub:** [github.com/Tanziruu](https://github.com)")  # এখানে তোমার আসল ইউজারনেম দিয়ে নিও
    st.write("- **LinkedIn:** [linkedin.com/in/tanzir-ahmed](https://linkedin.com)")

    # পিসি ও মোবাইল উভয় ডিভাইসের সব স্ট্রিমলিট ব্র্যান্ডিং হাইড করার জন্য চূড়ান্ত CSS
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden; display: none;}
                footer {visibility: hidden; display: none;}
                header {visibility: hidden; display: none;}
                .stAppDeployButton {visibility: hidden; display: none;}
                [data-testid="stStatusWidget"] {visibility: hidden; display: none;}
                div[class^="st-emotion-cache"] footer {visibility: hidden; display: none;}
                button[title="View Streamlit app"] {visibility: hidden; display: none;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
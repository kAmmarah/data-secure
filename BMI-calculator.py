import streamlit as st
import base64

# 🎨 Page Config
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 🌆 Background Image Function
def set_bg_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    bg_css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0);
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

# 🖼️ Set Background
set_bg_image("background.jpg")  # Make sure this image is in the same folder

# 🏷️ Show Logo
st.image("logo.png", width=250, use_container_width=False)  # Make sure logo.png is also in the same folder

# 🌟 Title
st.markdown("<h1 style='text-align: center; color: white;'>⚖️ BMI Calculator</h1>", unsafe_allow_html=True)

# 🧍 Input Section
st.markdown("## 📏 Enter Your Details")

height = st.number_input("Enter your height in meters (e.g., 1.75):", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Enter your weight in kilograms (e.g., 70):", min_value=10.0, max_value=300.0, step=0.1)

# ➕ Calculate Button
if st.button("Calculate BMI 💡"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # 🧠 BMI Result Interpretation
        if bmi < 18.5:
            st.info("You are **Underweight** 🦴")
        elif 18.5 <= bmi < 24.9:
            st.success("You are in the **Normal range** 💪")
        elif 25 <= bmi < 29.9:
            st.warning("You are **Overweight** ⚠️")
        else:
            st.error("You are in the **Obese range** 🚨")
    else:
        st.error("Height must be greater than 0.")

# 📌 Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: white;'>Made with ❤️ by Ammara Dawood</p>",
    unsafe_allow_html=True
)
# 
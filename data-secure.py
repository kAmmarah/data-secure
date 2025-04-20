# import streamlit as st
# import base64

# # 🌠 Page Configuration
# st.set_page_config(page_title="Data Secure", layout="wide")

# # 🌄 Background Image Setup
# def set_background(image_file):
#     with open(image_file, "rb") as image:
#         encoded = base64.b64encode(image.read()).decode()
#     st.markdown(f"""
#          <style>
#          .stApp {{
#              background-image: url("data:image/png;base64,{encoded}");
#              background-size: cover;
#          }}
#          </style>
#          """, unsafe_allow_html=True)

# # 🔷 Set Background
# set_background("bg_image.jpg")  # 💡 Replace with your background image file

# # 🎨 Animated Logo and Title
# st.markdown("""
# <h1 style='text-align: center; color: #FF69B4; animation: pulse 2s infinite;'>🔐 Data Secure</h1>
# <h4 style='text-align: center;'>✨ Created by <b>Ammara Dawood</b> ✨</h4>
# <style>
# @keyframes pulse {
#   0% { transform: scale(1); }
#   50% { transform: scale(1.05); }
#   100% { transform: scale(1); }
# }
# </style>
# """, unsafe_allow_html=True)

# # 🌐 Navbar (via sidebar)
# selected_page = st.sidebar.radio("📂 Navigate", ["🔓 Register", "🔑 Login"])

# # 📦 Temporary user storage (for demo)
# if 'users' not in st.session_state:
#     st.session_state['users'] = {}

# # 📝 Register
# if selected_page == "🔓 Register":
#     st.subheader("📝 Create your account")
#     new_user = st.text_input("👤 Username")
#     new_pass = st.text_input("🔑 Password", type="password")
#     if st.button("📥 Register"):
#         if new_user in st.session_state['users']:
#             st.warning("⚠️ Username already exists.")
#         else:
#             st.session_state['users'][new_user] = new_pass
#             st.success("🎉 Registered successfully! You can now log in.")

# # 🔑 Login
# elif selected_page == "🔑 Login":
#     st.subheader("🔐 Login to your account")
#     username = st.text_input("👤 Username")
#     password = st.text_input("🔑 Password", type="password")
#     if st.button("🚪 Login"):
#         if username in st.session_state['users'] and st.session_state['users'][username] == password:
#             st.success(f"✅ Welcome back, {username}!")
#             st.balloons()
#         else:
#             st.error("❌ Invalid credentials. Try again!")

# # 👣 Footer
# st.markdown("""
# <hr>
# <p style='text-align: center;'>💻 This app is beautifully created by <b>Ammara Dawood</b> 🌟</p>
# """, unsafe_allow_html=True)





import streamlit as st
import base64

# 🌠 Page Setup
st.set_page_config(page_title="Data Secure", layout="wide")

# 🌄 Background Image Function
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,{encoded}");
             background-size: cover;
             background-position: center;
         }}
         </style>
         """, unsafe_allow_html=True)

# 🔷 Set Background
set_background("bg_image.jpg")  # Replace with your image

# 🎨 Animated Logo in Light Blue & Cyan
st.markdown("""
<div style="text-align:center; padding: 20px;">
  <h1 style="font-size: 50px; color: #00BFFF; animation: glow 2s infinite;">🔐 Data-Secure</h1>
  <h3 style="color: #40E0D0;">✨ Created by <b>Ammara</b> ✨</h3>
</div>

<style>
@keyframes glow {
  0% { text-shadow: 0 0 5px #1E90FF; }
  50% { text-shadow: 0 0 20px #00BFFF, 0 0 30px #1E90FF; }
  100% { text-shadow: 0 0 5px #1E90FF; }
}
</style>
""", unsafe_allow_html=True)

# 🌐 Top Navbar in Dark Blue
st.markdown("""
<style>
.navbar {
    background-color: #001f3f;
    padding: 12px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 30px;
}
.navbar a {
    margin: 0px 20px;
    color: #ADD8E6;
    font-weight: bold;
    font-size: 18px;
    text-decoration: none;
}
.navbar a:hover {
    color: #00BFFF;
}
</style>

<div class="navbar">
  <a href="#register">📝 Register</a>
  <a href="#login">🔐 Login</a>
</div>
""", unsafe_allow_html=True)

# 📦 Session for demo users
if 'users' not in st.session_state:
    st.session_state['users'] = {}

# 🔓 Registration Section
st.markdown("<h2 id='register' style='color:#1E90FF;'>📝 Register</h2>", unsafe_allow_html=True)
new_user = st.text_input("👤 Username")
new_pass = st.text_input("🔑 Password", type="password")
if st.button("📥 Register"):
    if new_user in st.session_state['users']:
        st.warning("⚠️ Username already exists.")
    else:
        st.session_state['users'][new_user] = new_pass
        st.success("🎉 Registered successfully! You can now log in.")

# 🔑 Login Section
st.markdown("<h2 id='login' style='color:#1E90FF;'>🔐 Login</h2>", unsafe_allow_html=True)
username = st.text_input("👤 Username", key="login_user")
password = st.text_input("🔑 Password", type="password", key="login_pass")
if st.button("🚪 Login"):
    if username in st.session_state['users'] and st.session_state['users'][username] == password:
        st.success(f"✅ Welcome back, {username}!")
        st.balloons()
    else:
        st.error("❌ Invalid credentials. Please try again.")

# 💙 Footer
st.markdown("""
<hr>
<p style='text-align: center; color: #87CEFA;'>💻 This app is beautifully created by <b>Ammara Dawood</b> 💖</p>
""", unsafe_allow_html=True)

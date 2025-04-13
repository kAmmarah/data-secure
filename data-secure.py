import streamlit as st
from cryptography.fernet import Fernet
import hashlib
import base64

# ----- In-memory database -----
data_store = {}
failed_attempts = 0
reauth_required = False

# ----- Generate a Fernet key -----
def generate_key(passkey):
    hashed = hashlib.sha256(passkey.encode()).digest()
    return base64.urlsafe_b64encode(hashed[:32])

# ----- Encrypt data -----
def encrypt_data(text, passkey):
    key = generate_key(passkey)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode())
    return encrypted

# ----- Decrypt data -----
def decrypt_data(encrypted_text, passkey):
    try:
        key = generate_key(passkey)
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_text).decode()
    except:
        return None

# ----- Style -----
def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64.b64encode(open("background.jpg", "rb").read()).decode()}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True
    )

def show_logo():
    st.image("logo.png", width=100)

# ----- Pages -----
def home():
    show_logo()
    st.title("🔐 Secure Data Storage")
    st.markdown("Welcome! Please choose an action:")
    if st.button("📥 Store New Data"):
        st.session_state.page = "store"
    if st.button("🔍 Retrieve Data"):
        st.session_state.page = "retrieve"

def store_data():
    show_logo()
    st.title("📥 Store Your Secret Data")
    text = st.text_area("Enter data to encrypt:")
    passkey = st.text_input("Enter a passkey (keep it safe):", type="password")
    if st.button("Encrypt & Save"):
        if text and passkey:
            hash_key = hashlib.sha256(passkey.encode()).hexdigest()
            encrypted = encrypt_data(text, passkey)
            data_store[hash_key] = encrypted
            st.success("✅ Data stored securely!")
        else:
            st.warning("Please enter both data and passkey.")
    if st.button("🔙 Back"):
        st.session_state.page = "home"

def retrieve_data():
    global failed_attempts, reauth_required
    show_logo()
    st.title("🔍 Retrieve Your Secret Data")

    if failed_attempts >= 3:
        reauth_required = True
        st.session_state.page = "login"
        return

    passkey = st.text_input("Enter your passkey:", type="password")
    if st.button("Retrieve"):
        if passkey:
            hash_key = hashlib.sha256(passkey.encode()).hexdigest()
            if hash_key in data_store:
                decrypted = decrypt_data(data_store[hash_key], passkey)
                if decrypted:
                    st.success("🔓 Your data:")
                    st.code(decrypted)
                    failed_attempts = 0  # reset on success
                else:
                    failed_attempts += 1
                    st.error(f"❌ Incorrect passkey! Attempts left: {3 - failed_attempts}")
            else:
                failed_attempts += 1
                st.error(f"❌ No data found or incorrect key! Attempts left: {3 - failed_attempts}")
        else:
            st.warning("Please enter a passkey.")
    if st.button("🔙 Back"):
        st.session_state.page = "home"

def login():
    global failed_attempts, reauth_required
    show_logo()
    st.title("🔐 Reauthorization Required")
    st.warning("⚠️ Too many failed attempts. Please login to continue.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # simple reauth
            failed_attempts = 0
            reauth_required = False
            st.success("✅ Reauthorized!")
            st.session_state.page = "home"
        else:
            st.error("Invalid credentials!")

# ----- Main App -----
def main():
    set_bg()
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home()
    elif st.session_state.page == "store":
        store_data()
    elif st.session_state.page == "retrieve":
        retrieve_data()
    elif st.session_state.page == "login":
        login()

    # About section always shown at the bottom
    st.markdown("""
    ---
    ### ℹ️ About This App
    This app allows users to securely store and retrieve secret data using their own passkeys.

    🔐 **How it works:**
    - Data is encrypted with your unique passkey using the **Fernet encryption** method.
    - Only the correct passkey can decrypt the data.
    - After 3 failed attempts, reauthorization is required to ensure security.

    🧠 **No data is stored externally** – everything is in memory and erased when the app restarts.

    ✅ Designed and created by: **Ammara Dawod**
    """)

if __name__ == "__main__":
    main()




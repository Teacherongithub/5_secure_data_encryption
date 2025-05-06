import streamlit as st
from encryption_utils import hash_passkey, encrypt_data, decrypt_data
from auth_utils import check_login, get_failed_attempts, increment_failed_attempts, reset_failed_attempts
from session_state import init_session_state

# In-memory storage
stored_data = {}

# Initialize session
init_session_state()

st.title("🔒 Secure Data Encryption System")

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            hashed_passkey = hash_passkey(passkey)

            if encrypted_text in stored_data and stored_data[encrypted_text]["passkey"] == hashed_passkey:
                decrypted_text = decrypt_data(encrypted_text)
                reset_failed_attempts()
                st.success(f"✅ Decrypted Data: {decrypted_text}")
            else:
                increment_failed_attempts()
                attempts_left = 3 - get_failed_attempts()
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")

                if get_failed_attempts() >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if check_login(login_pass):
            reset_failed_attempts()
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")

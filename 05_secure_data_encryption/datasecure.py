import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# Data file & constants
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOCKOUT_DURATION = 60

# Initialize session state
if "authenticated_user" not in st.session_state:
    st.session_state.authenticated_user = None
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# Load & Save Data Functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Key Generation and Password Hashing
def generate_key(passkey):
    key = pbkdf2_hmac('sha256', passkey.encode(), SALT, 100000)
    return urlsafe_b64encode(key)

def hash_password(password):
    return pbkdf2_hmac('sha256', password.encode(), SALT, 100000).hex()

# Encryption and Decryption Functions
def encrypt_text(text, passkey):
    try:
        key = generate_key(passkey)
        cipher = Fernet(key)
        return cipher.encrypt(text.encode()).decode()
    except Exception as e:
        return None

def decrypt_text(encrypted_text, passkey):
    try:
        key = generate_key(passkey)
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_text.encode()).decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

# App UI
stored_data = load_data()
st.title("🔒 Secure Data Encryption System")
menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("📋 Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to The Secure Data System")
    st.markdown("""
        ### 💡 Features:
        - 🔐 Encrypt your sensitive data securely.
        - 💾 Store encrypted information safely.
        - 🔓 Retrieve and decrypt your data anytime.
        - 🚨 Secure login system with lockout protection.

        ⚠️ **Note:** Remember your encryption key. Without it, your data cannot be decrypted!

        ---
        👉 Select an option from the sidebar to begin.
    """)

elif choice == "Register":
    st.subheader("📝 Register New User")
    username = st.text_input("👤 Choose Username")
    password = st.text_input("🔑 Choose Password:", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ User already exists!")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User registered successfully!")
        else:
            st.error("❌ Both fields are required.")

elif choice == "Login":
    st.subheader("🔑 User Login")

    if time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"🚫 Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username in stored_data and hash_password(password) == stored_data[username]["password"]:
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"🎉 Welcome {username}! You have successfully logged in.")
        else:
            st.session_state.failed_attempts += 1
            remaining = 3 - st.session_state.failed_attempts
            st.error(f"❌ Invalid username or password! Attempts left: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.lockout_time = time.time() + LOCKOUT_DURATION
                st.error("🚫 Too many failed attempts. Login locked for 60 seconds.")
                st.stop()

elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("⚠️ Please login first.")
    else:
        st.subheader("💾 Store Encrypted Data")
        data = st.text_area("📝 Enter data to encrypt")
        passkey = st.text_input("🔑 Encryption Key (passphrase)", type="password")

        if st.button("Encrypt And Save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                if encrypted:
                    stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                    save_data(stored_data)
                    st.success("✅ Data encrypted and saved successfully!")
                else:
                    st.error("❌ Encryption failed.")
            else:
                st.error("❌ All fields are required.")

elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("⚠️ Please login first.")
    else:
        st.subheader("🔓 Retrieve Encrypted Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("ℹ️ No data found.")
        else:
            st.write("📄 **Encrypted Data Entries:**")
            for index, item in enumerate(user_data, start=1):
                st.code(f"{index}: {item}", language="text")

            encrypted_input = st.text_area("🔒 Enter the Encrypted Text to Decrypt").strip()
            passkey = st.text_input("🔑 Enter Passkey (Decryption Key)", type="password")

            # Auto-clean: remove index prefix if pasted
            if ':' in encrypted_input:
                parts = encrypted_input.split(":", 1)
                if parts[0].strip().isdigit():
                    encrypted_input = parts[1].strip()

            if st.button("Decrypt"):
                if encrypted_input and passkey:
                    result = decrypt_text(encrypted_input, passkey)
                    if result:
                        st.success(f"✅ Decrypted Data Successfully!: {result}")
                    else:
                        st.error("❌ Decryption failed. Check your passkey or encrypted text.")
                else:
                    st.error("❌ Both Encrypted Text and Passkey are required.")

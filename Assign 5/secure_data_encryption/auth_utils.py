import streamlit as st

def check_login(password):
    return password == "admin123"  # Replace with secure mechanism in production

def get_failed_attempts():
    return st.session_state.get("failed_attempts", 0)

def increment_failed_attempts():
    st.session_state.failed_attempts = get_failed_attempts() + 1

def reset_failed_attempts():
    st.session_state.failed_attempts = 0

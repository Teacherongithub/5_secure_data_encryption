import streamlit as st

def init_session_state():
    if "failed_attempts" not in st.session_state:
        st.session_state.failed_attempts = 0

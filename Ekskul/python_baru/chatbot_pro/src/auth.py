import streamlit as st
from src.database import login_user, add_user

def auth_page():
    st.header("🤖 AI Assistant Pro")
    
    # AUTH CONTAINER
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.subheader("Login / Register")
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            with st.form("login_form"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                st.markdown("<br>", unsafe_allow_html=True)
                submit = st.form_submit_button("Login", use_container_width=True)
                
                if submit:
                    if login_user(username, password):
                        st.success(f"Welcome back, {username}!")
                        st.session_state["logged_in"] = True
                        st.session_state["username"] = username
                        st.rerun()
                    else:
                        st.error("Invalid username or password")

        with tab2:
            with st.form("register_form"):
                new_user = st.text_input("New Username")
                new_pass = st.text_input("New Password", type="password")
                confirm_pass = st.text_input("Confirm Password", type="password")
                st.markdown("<br>", unsafe_allow_html=True)
                submit_reg = st.form_submit_button("Register", use_container_width=True)
                
                if submit_reg:
                    if new_pass != confirm_pass:
                        st.error("Passwords do not match!")
                    elif add_user(new_user, new_pass):
                        st.success("Account created! Please login.")
                    else:
                        st.error("Username already taken")
        
        st.markdown('</div>', unsafe_allow_html=True)

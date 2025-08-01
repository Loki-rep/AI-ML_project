import streamlit as st
from src.services.service1 import get_dinner_idea

def main_router():
    st.set_page_config(page_title="What's for Dinner?")
    st.title("🍽️ What's for Dinner?")

    user_input = st.text_input("What ingredients do you have or mood are you in?")

    if st.button("Get Dinner Idea"):
        if not user_input.strip():
            st.warning("Please enter something.")
        else:
            with st.spinner("Thinking..."):
                suggestion = get_dinner_idea(user_input)
                st.success(f"Suggestion:\n\n{suggestion}")

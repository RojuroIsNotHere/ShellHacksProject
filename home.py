# pages/home.py
import streamlit as st

def display():
    st.title("Welcome to QuoteMates!")

    st.subheader("Features:")
    st.write(
        "- **Health Insurance Quotes:** Get estimates based on your age, pre-existing conditions, and desired coverage.\n"
        "- **Auto Insurance Quotes:** Calculate quotes based on vehicle age, value, and coverage type.\n"
        "- **Renters Insurance Quotes:** Estimate coverage based on your rental type and personal property value.\n"
        "- **User-Friendly Interface:** Our design makes it easy to navigate through different insurance options."
    )

    st.subheader("How It Works:")
    st.write(
        "1. Navigate to the desired insurance type using the sidebar.\n"
        "2. Fill out the required information.\n"
        "3. Click the button to receive your quote!\n"
        "4. Reach out to us through the Contact page for any questions."
    )
    
    st.write("Thank you for visiting our application. We hope you find the information you need!")

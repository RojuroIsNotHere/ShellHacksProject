# pages/about.py
import streamlit as st

def display():
    st.title("About Us")
    st.write(
        "This application was created by a dedicated team for ShellHacks 2024. "
        "Our goal is to provide users with quick insurance quotes "
        "for health, auto, and renters insurance."
    )
    
    st.subheader("Team Members:")
    team_members = [
        "1. ",
        "2. Giordano Galarce",
        "3. Kristian Valuyskiy"
    ]
    
    for member in team_members:
        st.write(member)

    st.write(
        "Thank you for using our application, and we hope you find it helpful!"
    )

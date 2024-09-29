import streamlit as st

def display():
    
    st.subheader("Contact Us")
    st.write("If you have any questions about our service, feel free to let us know.")
    
    with st.form("Email Form"):
    
        fullName = st.text_input(label="Full Name", placeholder = "Please enter your full name")
    
        email = st.text_input(label="Email Address", placeholder = "Please enter your email address")
    
        text = st.text_area(label="Comments", placeholder = "Please enter your comments")
    
        submit_res = st.form_submit_button(label="Send")

        if submit_res:

          st.success("Thank you! We will get back to you ASAP!")

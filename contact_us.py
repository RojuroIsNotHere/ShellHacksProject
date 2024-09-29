import streamlit as st

def send_email(message):
  st.write(message)

def display():

  message = "I am coming from Streamlit"
    
  with st.form("Email Form"):
    fullName = st.text_input(label="Full Name", placeholder = "Please enter your full name")
    email = st.text_input(label="Email Address", placeholder = "Please enter your email address")
    text = st.text_input(label="Comments", placeholder = "Please enter your comments")
    submit_res = st.form_submit_button(label="Send")

  send_email(message)

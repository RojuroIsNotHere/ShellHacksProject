import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender, password, receiver, smtp_server, smtp_port, email_message, subject):
  message = MIMEMultipart()
  message['To'] = Header(receiver)
  message['From'] = Header(sender)
  message['Subject'] = Header(subject)
  message.attach(MIMEText(email_message), 'plain', 'utf-8')

  server = smtplib.SMTP(smtp_server, smtp_port)
  server.starttls()
  server.ehlo()
  server.login(sender, password)
  text = message.as_string()
  server.sendemail(sender, reciever, text)
  server.quit()

def display():
    
  with st.form("Email Form"):
    
    fullName = st.text_input(label="Full Name", placeholder = "Please enter your full name")
    
    email = st.text_input(label="Email Address", placeholder = "Please enter your email address")
    
    text = st.text_area(label="Comments", placeholder = "Please enter your comments")
    
    submit_res = st.form_submit_button(label="Send")

    if submit_res:

      extra_info = """
      -----------------------------------------------

      Email Address of sender {} \n

      Sender Full Name {} \n

      ----------------------------------------------- \n \n

      """.format(email, fullName)

      message = extra_info + text
    
      send_email("quotematescom@gmail", "#123098Wow", email, "smtp.gmail.com", 587, message, "Test Email for hackathon")

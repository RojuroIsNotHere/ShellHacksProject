import streamlit as st

st.title("My Streamlit App")

# Create a sidebar for navigation
menu = st.sidebar.selectbox("Select a page:", ["Home", "About", "Services", "Contact"])

# Home page
if menu == "Home":
    st.subheader("Welcome to the Home Page")
    st.write("This is the home section where you can provide an overview of your app.")

# About page
elif menu == "About":
    st.subheader("About Us")
    st.write("This section contains information about the app or the individual.")

# Services page
elif menu == "Services":
    st.subheader("Our Services")
    st.write("Here you can describe the services offered.")

# Contact page
elif menu == "Contact":
    st.subheader("Contact Us")
    st.write("Provide contact information or a contact form here.")
    # Example of a simple contact form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Submit"):
        st.success("Message sent!")

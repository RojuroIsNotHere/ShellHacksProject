import streamlit as st

st.title("My Streamlit App")

# Create a sidebar for navigation
menu = st.sidebar.selectbox("Select a page:", ["Home", "About", "Renters", "Contact"])

# Home page
if menu == "Home":
    st.subheader("Welcome to the Home Page")
    st.write("This is the home section where you can provide an overview of your app.")

# About page
elif menu == "About":
    st.subheader("About Us")
    st.write("This section contains information about the app or the individual.")

# Services page
elif menu == "Renters":
    st.subheader("Renters Insurance Estimate: Express")
    st.write("Take this quick survey to see your estimate!")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    address = st.text_input("Your Address")
    rental_type = st.text_input("Rental Type")
    est_prop_val = st.text_input("Estimated Value of Personal Property")
    desired_coverage = st.text_input("Desired Liability Coverage")

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

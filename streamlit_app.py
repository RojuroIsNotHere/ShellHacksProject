import streamlit as st
# Import individual pages
import home, about, health_quotes, auto_quotes, renter_quotes, contact_us, chatbot

# Create a custom sidebar for navigation
menu = st.sidebar.selectbox("Create a quote:", ["Home","About Us","Health Quotes", "Auto Quotes", "Renter Quotes", "Contact Us"])


# Render the corresponding page based on user selection
if menu == "Home":
    home.display()  # Display the home page
elif menu == "About Us":
    about.display()  # Display the about page
elif menu == "Health Quotes":
    health_quotes.display()  # Display the health quotes page
elif menu == "Auto Quotes":
    auto_quotes.display()  # Display the auto quotes page
elif menu == "Renter Quotes":
    renter_quotes.display()  # Display the renter quotes page
elif menu == "Contact":
    contact_us.display()


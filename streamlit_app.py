import streamlit as st

st.title("My Streamlit App")

# Create a sidebar for navigation
menu = st.sidebar.selectbox("Select a page:", ["Home", "About", "Health Quotes", "Auto Quotes", "Renter Quotes", "Contact"])

def calculate_health_quote(age, pre_existing, coverage_amount):
    base_rate = 0.05  # Base rate per $1000 coverage
    age_factor = 0.01  # Additional charge per year of age
    if pre_existing:
        base_rate += 0.02  # Additional charge for pre-existing conditions

    # Calculate total rate based on age
    total_rate = base_rate + (age_factor * (age - 18))  # Start charging from age 18
    return coverage_amount * total_rate

# Function to calculate Auto Insurance Quote
def calculate_auto_quote(vehicle_age, vehicle_value, coverage_type):
    base_rate = 0.03  # Base rate per $1000 vehicle value
    if coverage_type == "Comprehensive":
        base_rate += 0.01  # Additional charge for comprehensive coverage
    elif coverage_type == "Collision":
        base_rate += 0.015  # Additional charge for collision coverage
    return vehicle_value * base_rate

def calcRentEstimate(rental_type, est_prop_val, desired_coverage):
        rate = 0.0
        if rental_type == "Apartment":
            rate = 0.03
        if rental_type == "Condo":
            rate = 0.025
        if rental_type == "Townhouse":
            rate = 0.06
        if rental_type == "House":
            rate = 0.09
        return rate * desired_coverage * ( est_prop_val / 0.6 ) 


# Home page
if menu == "Home":
    st.subheader("Welcome to the Home Page")
    st.write("This is the home section where you can provide an overview of your app.")

# About page
elif menu == "About":
    st.subheader("About Us")
    st.write("This section contains information about the app or the individual.")

# Services page
# Health Insurance Page
elif menu == "Health Quotes":
   st.subheader("Health Insurance Estimate: Express")
   st.write("Take this quick survey to see your estimate!")
   age = st.number_input("Enter your age:", min_value=18, max_value=120)
   pre_existing = st.checkbox("Do you have any pre-existing medical conditions?")
   coverage_amount = st.number_input("Enter desired coverage amount ($):", min_value=1000)
   if st.button("Get Health Quote"):
        quote = calculate_health_quote(age, pre_existing, coverage_amount)
        st.success(f"Health Insurance Quote: ${quote:.2f}")
        st.balloons()

elif menu == "Auto Quotes":
   st.subheader("Auto Insurance Estimate: Express")
   st.write("Take this quick survey to see your estimate!")
   vehicle_age = st.number_input("Enter the age of your vehicle (in years):", min_value=0)
   vehicle_value = st.number_input("Enter the current value of your vehicle ($):", min_value=100)
   car_model_year = st.number_input("Enter your car's model year:", min_value=1900, max_value=2025)
   coverage_type = st.selectbox("Select the type of coverage:", ["Liability", "Comprehensive", "Collision"])
   if st.button("Get Auto Quote"):
        quote = calculate_auto_quote(vehicle_age, vehicle_value, coverage_type)
        st.success(f"Auto Insurance Quote: ${quote:.2f}")
        st.balloons()

# Renters Insurance Page
elif menu == "Renter Quotes":
    st.subheader("Renters Insurance Estimate: Express")
    st.write("Take this quick survey to see your estimate!")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    address = st.text_input("Your Address")
    rental_type = st.selectbox("Rental Type", ["Apartment", "Condo", "Townhouse", "House"])
    est_prop_val = st.number_input("Estimated Value of Personal Property")
    desired_coverage = st.number_input("Desired Liability Coverage")
    
    if st.button("Submit"):
        calc = calcRentEstimate(rental_type, est_prop_val, desired_coverage) 
        st.success(f"{calc}")

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


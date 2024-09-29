import streamlit as st
from calculations import calculate_auto_quote  # Import the calculation function

def display():
    st.subheader("Auto Insurance Estimate: Express")
    st.write("Take this quick survey to see your estimate!")

    vehicle_age = st.number_input("Enter the age of your vehicle (in years):", min_value=0)
    vehicle_value = st.number_input("Enter the current value of your vehicle ($):", min_value=100)
    coverage_type = st.selectbox("Select the type of coverage:", ["Liability", "Comprehensive", "Collision"])
    vehicle_type = st.selectbox("Select your vehicle type:", [
        "Sedan",
        "SUV",
        "Truck",
        "Van",
        "Sports Car"
    ])

    quote_frequency = st.selectbox("Select your quote frequency:", ["Monthly", "Yearly"])

    if st.button("Get Auto Quote"):
        quote = calculate_auto_quote(vehicle_age, vehicle_value, coverage_type, vehicle_type, quote_frequency)
        st.success(f"Auto Insurance Quote: ${quote:.2f}")
        st.balloons()

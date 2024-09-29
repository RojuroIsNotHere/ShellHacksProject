import streamlit as st
from utils.calculations import calcRentEstimate  # Import the calculation function

def display():
    st.subheader("Renters Insurance Estimate: Express")
    st.write("Take this quick survey to see your estimate!")

    rental_type = st.selectbox("Rental Type", ["Apartment", "Condo", "Townhouse", "House"])
    est_prop_val = st.number_input("Estimated Value of Personal Property", min_value=1000)
    desired_coverage = st.number_input("Desired Liability Coverage", min_value=1000)

    if st.button("Submit"):
        estimate = calcRentEstimate(rental_type, est_prop_val, desired_coverage)
        st.success(f"Renters Insurance Quote: ${estimate:.2f}")

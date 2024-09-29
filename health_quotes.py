import streamlit as st
from calculations import calculate_health_quote

def display():
    st.subheader("Health Insurance Estimate: Express")
    st.write("Take this quick survey to see your estimate!")

    age = st.number_input("Enter your age:", min_value=18, max_value=120)
    coverage_amount = st.number_input("Enter desired coverage amount ($):", min_value=1000)
    pre_existing = st.checkbox("Do you have any pre-existing medical conditions?")
    smoker = st.checkbox("Do you smoke?")

    quote_frequency = st.selectbox("Select quote frequency:", ["Monthly", "Yearly"])

    if st.button("Get Health Quote"):
        quote = calculate_health_quote(age, coverage_amount, pre_existing, smoker, quote_frequency)
        st.success(f"Health Insurance Quote: ${quote:.2f}")
        st.balloons()

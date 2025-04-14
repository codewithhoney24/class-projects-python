import streamlit as st
import pandas as pd  # Importing pandas for future data handling
import time

def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Streamlit UI
st.set_page_config(page_title="BMI Calculator", page_icon="💪")
st.title("💪 BMI Calculator")

# Weight slider (kg)
weight = st.slider("🏋️ Select your weight (kg)", min_value=10.0, max_value=200.0, value=70.0, step=0.1)

# Height slider (m)
height = st.slider("📏 Select your height (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)

if st.button("Calculate BMI 🧮"):
    if weight > 0 and height > 0:
        with st.spinner("Calculating..."):
            time.sleep(1.5)  # Simulating processing time
        
        bmi = calculate_bmi(weight, height)
        st.success(f"💡 Your BMI is: **{bmi:.2f}**")

        # Classification with colors
        if bmi < 18.5:
            st.warning("⚠️ You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight.")
        else:
            st.error("🚨 You are obese.")

        # Display BMI Reference Table
        st.markdown("""
        ### 📊 BMI Categories:
        | BMI Range        | Category          |
        |-----------------|------------------|
        | **< 18.5**      | Underweight      |
        | **18.5 - 24.9** | Normal Weight    |
        | **25 - 29.9**   | Overweight       |
        | **30+**         | Obese            |
        """)
    else:
        st.error("🚨 Please enter valid values for weight and height.")

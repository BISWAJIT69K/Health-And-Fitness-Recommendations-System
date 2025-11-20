import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dummy model (replace with real training if needed)
def train_model():
    # Create sample training data
    data = pd.DataFrame({
        'Duration': [20, 30, 40, 50, 60],
        'Heart Rate': [120, 130, 135, 140, 150],
        'Calories': [120, 190, 250, 310, 370]
    })
    X = data[['Duration', 'Heart Rate']]
    y = data['Calories']
    model = LinearRegression().fit(X, y)
    return model

model = train_model()

# Recommendation logic
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight – You should gain weight."
    elif 18.5 <= bmi < 24.9:
        return "Fit – Maintain your current weight."
    else:
        return "Overweight – You should lose weight."

# Streamlit UI
st.title("🏋️‍♂️ Health & Fitness Recommendation System")
st.markdown("Get personalized fitness advice based on your body metrics and workout.")

with st.form("user_input_form"):
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Current Weight (kg)", value=70)
    dream_weight = st.number_input("Dream Weight (kg)", value=65)
    height = st.number_input("Height (in meters)", value=1.7)
    duration = st.number_input("Workout Duration (minutes)", value=30)
    heart_rate = st.number_input("Heart Rate during workout", value=140)
    submitted = st.form_submit_button("Generate Recommendation")

if submitted:
    bmi = weight / (height ** 2)
    advice = get_bmi_category(bmi)
    calories = model.predict([[duration, heart_rate]])[0]

    st.subheader("📋 Recommendation Summary")
    st.markdown(f"**BMI:** {bmi:.2f}")
    st.markdown(f"**Advice:** {advice}")
    st.markdown(f"**Estimated Calories Burned:** {calories:.2f} kcal")

    st.success("Recommendation generated successfully!")

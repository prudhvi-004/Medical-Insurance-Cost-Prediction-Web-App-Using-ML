import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('C:/Users/prudh/OneDrive/Desktop/Machine Learning/Projects/Medical Insurance Cost Prediction/insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Medical Insurance Cost Predictor")
st.title("Medical Insurance Cost Prediction App")

# User inputs
age = st.number_input("Age", min_value=0, max_value=100, value=25)
sex = st.selectbox("Sex", options=["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=27.9)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", options=["yes", "no"])
region = st.selectbox("Region", options=["southeast", "southwest", "northeast", "northwest"])

# Encode inputs
sex_encoded = 0 if sex == "male" else 1
smoker_encoded = 0 if smoker == "yes" else 1
region_dict = {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}
region_encoded = region_dict[region]

# Combine into array
input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])

# Prediction
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ₹{prediction[0]:,.2f}")

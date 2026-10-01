import streamlit as st
import joblib
import numpy as np

st.title("Diabetes Prediction App")
st.write("Patient chi mahiti bhara ani prediction pahaa.")

model = joblib.load("model.pkl")

pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 300, 120)
bp = st.number_input("Blood Pressure", 0, 200, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):
    data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    result = model.predict(data)[0]
    if result == 1:
        st.error("Diabetic (Diabetes chi shakyata jast ahe)")
    else:
        st.success("Non-Diabetic (Diabetes nahi)")
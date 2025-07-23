import streamlit as st 
import requests

st.title("📝 Score Predictor ✅")
a = st.slider("Study Time",0,10)
b = st.slider("Attended Days",0,80)
gen = st.selectbox("Gender",["Male", "Female"])

gender = 1 if (gen=="Male") else 0 
if (st.button("Predict the score")):
    data = {
        "Study_time":a,
        "Attendence":b,
        "gender_Male":gender 
    }
    res = requests.post("http://127.0.0.1:8000/predict",json=data)
    result = res.json()
    st.write("The Pridicted Score is : ",result["Predicted_score"])
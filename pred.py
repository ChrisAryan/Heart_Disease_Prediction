import pickle
import streamlit as st
import streamlit_option_menu as option_menu

# loading the model
heart_model=pickle.load(open("heart-model.sav","rb"))

st.header("Heart Disease Prediction")

age=st.text_input("Age")
sex=st.text_input("Gender")
chestpain=st.text_input("CP")
trestbps=st.text_input("trestbps")
chol=st.text_input("chol")
fbs=st.text_input("fbs")
restecg=st.text_input("restecg")
thalach=st.text_input("thalach")
exang=st.text_input("exang")
oldpeak=st.text_input("oldpeak")
slope=st.text_input("slope")
ca=st.text_input("ca")
thal=st.text_input("thal")

#code for prediction
heart_diag=""

#creating a button for prediction
if(st.button("TestResult")):
    heart_pred=heart_model.predict([[age,sex,chestpain,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    if(heart_pred[0]==1):
        heart_diag="You have heart problems"
    else:
        heart_diag=" You don't have heart problems"
    st.success(heart_diag)

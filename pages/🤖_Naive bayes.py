import streamlit as st
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
data=pd.read_csv("diabetes2.csv")
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model = GaussianNB()
model.fit(x_train,y_train)
st.markdown("""
<style>
  .stApp {  /* Target the entire Streamlit app container */
    background-color: #92a1cf;
    color: black;
  }
</style>
""", unsafe_allow_html=True)
st.header("Naive Bayes for diabetes prediction")
st.subheader("Pregnancies:")
try:
    preg=float(st.text_input("Enter pregnancies count from 1 to 10:"))
except ValueError:
    st.error("Please enter a valid number.")
    preg = None
st.subheader("Glucose:")
try:
    glu=float(st.text_input("Enter glucose level from 80 to 180:"))
except ValueError:
    st.error("Please enter a valid number.")
    glu=None
st.subheader("Blood pressure:")
try:
    blood=float(st.text_input("Enter blood pressure 40 to 130:"))
except ValueError:
    st.error("Please enter a valid number.")
    blood=None
st.subheader("Skin Thickness:")
try:
    skin=float(st.text_input("Enter skin thickness from 0 to 50:"))
except ValueError:
    st.error("Please enter a valid number.")
    skin=None
st.subheader("Insulin level:")
try:
    ins=float(st.text_input("Enter insulin level:"))
except ValueError:
    st.error("Please enter a valid number")
    ins=None
st.subheader("BMI:")
try:
    bmi=float(st.text_input("Enter BMI from 20 to 50:"))
except ValueError:
    st.error("Please enter a valid number")
    bmi=None
st.subheader("Diabetes pedigree function")
try:
    dia=float(st.text_input("Enter diabetes pedigree function from 0 to 5:"))
except ValueError:
    st.error("Please enter a valid rating")
    dia=None
st.subheader("Age:")
try:
    age=float(st.text_input("Enter the age:"))
except ValueError:
    st.error("Please enter a valid number")
    age=None
if bmi:
    prediction=model.predict([[preg,glu,blood,skin,ins,bmi,dia,age]])
    if st.button('Predict'):
        st.success("Successfully predicted!")
        if prediction[0]==1:
            st.subheader("The Patient has diabetes")
        else:
            st.subheader("The Patient doesnt have diabetes")

import streamlit as st
import pandas as pd
import category_encoders as ce
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
df=pd.read_csv("car_evaluation.csv")
df=df.tail(100)
col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df.columns = col_names
x = df.drop(['class'], axis=1)
y = df['class']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 42)
encoder = ce.OrdinalEncoder(cols=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
x_train = encoder.fit_transform(x_train)
x_test = encoder.transform(x_test)
model= RandomForestClassifier(n_estimators= 10, criterion="entropy")  
model.fit(x_train,y_train)
st.markdown("""
<style>
  .stApp {  /* Target the entire Streamlit app container */
    background-color: #92a1cf;
    color: black;
  }
</style>
""", unsafe_allow_html=True)
st.header("Random forest for car classification")
st.subheader("Buyings:")
try:
    buy=float(st.text_input("Enter buying rating from 1 to 4:"))
except ValueError:
    st.error("Please enter a valid rating.")
    buy = None
st.subheader("Maintainance:")
try:
    maint=float(st.text_input("Enter Maintainace rating from 1 to 4:"))
except ValueError:
    st.error("Please enter a valid rating.")
    maint=None
st.subheader("Doors:")
try:
    doors=float(st.text_input("Enter Number of doors from 1 to 4:"))
except ValueError:
    st.error("Please enter a valid number of doors")
    doors=None
st.subheader("Persons:")
try:
    per=float(st.text_input("Enter Number of persons from 1 to 4:"))
except ValueError:
    st.error("Please enter a valid number of persons")
    per=None
st.subheader("Luggage Boot:")
try:
    lug=float(st.text_input("Enter Luggage Boot rating from 1 to 4:"))
except ValueError:
    st.error("Please enter a valid rating")
    lug=None
st.subheader("Safety:")
try:
    safe=float(st.text_input("Enter Safety rating from 1 to 4:"))
except ValueError:
    st.error("Please enter a valid rating")
    safe=None

prediction=model.predict([[buy,maint,doors,per,lug,safe]])
if st.button('Predict'):
    st.success("Successfully predicted!")
    st.subheader("Details about the car:")
    if prediction[0]=='good':
        st.subheader("The selected features of car is pretty good")
    elif prediction[0]=='vgood':
        st.subheader("The selected features of car is very good")
    elif prediction[0]=='acc':
        st.subheader("The Selected features of car is acceptable but not good")
    else:
        st.subheader("The Selected features of car is unacceptable")

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
col1,col2=st.columns(2)
data=pd.read_csv('Salary_Data.csv')
x=data[['YearsExperience']]
y=data['Salary']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
st.markdown("""
<style>
  .stApp {  /* Target the entire Streamlit app container */
    background-color: #92a1cf;
    color: black;
  }
</style>
""", unsafe_allow_html=True)
st.header("Linear Regression to predict Salary:")
try:
  exp = float(st.text_input("Enter the experience"))
except ValueError:
  st.error("Please enter a valid number for experience.")
  exp = None

if exp is not None:
  prediction = model.predict([[exp]])
  if st.button('Predict'):
    st.success("Successfully predicted!")
    st.subheader("Expected Salary:")
    st.write(prediction[0])

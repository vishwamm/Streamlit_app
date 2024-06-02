import pandas as pd
import streamlit as st
st.title("Dataset used in this website")
df1=pd.read_csv("car_evaluation.csv")
df1=df1.tail(100)
df2=pd.read_csv("diabetes2.csv")
df3=pd.read_csv("Mall_Customers.csv")
df4=pd.read_csv("Salary_Data.csv")
st.markdown("""
<style>
  .stApp {  /* Target the entire Streamlit app container */
    background-color: #92a1cf;
    color: black;
  }
</style>
""", unsafe_allow_html=True)
a,b=st.columns(2)
a.subheader("Mall customer.csv-Clustering")
a.write(df3)
a.subheader("Car eval.csv-Classification")
a.write(df1)
b.subheader("Diabetes.csv-Classification")
b.write(df2)
b.subheader("Salary data.csv-Regression")
b.write(df4)
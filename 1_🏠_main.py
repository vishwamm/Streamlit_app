import streamlit as st
from PIL import Image
img=Image.open("ml.jpeg")
import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
img=Image.open("ml.jpeg")
st.set_page_config(
    page_title="Machine Learning Website",
    page_icon=img)
st.markdown("""
<style>
  .stApp {  /* Target the entire Streamlit app container */
    background-color: #92a1cf;
    color: black;
  }
</style>
""", unsafe_allow_html=True)
st.header("DEMO FOR EVERY MACHINE LEARNING ALGORITHM!")
st.write("This interactive website lets you explore machine learning through experimentation!  It provides a user-friendly interface" 
         "built with Streamlit to perform regression, classification, and clustering tasks using various algorithms.")
col1, col2 = st.columns(2)
alg=['AdaBoost','DBSCAN clustering','Decision tree','Hierarchical clustering','K means clustering','KNN','Linear regression','Logistic regression'
     ,'Naive Bayes','XGBoost','Random Forest','SVM']
col1.header("Algorithms:")
for i in alg:
    col1.markdown('* **'+i+'**')
def load(file:str):
    with(open(file,'r')) as f:
        return json.load(f)
lottie=load('lottie_files/robot.json')
if lottie:
    with col2:
        st_lottie(lottie, height=400, width=None, key="lottie_animation")
        
    





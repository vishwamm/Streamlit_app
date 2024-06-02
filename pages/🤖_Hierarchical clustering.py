import streamlit as st
import pandas as pd  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:, [3, 4]].values
from sklearn.cluster import AgglomerativeClustering   
model= AgglomerativeClustering(n_clusters=5, linkage='ward')   
y_predict= model.fit_predict(x)
plt.scatter(x[:,0], x[:,1], c=y_predict)
plt.title('Clusters of customers')  
plt.xlabel('Annual Income (k$)')  
plt.ylabel('Spending Score (1-100)')  
plt.legend()
plt.savefig('h_cluster.png', bbox_inches='tight')
img='h_cluster.png'
st.markdown("""
<style>
  .stApp {  /* Target the entire Streamlit app container */
    background-color: #92a1cf;
    color: black;
  }
</style>
""", unsafe_allow_html=True)
st.header("Hierarchical  clustering")
st.write("Clustering is done based upon given Mall customer dataset")
st.subheader("Resulted image:")
st.image("k_cluster.png")
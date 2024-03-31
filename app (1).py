import pickle
import streamlit as st
iris_flower = pickle.load(open('iris.sav', 'rb'))
st.title('Iris Flower Prediction using ML')
col1, col2, col3,col4 = st.columns(4)
with col1:
    st.text("Sepal length")
    sepal_length = st.slider('Enter value', (4,7.91))
with col2:
  st.text("Sepal Width")
  sepal_width=st.slider('Enter value',(2.0,4.41))
with col3:
  st.text("petal length")
  petal_length=st.slider('Enter value',(1.0,6.91))
with col4:
  st.text("petal widht")
  petal_width =st.slider('Enter value',(.10,2.51))
if st.button("Predict type of Iris"):
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])     




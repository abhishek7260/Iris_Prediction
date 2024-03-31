import pickle
import streamlit as st


# Load the model
model = pickle.load(open('iris.sav', 'rb'))

# Set up the Streamlit app
st.title('Iris Flower Prediction using ML')

# Define columns for input fields
col1, col2, col3, col4 = st.columns(4)
# Input fields for Sepal Length, Sepal Width, Petal Length, and Petal Width
with col1:
    st.text("Sepal length")
    sepal_length = st.slider('Enter value', 4.0, 7.91)
with col2:
    st.text("Sepal Width")
    sepal_width = st.slider('Enter value', 2.0, 4.41)
with col3:
    st.text("Petal length")
    petal_length = st.slider('Enter value', 1.0, 6.91)
with col4:
    st.text("Petal width")
    petal_width = st.slider('Enter value', 0.10, 2.51)

# Prediction button
if st.button("Predict type of Iris"):
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.write(f"The predicted type of Iris is: {result}")

import streamlit as st
import pandas as pd
import numpy as np
import pickle

#load the model
model = pickle.load(open("iris_model.pkl",'rb'))
# App title
st.title("Iris flower classification app")
st.write("predict the species of iris flower using ML model")
#input fields
sepal_length = st.number_input("sepal_length(cm)", 4.0, 8.0, 5.4)
sepal_width = st.number_input("sepal_width(cm)", 2.0, 4.4, 3.4)
petal_length = st.number_input("petal_length(cm)", 1.0, 7.0, 4.5)
petal_width = st.number_input("petal_width(cm)", 0.1, 2.5, 1.3)
#predict button
if st.button("predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    species = ['Setusa','versicular','virginica']
    st.success (f"The predicted flower species is {species[prediction[0]]}")
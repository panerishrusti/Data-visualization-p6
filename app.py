import streamlit as st
import numpy as np

model=pickle.load(open('iris_model.pkl','rb'))

st.title('Iris Prediction and visualization')

sepal_length=st.slider("Sepal Length",4.0,8.0,5.0)
sepal_width=st.slider("Sepal width",2.0,4.5,3.0)

petal_length=st.slider("Petal Length",1.0,7.0,4.0)
petal_width=st.slider("Petal width",0.1,2.5,1.0)

input_data=np,array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction=model.predict(input_data)

species=['Setose','Versicolor','Verginica']

st.header('Prediction')
st.success(species[predicion[0]])
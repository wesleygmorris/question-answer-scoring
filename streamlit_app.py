import streamlit as st
import numpy as np

st.markdown('## Iris Species Prediction')
sepal_length = st.number_input('sepal length (cm)')
sepal_width = st.number_input('sepal width (cm)')
petal_length = st.number_input('petal length (cm)')
petal_width = st.number_input('petal width (cm)')
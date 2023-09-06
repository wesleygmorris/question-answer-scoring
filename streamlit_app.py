import streamlit as st
import pandas as pd
import numpy as np
from transformers import pipeline

pipe = pipeline('text-classification', model='tiedaar/short-answer-classification')
df = pd.read_csv('../data/subsections.csv')
sample_row = df.sample(n=1)

passage = sample_row['clean_text']
question = sample_row['question']

st.markdown('## Short answer scoring demonstration')
st.markdown('### Passage')
st.markdown(passage)

sepal_length = st.number_input('sepal length (cm)')
sepal_width = st.number_input('sepal width (cm)')
petal_length = st.number_input('petal length (cm)')
petal_width = st.number_input('petal width (cm)')
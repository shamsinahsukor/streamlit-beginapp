
import streamlit as st
import numpy as np
import pandas as pd

st.header("Sham's first Streamlit App")
st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))


st.header("About Diabetes")
from PIL import Image
image = Image.open('img-what-is-diabetes.jpg')

st.image(image, caption='What is diabetes Type')

st.write(pd.DataFrame({
    'Age Range': ['20's', '30's', '40's', '50's', '60's', '70's', '80's'],
    'Frequency': [240,78, 46, 25, 4, 1]
}))
    
 
st.header("Diabetes Types")
from PIL import Image
image = Image.open('diabetes-type.jpg')

st.image(image, caption='Diabetes Type')

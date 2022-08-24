
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

Age Range,Count of Age
20's,240
30's,78
40's,46
50's,25
60's,4
80's,1


st.header("Diabetes Types")
from PIL import Image
image = Image.open('diabetes-type.jpg')

st.image(image, caption='Diabetes Type')

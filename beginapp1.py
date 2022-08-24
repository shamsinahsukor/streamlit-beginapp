import streamlit as st
import numpy as np
import pandas as pd

st.header("Sham's first Streamlit App")
st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

import streamlit as st
import pandas as pd

st.header("Terms & Conditions")

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

st.header("About Diabetes")
from PIL import Image
image = Image.open('img-what-is-diabetes.jpg')

st.image(image, caption='What is diabetes Type')
    
option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C'])

if option=='line chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [3.1569, 101.7123],
    columns=['lat', 'lon'])

    st.map(map_data)

else:
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
        'Intplan': ['yes', 'yes', 'yes', 'no'],
        'Churn Status': [0, 0, 0, 1]
        }))
        
  
st.header("Diabetes Types")
from PIL import Image
image = Image.open('diabetes-type.jpg')

st.image(image, caption='Diabetes Type')

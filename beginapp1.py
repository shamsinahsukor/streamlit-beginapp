
import streamlit as st
import numpy as np
import pandas as pd

st.header("Sham's first Streamlit App")
st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

video_file = open('myvideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

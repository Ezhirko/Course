import streamlit as st
import os
from PIL import Image

st.markdown(
    """
    <style>
    body {
    font-family: 'Helvetica', Times, serif;
    text-align: center;
    display: flex;
    align-items: center;
    }
    
    .title {
        font-family: 'Helvetica', Times, serif;
        font-size: 2em;
        font-weight: bold;
        text-align: center;
    }
    
    .subheading {
        font-family: 'Helvetica', sans-serif;
        font-size: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
image = Image.open("RCLogger/Source/RCLogo.png")
col1,col2,col3 = st.columns([1,1,1])
with col1:
    st.markdown("<h1 class='title'></h1>", unsafe_allow_html=True)
with col2:
    st.image(image, output_format='auto',width=100)
    
st.markdown("<h1 class='title'>RADIANT CHAMPS</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='subheading'>Badminton Academy</h1>", unsafe_allow_html=True)

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
    height: 100vh;
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
st.image(image, width=75)
st.markdown("<h1 class='title'>RADIANT CHAMPS</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='subheading'>Badminton Academy</h1>", unsafe_allow_html=True)

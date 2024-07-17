import streamlit as st
import os
from PIL import Image

st.markdown(
    """
    <style>
    body {
    font-family: 'Helvetica', Times, serif;
    text-align: center;
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
image = Image.open("RCLogo.png")
st.image(image, use_column_width=True)
st.markdown("<h1 class='title'>RADIANT CHAMPS</h1>", unsafe_allow_html=True)
st.markdown("<h1 class='subheading'>Badminton Academy</h1>", unsafe_allow_html=True)

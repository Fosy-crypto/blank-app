import streamlit as st

color = st.color_picker("Pick A Color", "#00FFFF")
st.write("The current color is", color)

import streamlit as st

st.audio("cat-purr.mp3", format="audio/mpeg", loop=True)

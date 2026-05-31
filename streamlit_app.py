import streamlit as st

color = st.color_picker("Pick A Color", "#00FFFF")
st.write("The current color is", color)

import streamlit as st
your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py

if st.button("Home"):
    st.switch_page("your_app.py")
if st.button("Page 1"):
    st.switch_page("pages/page_1.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")

st.audio("gemilang_mp3.mp3", format="audio/mpeg", loop=True)

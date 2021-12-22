import streamlit as st


st.title("Hello Ruben")

celsious = st.number_input("Temperature in celsius", 0)

in_far = celsious * 1.8 + 32

st.title(f"Temperature in farenheit: {in_far}")

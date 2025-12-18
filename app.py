import streamlit as st
st.title("My First Project")
name = st.text_input ("Gey")
if name:
  st.write(f "Hello, {name}!")

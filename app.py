import streamlit as st

# Set the title of the app
st.title("Hello, Streamlit!")

# Add a simple text input and display it
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# Add a slider and display the value
age = st.slider("Select your age", 0, 100)
st.write(f"You are {age} years old.")

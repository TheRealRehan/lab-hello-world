import streamlit as st

# Set page title
st.title("Hello Streamlit!")

# Add some text
st.write("Welcome to your first Streamlit app!")

# Add a sidebar
st.sidebar.header("Navigation")
st.sidebar.write("This is a sidebar")

# Add an interactive widget
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Add a button
if st.button("Click me!"):
    st.write("Button clicked!")

# Add a slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old")

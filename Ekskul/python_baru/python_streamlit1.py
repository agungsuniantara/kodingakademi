import streamlit as st

# Displaying Titles
st.title("Web App Demo")
st.header("Displaying Text")

# Displaying regular text
st.write("This text is rendered using st.write().")

st.title("Input Example")

# Text Input
user_name = st.text_input("Name:")

# Number Input
user_age = st.number_input("Age:", min_value=0)

# Button
if st.button("Submit Data"):
    st.write("Name:", user_name)
    st.write("Age:", user_age)

# Sidebar Elements
st.sidebar.header("Configuration")
theme = st.sidebar.text_input("Enter theme:")

st.write("The settings are located in the sidebar.")
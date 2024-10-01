import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("My Streamlit App")
st.write("This app will get the user's name and say hello to the user when a button is clicked.")

name = st.text_input("Enter your name:")
age=  st.slider("Select your age:", 1, 100)

st.write(f"Hello {name}, you are {age} years old.")

if st.button("Say hello"):
    st.write("Hello there!")

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [24, 30, 35, 40, 29]
}
df = pd.DataFrame(data)

st.write("Here is the DataFrame:")
st.dataframe(df)

fig, ax = plt.subplots()
ax.hist(df["Age"], bins=5, color='blue', alpha=0.7)
ax.set_title("Histogram of Ages")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")

st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    st.write("Hello")

with col2:
    st.write("World")

with st.expander("More Information"):
    st.write("This is a sample Streamlit application")

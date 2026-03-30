#Task B input
import streamlit as st
import pandas as pd

st.sidebar.subheader("Entry Form")
name = st.sidebar.text_input("Student Name")
score = st.sidebar.number_input("Score", min_value=0, max_value=100, step=1)

if (st.sidebar.button("Add Student")):
    data = [name, score]

#Task C display
#from logic import ___
st.header("Faculty Grade Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Average", avg)
col2.metric("Highest", high)
col3.metric("Lowest", low)

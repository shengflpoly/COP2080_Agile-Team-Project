#Task B input
import streamlit as st
import pandas as pd
from logic import AddStudent, __Students

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=["Name", "Score", "Grade"])

st.sidebar.subheader("Entry Form")
name = st.sidebar.text_input("Student Name")
score = st.sidebar.number_input("Score", min_value=0, max_value=100, step=1)

if (st.sidebar.button("Add Student")):
    AddStudent(name, score)

if st.sidebar.button("Reset / Rerun"):
    st.rerun()

#Task C display
from logic import GetMin, GetMax, GetAverage
st.header("Faculty Grade Dashboard")

avg = GetAverage()
max = GetMax()
min = GetMin()

col1, col2, col3 = st.columns(3)
col1.metric("Average", avg)
col2.metric("Highest", max)
col3.metric("Lowest", min)

st.subheader("Grade Distribution")

grade_counts = __Students["Grade"].value_counts()
st.bar_chart(grade_counts)

st.subheader("Current Roaster")
st.dataframe(__Students)


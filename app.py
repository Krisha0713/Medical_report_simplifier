import streamlit as st
st.title("Medical report simplifier")
st.write("paste your medical report below to simplify it for better understanding.")
report = st.text_area("Medical Report", height=300)
if st.button("Simplify Report"):
    st.success("app is running successfully")
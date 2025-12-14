import streamlit as st
import re
from report_analysis import analyser

st.title("Medical Report Simplifier")
st.write("Paste your medical report below")

report = st.text_area("Medical Report")

if st.button("Simplify"):

    report = report.lower()

    found = False

    for test in analyser:
        if test in report:
            found = True
            st.subheader(test.capitalize())
            st.write(analyser[test]["description"])

            numbers = re.findall(r"\d+\.?\d*", report)

            if numbers:
                value = float(numbers[0])
                low, high = analyser[test]["range"]

                st.write(f"Detected value: {value}")

                if value < low:
                    st.error("Status: LOW")
                    st.write(analyser[test]["low"])
                elif value > high:
                    st.error("Status: HIGH")
                    st.write(analyser[test]["high"])
                else:
                    st.success("Status: NORMAL")
                    st.write("This value is within the normal range.")

    if not found:
        st.warning("No known medical test found in the report.")

st.warning("This tool is for educational purposes only and not medical advice.")

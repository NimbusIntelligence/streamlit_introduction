import streamlit as st

st.progress(88, text="Presentation Progress")

st.header("Streamlit And Snowflake")

sentences = ["Streamlit in Snowflake allows to securely build, deploy, and share Streamlit apps",
             "Use data stored in Snowflake without moving the data or application code to an external system",
             "Install additional packages in your Streamlit app (not all packages are supported)",
             "Uses a combination of cloud services instances and virtual warehouse instances",
             "Requires a virtual warehouse to run a Streamlit app and to perform SQL queries (check costs)",
             "Snowflake currently supports version 1.22.0 of the Streamlit libraries",
             ]

with st.form(key='my_form'):
    checked_tasks = [st.checkbox(sentence, key=f"checkbox_{i}") for i, sentence in enumerate(sentences)]
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if all(checked_tasks):
        st.warning("Streamlit is only available to accounts in AWS and Microsoft Azure commercial regions.")
        st.snow()
    else:
        st.error("Please make sure to check all tasks before submitting.")
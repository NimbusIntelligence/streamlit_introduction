import streamlit as st

st.progress(66, text="Presentation Progress")

st.header("Building And Deploying With Streamlit")

uploaded_file = st.file_uploader("Upload a Picture", type="png")

if uploaded_file is not None:
    st.write("Here is the Picture you uploaded:")
    st.image(uploaded_file, use_column_width=True, caption="Uploaded Picture")

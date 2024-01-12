import streamlit as st

st.progress(22, text="Presentation Progress")

st.header("Agenda")

with st.expander("**1.Who Should Use Streamlit?** :older_man:"):
    st.markdown("Show the target audience and use cases for Streamlit")

with st.expander("**2. Streamlit Under The Hood** :bomb:"):
    st.markdown("Explain how Streamlit works and what it does under the hood")

with st.expander("**3. How Easy Is Streamlit?** :building_construction:"):
    st.markdown("Show a simple demo code for a Streamlit app")

with st.expander("**4. Building And Deploying With Streamlit** :airplane:"):
    st.markdown("Show how to build and deploy a Streamlit app")

with st.expander("**5. Limitations Of Streamlit** :no_entry:"):
    st.markdown("Discuss the current limitations of Streamlit")

with st.expander("**6. Streamlit And Snowflake** :snowflake:"):
    st.markdown("Present the possibilities of Streamlit and Snowflake")

with st.expander("**7. Conclusion** :tada:"):
    st.markdown("Summarise the key points of the presentation")

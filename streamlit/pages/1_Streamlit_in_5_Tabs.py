import streamlit as st

st.progress(11, text="Presentation Progress")

st.header("Streamlit Explained In Five Tabs")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Rapid Prototyping",
                                        "Python-Centric",
                                        "Simplicity",
                                        "Interactive",
                                        "Snowflake Integration"]
                                        )

with tab1:
    st.subheader("Rapid Prototyping With Streamlit")
    
    if st.button('What Is Rapid Prototyping With Streamlit?', type="primary"):
        st.markdown("""
                    - Streamlit enables quick prototyping of web applications
                    - Allowing quick iterations and experimentation for visualisations and interfaces
                    - Wide range of pre-built components and widgets
                    """)

with tab2:
    st.subheader("Python-Centric")
    
    if st.checkbox('I want to know more about Python-centric Streamlit', value=False):
        st.markdown("""
                    - Streamlit is a Python library allowwing building web applications directly from Python scripts
                    - Enables a Python-centric workflow for data scientists
                    - Leveraging existing Python skills and knowledge
                    - No need to learn HTML, CSS, or JavaScript
                    """)
    
with tab3:
    st.subheader("Simplicity Of Streamlit")
    
    if st.toggle('Activate Simple Streamlit', value=False): 
        st.markdown("""
                    - Streamlit is designed to be simple and intuitive
                    - Prioritization of simplicity and ease of use
                    - High-level API abstracts away much of the complexity of building a web application
                    - No front-end development experience required
                    """)
    
with tab4:
    st.subheader("Interactive")
    
    option = st.selectbox("What do you want to know more about?", ('The weather', 'My future', 'Drink of the Day', 'Streamlits interactivity'), index=None,)
    
    if option == "Streamlits interactivity":
        st.markdown("""
                    - Streamlit is designed to be interactive
                    - Visualisations and interfaces are updated in real-time with minimal code
                    - Allows effective communication of insights and findings for all audiences
                    """)
    
    if option in ['The weather', 'My future', 'Drink of the Day']:
        st.markdown(""" I don't have any information about that, sorry ...""")

with tab5:
    st.subheader("Snowflake Integration")
    
    selection = st.select_slider(
        'Integrate Streamlit with Snowflake',
        options=['No', 'Still No', 'Maybe', 'Not Sure', 'Close to Yes', 'Yes', 'Hell Yeah']
        )
    
    if selection == "Hell Yeah":
        st.markdown("""
                    - Seamlessly integrates with Snowflake and interact with data stored in Snowflake
                    - Create interactive data applications directly inside Snowflake
                    - Snowflake data does not leave the Snowflake environment
                    - Use Snowflake / Streamlit editor to create quick prototypes
                    """)
    
    if selection == "Yes":
        st.markdown(""" Nearly there ...""")
    
    if selection == "Close to Yes":
        st.markdown(""" We get there ...""")
    
    if selection == "Not Sure":
        st.markdown(""" Whats holding you back ...""")
    
    if selection == "Maybe":
        st.markdown(""" Come on ...""")
    
    if selection == "Still No":
        st.markdown(""" Why not ...""")
    
    if selection == "No":
        st.markdown(""" You are missing out ...""")

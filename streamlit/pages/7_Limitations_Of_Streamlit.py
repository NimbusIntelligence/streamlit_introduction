import streamlit as st
import pandas as pd
import time

st.progress(77, text="Presentation Progress")

st.header("So i can use Streamlit for all my app projects now?")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.02)
    my_bar.progress(percent_complete + 1)
time.sleep(1)
my_bar.empty()

chart_data = pd.DataFrame({"Absolutely": [10,0], "Not": [0,10]})

st.line_chart(chart_data, color=["#FF0000", "#FF0000"], width=1000, height=1000)

time.sleep(5)

st.divider()

st.header("Limitations Of Streamlit")
    
col1, col2 = st.columns(2)

with col1:
    st.subheader("Inefficiency")
    st.markdown("""
                - Every user interaction re-executes the whole Python code
                - Code runs from top to bottom, which can be inefficient
                - Caching is currently available but limited
                """)
    
with col2:
    st.subheader("Customization")
    st.markdown("""
                - Streamlit only offers limited customization and styling options
                - Limited options for widgets such as sliders or buttons            
                - No support for adding custom CSS or JavaScript (dead anyway)
                """)
    
st.divider()

col3, col4 = st.columns(2)

with col3:
    st.subheader("Complex Applications")
    st.markdown("""
                    - Streamlit is not designed for building complex applications
                    - Mulitpage apps are possible but not intuitive for users
                    - No redirecting to other pages using buttons
                """)
    
with col4:
    st.subheader("Production Readiness")
    st.markdown("""
                    - Designed for prototyping and small to medium sized apps
                    - Devloped to display insights and findings quickly
                    - Not ready for highly scalable and production-ready apps
                """)
    
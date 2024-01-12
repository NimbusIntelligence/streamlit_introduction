import streamlit as st
import pandas as pd

st.progress(44, text="Presentation Progress")

st.header("Streamlit Under The Hood")

df = pd.DataFrame({"How Streamlit Works":
                   ["Streamlit apps are Python scripts that run from top to bottom.",
                    "Every time a user opens a browser tab pointing to your app, the script is executed and a new session starts.",
                    "As the script executes, Streamlit draws its output live in a browser.",
                    "Every time a user interacts with a widget, your script is re-executed and Streamlit redraws its output in the brower.",
                    "The output value of that widget matches the new value during that rerun.",
                    "Session State lets you save information that persists between reruns when you need more than a simple widget.",
                    "Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder."
                    ]
                    })

st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()

pick = st.slider('Pick the right number to see more information about caching in Streamlit', 0, 50, value=25)

if pick == 42:
    st.caption("*The idea of 42 being the answer to life, the universe, and everything comes from Douglas Adams' science fiction series 'The Hitchhiker's Guide to the Galaxy.'")

    st.subheader("Caching In Streamlit")
    st.markdown("""
                Streamlit apps are Python scripts that run from top to bottom, which brings two major challenges:
        
                1. Long-running functions run again and again, which slows down your app.
                2. Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.

                Streamlit solves these problems with two caching decorators!
                """)
    
    st.image("https://docs.streamlit.io/images/caching-high-level-diagram.png", use_column_width=True, caption="Streamlit's two caching decorators")

    col1, col2 = st.columns(2)
    with col1:
        st.write("**st.cache_data**")
        st.markdown("""
                    - Recommended for caching computations that return data
                    - Any serializable data object (str, int, float, DataFrame, array, list, …)
                    - The cached return value is a copy of the original data, so mutations to the cached value don't affect the original data.
                    """)

    with col2:
        st.write("**st.cache_resource**")
        st.markdown("""
                    - Recommended to cache global resources like ML models or database connections
                    - Unserializable objects that you don't want to load multiple times
                    - Shared across all reruns and sessions of an app
                    """)

elif pick == 25:
    st.empty()

else:
    st.write("You picked the wrong number")
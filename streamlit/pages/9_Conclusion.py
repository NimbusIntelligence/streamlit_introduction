import streamlit as st
import graphviz as gv

st.progress(100, text="Presentation Progress")

with st.sidebar:
    st.subheader("Code")
    st.write("Link to [Github](https://github.com/wiesnseb/streamlit_introduction)")
    st.divider()
    st.subheader("Author")
    st.write("Sebastian Wiesner")

st.header("Conclusion About Streamlit")

graph = gv.Digraph()
graph.edge('Easy to use', 'No frontend knowledge needed')
graph.edge("No frontend knowledge needed", 'Prototype applications in minutes')
graph.edge('Prototype applications in minutes', 'Easy to use')
graph.edge('Prototype applications in minutes', 'Use beloved Python skills')
graph.edge('Use beloved Python skills', 'Interactive visualisations with minimal code')
graph.edge('Interactive visualisations with minimal code', 'Show insights and findings quickly')
graph.edge('Show insights and findings quickly', 'Use Streamlit inside Snowflake')
graph.edge('Use Streamlit inside Snowflake', 'Prototype applications in minutes')
graph.edge('Use Streamlit inside Snowflake', "Customisation and complexity limitations")
graph.edge("Customisation and complexity limitations", "No frontend knowledge needed")

st.graphviz_chart(graph, use_container_width=True)

if st.button("End this presentation", use_container_width=True):
    st.balloons()

st.toast("Thank you for your attention!")
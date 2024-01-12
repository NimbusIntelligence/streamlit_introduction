import streamlit as st

st.progress(33, text="Presentation Progress")

st.header("Who Should Use Streamlit?")

my_dict = {"Who Should Use Streamlit?": {"Data Scientists": "People who don't know how dashboards work.", "Analysts": "People who don't know how dashboards work.", "Engineers": "People who don't know how dashboards work."},
           "Use Cases": "Exploratory Data Analysis and Dashboard Prototyping.",
           "When to Choose Streamlit?": "Quick Prototypes and Sharing Insights.",
           "Benefits for Users": "Simplicity and Collaboration."
}

st.json(my_dict)

st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("**Number of Weekly Downloads**", "401,033", "1.5 %")
col2.metric("**Active Community Contributors**", "333", "-8.1%")
col3.metric("**Streamlit Apps Created**", "101,023", "4.5%")
st.caption("*Numbers are purely fictional and for demonstration purposes only.")
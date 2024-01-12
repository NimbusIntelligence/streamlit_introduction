import streamlit as st

st.progress(55, text="Presentation Progress")

st.header("How Easy Is Streamlit?")
st.subheader("This is an example to show how easy Streamlit is!")

st.success("Streamlit is very easy and intuitive to use")
st.info("You don't need any frontend knowledge to build a dashboard.")

st.write("Wide range of pre-built components and widgets available to use")

easy = st.radio(
    "How easy is it to build an app with Streamlit?",
    [":rainbow[Super Easy]", "***Easy***", ":clown_face: I don't know how to code :clown_face:"],
    index=None,
)

if easy:
    st.write("You have chosen:", easy)

if st.button("Show me the code!"):
    st.divider()
    st.subheader("Code for this page:")

    body = """
    import streamlit as st

    st.header("How Easy Streamlit Is")
    st.subheader("This is an example to show how easy Streamlit is.")

    st.success("Streamlit is very easy and intuitive to use.")
    st.info("You don't need any frontend knowledge to build a dashboard.")

    st.write("Wide range of pre-built components and widgets available to use")

    easy = st.radio(
        "How easy is it to build an app with Streamlit?",
        [":rainbow[Super Easy]", "***Easy***", ":clown_face: I don't know how to code :clown_face:"],
        index=None,
    )

    if easy:
        st.write("You have chosen:", easy)

    if st.button("Show me the code!"):
        # displayed now (inception?)
    """

    st.code(body, language="python", line_numbers=True)
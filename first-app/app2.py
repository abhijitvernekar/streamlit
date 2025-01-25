import streamlit as st

st.title('Hierarchical Data Viewer')
st.header("Header")
st.subheader("Subheader")
st.caption("Caption")
st.write("Wrtie")
st.text("Text")
st.code("v = variable\n another_call()","python")
st.markdown("**bold**")

st.divider()

st.latex("...")
st.error("this is an error")
st.info("this is an info")
st.warning("warning")
st.success("success")


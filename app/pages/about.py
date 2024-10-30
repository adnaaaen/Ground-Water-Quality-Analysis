from utils import helper
import streamlit as st

st.set_page_config(
    page_title="About | Water Quality ",
    page_icon="💧",
    layout="wide",
)

sidebar_content = helper.create_sidebar()

with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


st.write("This from about page")
st.sidebar.write("this is from about page sidebar")

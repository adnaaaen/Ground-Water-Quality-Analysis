import streamlit as st

st.set_page_config(
    page_title="About | Water Quality ",
    page_icon="💧",
    layout="wide",
)
from utils import helper

sidebar_content = helper.create_sidebar()

with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


st.markdown("# **ABOUT**")
st.divider()

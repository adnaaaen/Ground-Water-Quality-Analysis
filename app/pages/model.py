import streamlit as st
from utils import helper

st.set_page_config(
    page_title="Model | Water Quality ",
    page_icon="💧",
    layout="wide",
)
sidebar_content = helper.create_sidebar()


with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


st.write("THIS FROM MODEL PAGE")
st.sidebar.write("THIS FROM MODEL PAGE SIDEBAR")

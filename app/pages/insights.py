import streamlit as st
from utils import helper

st.set_page_config(
    page_title="Insights | Water Quality ",
    page_icon="💧",
    layout="wide",
)
sidebar_content = helper.create_sidebar()

with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


with st.sidebar:

    st.divider()
    st.session_state.select_box_district = ""
    state = st.selectbox("Choose State", options=helper.get_unique_values("STATE"))

    if state:
        st.session_state.select_box_district = helper.STATE[state]

    dist = st.selectbox("Choose District", options=st.session_state.select_box_district)

    st.button("Apply Changes")


st.markdown("## **KEY INSIGHTS**")

cols = st.columns(4)

cols[0].metric(
    value=helper.get_values_by_locality(state=state, district=dist)["pH"].mean(),
    label=f"Mean value of pH in {dist}",
)

import streamlit as st

st.set_page_config(
    page_title="Model | Water Quality ",
    page_icon="💧",
    layout="wide",
)
from utils import helper

sidebar_content = helper.create_sidebar()


with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


st.markdown("# **MODEL SELECTION & EVALUATION**")
st.divider()
st.info("Since, this is a classification problem")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Decision Tree Classifier",
        "Random Forest Classifier",
        "K Neighbors Classifier",
        "Logistic Regression",
    ]
)

with tab1:
    st.write("from decision tree")

with tab2:
    st.write("from random forest")

with tab3:
    st.write("from k neighbors")

with tab4:
    st.write("from logistic regression")

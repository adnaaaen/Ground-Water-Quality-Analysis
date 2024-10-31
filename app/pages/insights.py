import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Insights | Water Quality ",
    page_icon="💧",
    layout="wide",
)
from utils import helper

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


st.markdown("# **KEY INSIGHTS**")
st.divider()

st.caption(f"State: :blue[{state}]")
st.caption(f"District: :blue[{dist}]")

# -------------------------------------------------------------------------
# key measures by states and districts as metrics

cols = st.columns(4)

ph_mean = helper.get_values_by_locality(state=state, district=dist)["pH"].mean()
cols[0].metric(
    value=round(ph_mean, 2),
    label="avg pH",
    help="Potential of Hydrogen (Acidity or Alkalinity)",
    delta=f"{"Safe Range" if 6.5 <= ph_mean <= 8.5 else "-Alert Range" }",
)

cl_mean = helper.get_values_by_locality(state=state, district=dist)["Cl"].mean()
cols[0].metric(
    value=round(cl_mean, 2),
    label="avg Cl",
    help="Chloride",
    delta=f"{"Safe Range" if 0 <= cl_mean <= 250 else "-Alert Range" }",
)

tds_mean = helper.get_values_by_locality(state=state, district=dist)["TDS"].mean()
cols[1].metric(
    value=round(tds_mean, 2),
    label="avg TDS",
    help="Total Dissolved Solids",
    delta=f"{"Safe Range" if 0 <= tds_mean <= 500 else "-Alert Range" }",
)

th_mean = helper.get_values_by_locality(state=state, district=dist)["TH"].mean()
cols[1].metric(
    value=round(th_mean, 2),
    label="avg TH",
    help="Total Hardness",
    delta=f"{"Safe Range" if 0 <= th_mean <= 300 else "-Alert Range" }",
)

ec_mean = helper.get_values_by_locality(state=state, district=dist)["EC"].mean()
cols[2].metric(
    value=round(ec_mean, 2),
    label="avg EC",
    help="Electrical Conductivity",
    delta=f"{"Safe Range" if 0 <= ec_mean <= 800 else "-Alert Range" }",
)

so4_mean = helper.get_values_by_locality(state=state, district=dist)["SO4"].mean()
cols[2].metric(
    value=round(so4_mean, 2),
    label="avg SO4",
    help="Sulfate",
    delta=f"{"Safe Range" if 0 <= so4_mean <= 250 else "-Alert Range" }",
)

no3_mean = helper.get_values_by_locality(state=state, district=dist)["NO3"].mean()
cols[3].metric(
    value=round(no3_mean, 2),
    label="avg NO3",
    help="Nitrate",
    delta=f"{"Safe Range" if 0 <= no3_mean <= 10 else "-Alert Range" }",
)

ca_mean = helper.get_values_by_locality(state=state, district=dist)["Ca"].mean()
cols[3].metric(
    value=round(ca_mean, 2),
    label="avg Ca",
    help="Calcium",
    delta=f"{"Safe Range" if 0 <= ca_mean <= 100 else "-Alert Range" }",
)


st.write("")
st.write("")
st.write("")
tab1, tab2 = st.tabs(["Analysis", "Corelation"])

with tab1:
    col1, col2 = st.columns(2)
    cat_var = col1.selectbox(
        "Categorical Variable: ",
        options=helper.df.select_dtypes(include="O").columns[::-1],
    )
    num_var = col2.selectbox(
        "Numerical Variable: ",
        options=helper.df.select_dtypes(include=np.number).columns[::-1],
    )

    col1.caption(f"CATEGORICAL DISTRIBUTION OF :blue[{cat_var}]")
    cat_fig = px.bar(helper.df[cat_var])
    col1.plotly_chart(cat_fig)

    col2.caption(f"NUMERICAL DISTRIBUTION OF :blue[{num_var}]")
    num_fig = px.histogram(helper.df[num_var])
    col2.plotly_chart(num_fig)


with tab2:
    seleted_cols = st.multiselect(
        label="Select columns to find relation",
        options=helper.df.select_dtypes(include=np.number).columns,
        default=["pH", "Cl", "TDS"],
    )
    corr_fig = px.imshow(helper.df[seleted_cols].corr(), text_auto=True)
    st.plotly_chart(corr_fig)

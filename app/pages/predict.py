import streamlit as st
from utils import helper
import numpy as np

# page configurations
st.set_page_config(page_title="Predict | Water Quality Analysis")

helper.get_page_link()


st.session_state.state=""
st.session_state.district=""

st.session_state.latitude=0
st.session_state.longitude=0

st.session_state.ph=0
st.session_state.ec=0

st.session_state.co3=0
st.session_state.hco3=0

st.session_state.cl=0
st.session_state.so4=0

st.session_state.no3=0
st.session_state.po4=0

st.session_state.th=0
st.session_state.ca=0

st.session_state.mg=0
st.session_state.na=0

st.session_state.k=0
st.session_state.f=0

st.session_state.sio2=0
st.session_state.tds=0

st.session_state.hardness=""
st.session_state.quality=""

is_random_data = st.button("Generate Random data")
if is_random_data:
    st.session_state.name = "Adnan"
    st.session_state.age = int(np.random.randint(10,100,size=1))

with st.form("model-prediction"):

    left, middle, right = st.columns(3)
    with left:
        state = st.text_input("State", value=st.session_state.state)
        district = st.text_input("District", value=st.session_state.district)
        latitude = st.number_input("Latitude", value=st.session_state.latitude)
        longitude = st.number_input("Longitude", value=st.session_state.longitude)
        ph = st.number_input("pH", value=st.session_state.ph)
        ec = st.number_input("EC", value=st.session_state.ec)
        co3 = st.number_input("CO3", value=st.session_state.co3)
        quality = st.text_input("Quality", value=st.session_state.quality)

    with middle:
        hco3 = st.number_input("HCO3", value=st.session_state.hco3)
        cl = st.number_input("CL", value=st.session_state.cl)
        so4 = st.number_input("SO4", value=st.session_state.so4)
        no3 = st.number_input("NO3", value=st.session_state.no3)
        po4 = st.number_input("PO4", value=st.session_state.po4)
        th = st.number_input("TH", value=st.session_state.th)
        ca = st.number_input("Ca", value=st.session_state.ca)

    with right:
        mg = st.number_input("Mg", value=st.session_state.mg)
        na = st.number_input("Na", value=st.session_state.na)
        k = st.number_input("K", value=st.session_state.k)
        f = st.number_input("F", value=st.session_state.f)
        sio2 = st.number_input("SiO2", value=st.session_state.sio2)
        tds = st.number_input("TDS", value=st.session_state.tds)
        hardness = st.text_input("Hardness", value=st.session_state.hardness)


    btn = st.form_submit_button("Predict")

from time import sleep
import streamlit as st

# page configurations
st.set_page_config(
    page_title="Predict | Water Quality ",
    page_icon="💧",
    layout="wide",
)
from utils.model_predict import predict, ModelParams
from utils import helper

sidebar_content = helper.create_sidebar()

with st.sidebar:
    for item in sidebar_content:
        st.page_link(page=item["page"], label=item["label"], icon=item["icon"])


st.markdown("# **WATER QUALITY PREDICTION MODEL**")
st.divider()


if "state" not in st.session_state:
    st.session_state.state = None
    st.session_state.district = None

    st.session_state.ph = None
    st.session_state.ec = None

    st.session_state.co3 = None
    st.session_state.hco3 = None

    st.session_state.cl = None
    st.session_state.so4 = None

    st.session_state.no3 = None
    st.session_state.po4 = None

    st.session_state.th = None
    st.session_state.ca = None

    st.session_state.mg = None
    st.session_state.na = None

    st.session_state.k = None
    st.session_state.f = None

    st.session_state.sio2 = None
    st.session_state.tds = None

    st.session_state.hardness = None

is_random_data = st.button("Generate Random Data")

if is_random_data:
    st.session_state.state = helper.get_random_category("STATE")
    st.session_state.district = helper.get_random_district_by_state(
        st.session_state.state
    )

    st.session_state.hardness = helper.get_random_category("HARDNESS")

    st.session_state.ph = helper.get_normal_num("pH")
    st.session_state.ec = helper.get_normal_num("EC")

    st.session_state.co3 = helper.get_normal_num("CO3")
    st.session_state.hco3 = helper.get_normal_num("HCO3")

    st.session_state.cl = helper.get_normal_num("Cl")
    st.session_state.so4 = helper.get_normal_num("SO4")

    st.session_state.no3 = helper.get_normal_num("NO3")
    st.session_state.po4 = helper.get_normal_num("PO4")

    st.session_state.th = helper.get_normal_num("TH")
    st.session_state.ca = helper.get_normal_num("Ca")

    st.session_state.mg = helper.get_normal_num("Mg")
    st.session_state.na = helper.get_normal_num("Na")

    st.session_state.k = helper.get_normal_num("K")
    st.session_state.f = helper.get_normal_num("F")

    st.session_state.sio2 = helper.get_normal_num("SiO2")
    st.session_state.tds = helper.get_normal_num("TDS")


with st.form("model-prediction"):
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        state = st.text_input(
            "State", value=st.session_state.state, placeholder="e.g. Kerala"
        )
        cl = st.number_input("CL", value=st.session_state.cl, placeholder="0")
        ca = st.number_input("Ca", value=st.session_state.ca, placeholder="0")

    with col2:
        district = st.text_input(
            "District", value=st.session_state.district, placeholder="e.g. Malappuram"
        )
        ph = st.number_input("pH", value=st.session_state.ph, placeholder="0")
        ec = st.number_input("EC", value=st.session_state.ec, placeholder="0")

    with col3:
        co3 = st.number_input("CO3", value=st.session_state.co3, placeholder="0")
        hco3 = st.number_input("HCO3", value=st.session_state.hco3, placeholder="0")
        tds = st.number_input("TDS", value=st.session_state.tds, placeholder="0")

    with col4:
        so4 = st.number_input("SO4", value=st.session_state.so4, placeholder="0")
        no3 = st.number_input("NO3", value=st.session_state.no3, placeholder="0")
        na = st.number_input("Na", value=st.session_state.na, placeholder="0")

    with col5:
        k = st.number_input("K", value=st.session_state.k, placeholder="0")
        po4 = st.number_input("PO4", value=st.session_state.po4, placeholder="0")
        th = st.number_input("TH", value=st.session_state.th, placeholder="0")

    with col6:
        hardness = st.text_input(
            "Hardness", value=st.session_state.hardness, placeholder="e.g. Soft"
        )
        mg = st.number_input("Mg", value=st.session_state.mg, placeholder="0")

    with col7:
        f = st.number_input("F", value=st.session_state.f, placeholder="0")
        sio2 = st.number_input("SiO2", value=st.session_state.sio2, placeholder="0")

    # Submit button for form
    btn = st.form_submit_button("Predict Water Quality", use_container_width=True)
    if btn:
        # Collect all input fields into a dictionary
        all_inputs = ModelParams(
            state=state,
            district=district,
            ph=ph,
            ec=ec,
            co3=co3,
            hco3=hco3,
            cl=cl,
            so4=so4,
            no3=no3,
            po4=po4,
            th=th,
            ca=ca,
            mg=mg,
            na=na,
            k=k,
            f=f,
            sio2=sio2,
            tds=tds,
            hardness=hardness,
        )

        # Display the collected inputs dictionary

        prediction, color = predict(all_inputs)

        with st.status("Predicting water quality...", expanded=True) as status:
            sleep(2)
            status.update(
                label=f"This water quality level is classified as :{color}[{prediction}]",
                expanded=False,
            )

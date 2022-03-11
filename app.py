import streamlit as st
import requests


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- LOAD ASSETS ----




# ---- HEADER SECTION ----
with st.container():
    st.title("Stock market performance prediction")
    st.write(
        "Choose a tick and predict the performance of a share against the market performance"
    )


#st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# ---- PREDICTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")

    st.markdown('Choose a tick to predict the performance of the share')
    tick = st.text_input(label='TICK')
    button=st.button('Predict')

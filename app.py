import streamlit as st
import requests

st.title('Stock market performance prediction')

#st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)



st.markdown(Choose a tick to predict the performance of the share)


tick = st.date_input(label='TICK')

button=st.button('Predict')


st.write('Ticks availables')

st.write('APPL=Apple')
st.write()

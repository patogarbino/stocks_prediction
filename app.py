import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_tags import st_tags



st.set_page_config(page_title="My Webpage",page_icon=":bar_chart:", layout="wide")

# ---- LOAD ASSETS ----


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()






# ---- HEADER SECTION ----
with st.container():
    st.title("Stock market performance prediction")
    st.write(
        "Choose a tick and predict the performance of a share against the market performance"
    )


#st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

# ---- PREDICTION ----
# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:

#         st.write("##")

#         st.markdown('Choose a ticker to predict the performance of the share')
#         tick = st.text_input(label='TICKER')
#         # button=st.button('Predict')

#     with right_column:
#         lottie_image = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ymyikn6l.json")

#         st_lottie(lottie_image)





with st.container():
    left_column, right_column = st.columns(2)
    with left_column:

        st.write("##")

        st.write('Dont you know the ticker of the company you are looking for?')


        #names = pd.read_csv('company_names.csv')
        names = pd.read_csv("company_names.csv")

        empresa = st_tags(
                            label='**Text below the name of the company:**',
                            text='Example: Apple',
                            value='',
                            suggestions=list(names['Name'].unique()),
                            maxtags=1,
                            key="asd")

        try:
            if empresa:
                empresax = names[names['Name'] == empresa[0]].iloc[0,0]
                st.markdown(f'###  the ticker is: {empresax}')

        except:
            print("")

        button=st.button('Predict')

    with right_column:
        lottie_image = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ymyikn6l.json")

        st_lottie(lottie_image)

        #st.write(empresax)

        # try:
        #     empresa = st_tags(
        #                     label='**Text below the name of the company:**',
        #                     text='Example: Zara',
        #                     value=['apple'],
        #                     suggestions=['apple', 'microsoft', 'tesla', 'facebook', 'le wagon', 'amazon', 'zara', 'mercadolibre', 'ebay'],
        #                     maxtags=1,
        #                     key="asd").lower()
        #     empresa = names[names['Name'] == empresa].iloc[0,0]
        #     st.markdown(f'###  the ticker is: {empresa}')

        # except:
        #      if empresa:
        #          st.markdown(f'### The company {empresa} is not in our database.')

        # button_find=st.button('Find ticker')

import streamlit as st
import requests

CSS = """
h1 {
    color: blue;
}
h6
{
    color: red;
}

"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'''
# TaxiFareModel Prediction
'''

st.markdown('''
### Please insert the required inputs
''')


#- date and time
date = st.date_input(label='Date')
date = str(date).replace('/','-')
time = st.time_input(label='Time')
date = date +' ' +str(time)
#pickup longitude
long1 = st.text_input(label='Pickup Longitude')
if long1:
    try:
        long1 = float(long1)
    except:
        "###### The input must be a number"
#pickup latitude
lat1 = st.text_input(label='Pickup Latitude')
if lat1:
    try:
        lat1 = float(lat1)
    except:
        "###### The input must be a number"
#dropoff longitude
long2 = st.text_input(label='Dropoff Longitude')
if long2:
    try:
        long2 = float(long2)
    except:
        "###### The input must be a number"
#dropoff latitude
lat2 = st.text_input(label='Dropoff Latitude')
if lat2:
    try:
        lat2 = float(lat2)
    except:
        "###### The input must be a number"
#passenger count
cont = st.text_input(label='Number of passengers')
if cont:
    try:
        cont = int(cont)
    except:
        "###### The input must be an integer"

if date and long1 and lat1 and long2 and lat2 and cont:

    url = 'https://taxifare.lewagon.ai/predict'

    params = { 'pickup_datetime':date,
            'pickup_longitude':long1,
            'pickup_latitude': lat1,
            'dropoff_longitude': long2,
            'dropoff_latitude':lat2,
            'passenger_count': cont
    }

    response = requests.get(url,params=params).json()['fare']

    st.markdown(f'### The Fare prediction is: USD {response:.2f}\n')

    import folium

    from streamlit_folium import folium_static

    m = folium.Map(location=[(float(long1)+float(long2))/2, (float(lat1)+float(lat2))/2], zoom_start=11)

    folium.Marker(location=[float(long1), float(lat1)],
                popup='Pickup',
                icon=folium.Icon(color="blue", icon="info-sign"),
                ).add_to(m)

    folium.Marker(location=[float(long2), float(lat2)],
                popup='Dropoff',
                icon=folium.Icon(color="blue", icon="info-sign"),
                ).add_to(m)

    folium_static(m)

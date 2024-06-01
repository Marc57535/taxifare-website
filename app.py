import streamlit as st
import datetime
import requests
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
''')

c1, c2 = st.columns(2)
c4, c5, c6 = st.columns([6,3,2])



today = datetime.date.today()
now = datetime.datetime.now().time()


with st.container():
    date = c1.date_input("Departure date", today)
    time = c2.time_input("Select time", now)
    pickup_datetime = datetime.datetime.combine(date, time)

with st.container():
    pickup_longitude = c1.number_input('Insert a pickup longitude', value=-74.00597)
    pickup_latitude = c2.number_input('Insert a pickup latitude', value=40.71427)


with st.container():
    dropoff_longitude = c1.number_input('Insert a drop off longitude', value=-72.00597)
    dropoff_latitude = c2.number_input('Insert a drop off latitude', value=40.71427)

passenger_count = st.number_input('Passenger', value=1)

url = 'https://taxifare.lewagon.ai/predict'
params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

if st.button('Calcul Cost'):
    # print is visible in the server output, not in the page
    response = requests.get(url=url, params=params)
    prediction = response.json()['fare']
    formatted_price = f'{round(prediction)}$'
    st.write('Cost', formatted_price)

    def get_map_data():

        return pd.DataFrame(
                {'lat': [pickup_latitude, dropoff_latitude], 'lon': [pickup_longitude, dropoff_longitude]}
            )

    df = get_map_data()

    st.map(df)
else:
    st.write('Enter your travel informations')

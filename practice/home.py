from datetime import datetime as dt

import pandas as pd
import plotly.express as px
import requests
import streamlit as st
import urllib3
from bs4 import BeautifulSoup

from db_manager import DBManager

urllib3.disable_warnings()
URL = 'https://programmer100.pythonanywhere.com/'
DB_NAME = 'temp_info.db'
TABLE_NAME = 'tempo'
conn = DBManager(DB_NAME)
conn.create_table(TABLE_NAME)


def get_site_info():
    response = requests.get(url=URL, verify=False)
    return response.text


def get_temp_info(site_info):
    soup = BeautifulSoup(markup=site_info, features='html.parser')
    temp_ = soup.find(name='h1', attrs={'id': 'temperatureId'})
    return temp_.text


def add_data_to_db():
    site = get_site_info()
    temp = get_temp_info(site)
    date = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    db_data = [date, temp]
    conn.insert_data(table_name=TABLE_NAME, data=db_data)


add_data_to_db()
data = conn.read_data(TABLE_NAME)
data = pd.DataFrame(data=data, columns=['date', 'temperature'])
st.title('Temperatures')
if not data.empty:
    figure = px.line(x=data.date, y=data.temperature, labels={'x': 'Date', 'y': 'Temperature (c)'})
    st.plotly_chart(figure_or_data=figure)

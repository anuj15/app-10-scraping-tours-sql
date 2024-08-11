import plotly.express as px
import streamlit as st

from methods import *

st.title('Temperatures')
data = read_temp_file()
if not data.empty:
    figure = px.line(x=data.timestamp, y=data.temperature, labels={'x': 'Date', 'y': 'Temperature (c)'})
    st.plotly_chart(figure_or_data=figure)

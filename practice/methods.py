import os.path
from datetime import datetime as dt

import pandas as pd
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
URL = 'https://programmer100.pythonanywhere.com/'
FILE_NAME = 'temp.txt'
file_exists = os.path.isfile(FILE_NAME)


def get_site_info():
    response = requests.get(url=URL, verify=False)
    return response.text


def get_temp_info(site_info):
    soup = BeautifulSoup(markup=site_info, features='html.parser')
    temp_ = soup.find(name='h1', attrs={'id': 'temperatureId'})
    return temp_.text


def read_temp_file():
    try:
        return pd.read_csv(FILE_NAME)
    except FileNotFoundError:
        return ''


def write_temp_info(temp_):
    time_now = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'timestamp': time_now,
        'temperature': temp_,
    }
    pd.DataFrame([data]).to_csv(path_or_buf=FILE_NAME, mode='a', index=False, header=not file_exists)


if __name__ == '__main__':
    site = get_site_info()
    temp = get_temp_info(site)
    write_temp_info(temp)

from smtplib import SMTP

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
URL = 'http://programmer100.pythonanywhere.com/tours/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/39.0.2171.95 Safari/537.36'}


def get_site_info(url):
    response = requests.get(url=url, headers=HEADERS, verify=False)
    return response.text


def get_tour_info(markup):
    soup = BeautifulSoup(markup=markup, features='html.parser')
    tour = soup.find(name='h1', attrs={'id': 'displaytimer'})
    return tour.text


def send_mail(msg):
    with SMTP(host='smtp.gmail.com', port=587) as conn:
        conn.starttls()
        conn.login(user='anuj.nits2@gmail.com', password='wzgpcyhchhcdoret')
        conn.sendmail(from_addr='anuj.nits2@gmail.com', to_addrs='anuj.nits@gmail.com', msg=msg)


def write_tour_info(tour):
    with open(file='tour_data.txt', mode='a') as f:
        f.write(f'{tour}\n')


def read_tour_info():
    try:
        with open(file='tour_data.txt') as f:
            return f.read()
    except FileNotFoundError:
        with open(file='tour_data.txt', mode='w'):
            return read_tour_info()


if __name__ == '__main__':
    page_source = get_site_info(URL)
    tour_info = get_tour_info(page_source)
    print(tour_info)
    if tour_info != 'No upcoming tours':
        if tour_info not in read_tour_info():
            write_tour_info(tour_info)
            send_mail(msg=f'Subject:New Tour Info\n\n{tour_info}')
            print('Email was sent successfully.')

import re

from bs4 import BeautifulSoup
from selenium import webdriver


def _format_date(start_date):
    date_str = f"{start_date.day}-{start_date.month}-{start_date.year}"
    return date_str


def _format_price(price):
    return price


def _format_time(time):
    return time


def _format_duration(time):
    time[0] = time[0].replace("h", "")
    time[1] = time[1].replace("m", "")
    return time


def _format_flight_id(id):
    return id[0]


def find_price(start_date, start_location, end_location):
    # 'price': '4185',
    # 'start_time': ['12', '55'],
    # 'end_time': ['15', '50'],
    # 'duration': ['2h', '55m'],
    # 'flight_id': ['AirAsia'],
    # 'site': 'makemytrip

    start_date =_format_date(start_date)

    driver = webdriver.Chrome(r"C:\Users\Akshat Malik\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(f'https://flights.makemytrip.com/makemytrip//search/O/O/E/1/0/0/S/V0/{start_location}_{end_location}_'
               f'{start_date}')
    list_of_price = list()
    time = driver.find_elements_by_class_name("timeCa")
    price_list = driver.find_elements_by_class_name("price_info")
    type_of_flight = driver.find_elements_by_class_name("airline_info_detls")

    for i in range(min(len(price_list), len(time))):
        price = re.findall(r'\d+', price_list[i].get_attribute('innerHTML').replace(",", ""))[0]
        start_time = re.findall(r'\d+\w', time[3*i].get_attribute('innerHTML'))
        end_time = re.findall(r'\d+\w', time[3*i + 1].get_attribute('innerHTML'))
        duration = re.findall(r'\d+\w', time[3*i + 2].get_attribute('innerHTML'))
        flight_id = BeautifulSoup(type_of_flight[i].get_attribute('innerHTML'), 'html.parser').span.contents
        list_of_price.append({
            "price": _format_price(price),
            "start_time": _format_time(start_time),
            "end_time": _format_time(end_time),
            "duration": _format_duration(duration),
            "flight_id": _format_flight_id(flight_id)
        })

    driver.close()
    list_of_price = sorted(list_of_price, key=lambda k: k['price'])
    return list_of_price

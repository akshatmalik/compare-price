import re

from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

def _format_date(start_date):
    date_str = f"{start_date.day}-{start_date.month}-{start_date.year}"
    return date_str


def find_price(start_date, start_location, end_location):

    start_date =_format_date(start_date)

    driver = webdriver.Chrome(r"C:\Users\Akshat Malik\Downloads\chromedriver_win32\chromedriver.exe")
    driver.get(f'https://flights.makemytrip.com/makemytrip//search/O/O/E/1/0/0/S/V0/{start_location}_{end_location}_'
               f'{start_date}')
    list_of_price = list()
    time = driver.find_elements_by_class_name("timeCa")
    price_list = driver.find_elements_by_class_name("price_info")
    type_of_flight = driver.find_elements_by_class_name("airline_info_detls")

    for i in range(len(price_list)):
        price = re.findall(r'\d+', price_list[i].get_attribute('innerHTML').replace(",", ""))[0]
        start_time = re.findall(r'\d+\w', time[3*i].get_attribute('innerHTML'))
        end_time = re.findall(r'\d+\w', time[3*i + 1].get_attribute('innerHTML'))
        duration = re.findall(r'\d+\w', time[3*i + 2].get_attribute('innerHTML'))
        flight_id = BeautifulSoup(type_of_flight[i].get_attribute('innerHTML'), 'html.parser').span.contents
        list_of_price.append({
            "price": price,
            "start_time": start_time,
            "end_time": end_time,
            "duration": duration,
            "flight_id": flight_id
        })

    driver.close()
    list_of_price = sorted(list_of_price, key=lambda k: k['price'])
    return list_of_price

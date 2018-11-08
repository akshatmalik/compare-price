import os
import pathlib
import re
import zipfile

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import helper_methods
from . import Website


class MakeMyTrip(Website):

    def _format_date(self, start_date):
        date_str = f"{start_date.day}-{start_date.month}-{start_date.year}"
        return date_str

    def _format_price(self, price):
        return price

    def _format_time(self, time):
        return time

    def _format_duration(self, time):
        time[0] = time[0].replace("h", "")
        time[1] = time[1].replace("m", "")
        return time

    def _format_flight_id(self, id):
        return id[0]

    def _setup(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = pathlib.Path(str(dir_path))

        url = "https://chromedriver.storage.googleapis.com/2.43/chromedriver_win32.zip"
        file_path = dir_path / f"chrome_driver_download.zip"

        if file_path.exists() == False:
            file_path = helper_methods.download_file(url, file_path)

        if pathlib.Path(dir_path / "chrome_driver_download").exists() == False:
            zip_ref = zipfile.ZipFile(file_path, 'r')
            zip_ref.extractall(dir_path / "chrome_driver_download")
            zip_ref.close()

    def website_name(self):
        return "MakeMyTrip"

    def _find_price(self, start_date, start_location, end_location):
        # 'duration': '12h 35m',
        # 'end_time': '00:45',
        # 'flight_id': 'Jet Airways',
        # 'price': 53660,
        # 'site': 'goibibo',
        # 'start_time': '22:50'
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = pathlib.Path(str(dir_path))
        file_name = dir_path / "chrome_driver_download" / f"chromedriver.exe"

        start_date = self._format_date(start_date)

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(executable_path=str(file_name), chrome_options=chrome_options)
        driver.get(
            f'https://flights.makemytrip.com/makemytrip//search/O/O/E/1/0/0/S/V0/{start_location}_{end_location}_'
            f'{start_date}')
        list_of_price = list()
        time = driver.find_elements_by_class_name("timeCa")
        price_list = driver.find_elements_by_class_name("price_info")
        type_of_flight = driver.find_elements_by_class_name("airline_info_detls")

        for i in range(min(len(price_list), len(time))):
            price = re.findall(r'\d+', price_list[i].get_attribute('innerHTML').replace(",", ""))[0]
            start_time = re.findall(r'\d+\w', time[3 * i].get_attribute('innerHTML'))
            end_time = re.findall(r'\d+\w', time[3 * i + 1].get_attribute('innerHTML'))
            duration = re.findall(r'\d+\w', time[3 * i + 2].get_attribute('innerHTML'))
            flight_id = BeautifulSoup(type_of_flight[i].get_attribute('innerHTML'), 'html.parser').span.contents

            list_of_price.append({
                "price": price,
                "start_time": start_time,
                "end_time": end_time,
                "duration": duration,
                "flight_id": flight_id,
                "site": self.website_name()
            })

        driver.close()
        return list_of_price
import sys, os
import os
import sys
import sys
sys.path.insert(0, r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight")

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\website_api")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\compare_price")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\venv")

import requests

from . import Website


class GoIbibo(Website):
    """
    The ap returns the result in this format

        # 'duration': '12h 35m',
        # 'end_time': '00:45',
        # 'flight_id': 'Jet Airways',
        # 'price': 53660,
        # 'site': 'goibibo',
        # 'start_time': '22:50'
    """

    def _format_date(self, start_date):
        date_str = f"{start_date.year}{start_date.month}{start_date.day}"
        return date_str

    def _format_price(self, price):
        return price

    def _format_time(self, time):
        time = time.split(":")
        return time

    def _format_duration(self, time):
        time = time.split(" ")
        time[0] = time[0].replace("h", "")
        time[1] = time[1].replace("m", "")
        return time

    def _format_flight_id(self, id):
        return id

    def _setup(self):
        pass

    def website_name(self):
        return "GoIbibo"

    def _find_price(self, start_date, start_location, end_location):


        start_date = self._format_date(start_date)

        params = (
            ('app_id', '41d6cc11'),
            ('app_key', '3d7e4932f6c586bc48346cb19c0587be'),
            ('format', 'json'),
            ('source', f"{start_location}"),
            ('destination', f"{end_location}"),
            ('dateofdeparture', f'{start_date}'),
            ('seatingclass', 'E'),
            ('adults', '1'),
            ('children', '0'),
            ('infants', '0'),
            ('counter', '100'),
        )

        response = requests.get('http://developer.goibibo.com/api/search/', params=params)
        print(response)
        print(response.json()['data'])
        flight_data = response.json()['data']['onwardflights']
        go_ibibo = list()

        # TODO: Time should be datetime
        for flight in flight_data:
            flight_id = flight['airline']
            start_time = flight['deptime']
            end_time = flight["arrtime"]
            duration = flight["duration"]
            price = flight["fare"]["totalfare"]
            go_ibibo.append({
                "price": price,
                "start_time": start_time,
                "end_time": end_time,
                "duration": duration,
                "flight_id": flight_id,
                "site": self.website_name()
            })

        return go_ibibo
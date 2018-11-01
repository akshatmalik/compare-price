import requests
from . import Website

def _format_date(start_date):
    date_str = f"{start_date.year}{start_date.month}{start_date.day}"
    return date_str


def _format_price(price):
    return price


def _format_time(time):
    time = time.split(":")
    return time


def _format_duration(time):
    time = time.split(" ")
    time[0] = time[0].replace("h", "")
    time[1] = time[1].replace("m", "")
    return time


def _format_flight_id(id):
    return id


def find_price(start_date, start_location, end_location):
    # 'duration': '12h 35m',
    # 'end_time': '00:45',
    # 'flight_id': 'Jet Airways',
    # 'price': 53660,
    # 'site': 'goibibo',
    # 'start_time': '22:50'

    start_date = _format_date(start_date)

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
    flight_data = response.json()['data']['onwardflights']
    site_name  = "goibibo"
    go_ibibo = list()

    for flight in flight_data:
        flight_id = flight['airline']
        start_time = flight['deptime']
        end_time = flight["arrtime"]
        duration = flight["duration"]
        price = flight["fare"]["totalfare"]
        go_ibibo.append({
            "price" : _format_price(price),
            "start_time": _format_time(start_time),
            "end_time" : _format_time(end_time),
            "duration" : _format_duration(duration),
            "flight_id" : _format_flight_id(flight_id),
            "site" : site_name
        })

    go_ibibo = sorted(go_ibibo, key=lambda k: k['price'])
    return go_ibibo

class GoIbibo(Website):

    def __init__(self):
        self.website_name = "go-ibibo"

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
        # 'duration': '12h 35m',
        # 'end_time': '00:45',
        # 'flight_id': 'Jet Airways',
        # 'price': 53660,
        # 'site': 'goibibo',
        # 'start_time': '22:50'

        start_date = _format_date(start_date)

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
        flight_data = response.json()['data']['onwardflights']
        go_ibibo = list()

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
                "site": self.website_name
            })

        return go_ibibo
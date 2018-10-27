import requests
from pprint import pprint
from datetime import datetime


def _format_date(start_date):
    date_str = f"{start_date.year}{start_date.month}{start_date.day}"
    return date_str

def find_price(start_date, start_location, end_location):

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
            "price" : price,
            "start_time": start_time,
            "end_time" : end_time,
            "duration" : duration,
            "flight_id" : flight_id,
            "site" : "goibibo"
        })

    go_ibibo = sorted(go_ibibo, key=lambda k: k['price'])
    return go_ibibo

import requests
from pprint import pprint


def find_price():
    params = (
        ('app_id', '41d6cc11'),
        ('app_key', '3d7e4932f6c586bc48346cb19c0587be'),
        ('format', 'json'),
        ('source', 'BLR'),
        ('destination', 'IXC'),
        ('dateofdeparture', '20181102'),
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
    #     pprint(flight)
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
    #     print(go_ibibo[-1])
    go_ibibo = sorted(go_ibibo, key=lambda k: k['price'])
    pprint(go_ibibo)
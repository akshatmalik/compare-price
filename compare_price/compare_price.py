# from __future__ import print_function, unicode_literals

import sys

sys.path.insert(0, r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight")
import os
import sys
import datetime
from pprint import pprint

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\website_api")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\compare_price")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\venv")
from website_api import makemytrip_find_price


class FindLowestPrice:
    def __init__(self, start_date, end_date, start_location, end_location):
        self.start_date = start_date
        self.end_location = end_location
        self.start_location = start_location
        self.end_date = end_date

    def _get_price_list(self, date):
        results = []
        # results.extend(go_ibibo_find_price.GoIbibo().find_price(date, self.start_location, self.end_location))
        results.extend(makemytrip_find_price.MakeMyTrip().find_price(date, self.start_location, self.end_location))
        return results

    def _filter_by_time(self, start_price_list: list, start_time: datetime, end_time: datetime):

        filtered_time_list = list()
        for time in start_price_list:

            if start_time <= time["start_time"] <= end_time:
                filtered_time_list.append(time)

        return filtered_time_list

    # noinspection PyShadowingNames
    def find_lowest_price(self):

        start_price_list = self._get_price_list(self.start_date)
        start_price_list = sorted(start_price_list, key=lambda k: int(k['price']))

        if self.end_date is None:
            return start_price_list, None

        end_price_list = self._get_price_list(self.end_date)
        end_price_list = sorted(end_price_list, key=lambda k: int(k['price']))

        return start_price_list, end_price_list

    # noinspection PyShadowingNames
    def find_flight_in_time_range(self, start_date_times: (datetime, datetime), end_date_times: (datetime, datetime)):
        start_price_list, end_price_list = self.find_lowest_price()

        start_price_list = self._filter_by_time(start_price_list, start_date_times[0], start_date_times[1])
        if end_date_times is None:
            return start_price_list, None
        end_price_list = self._filter_by_time(end_price_list, end_date_times[0], end_date_times[1])

        return start_price_list, end_price_list

    def find_time_in_duration(self, start_date_time, start_date_duration, end_date_time, end_date_duration):

        start_date_start_time = [0,0]
        start_date_start_time[0] = start_date_time[0] + start_date_duration[0]
        start_date_start_time[1] = start_date_time[1] + start_date_duration[1]

        end_date_start_time = [0,0]
        end_date_start_time[0] = end_date_time[0] + end_date_duration[0]
        end_date_start_time[1] = end_date_time[1] + end_date_duration[1]

        # pprint(start_date_start_time)
        # pprint(end_date_start_time)

        return self.find_flight_in_time_range( (start_date_time, start_date_start_time), (end_date_time, end_date_start_time))
import sys


def get_date(date):
    date_parts = date.split("/")
    try:
        entered_date =  datetime.datetime(year=int(date_parts[0]), month=int(date_parts[1]),
                                 day=int(date_parts[2]))
        if entered_date <= datetime.datetime.today():
            raise Exception("Falied compariosin")
        return entered_date
    except Exception as e:
        print(e)
        return None


def get_time(time, date):
    try:
        time_parts_start = time.strip().split(":")
        start_date_time = date
        start_date_time_start = start_date_time.replace(hour=int(time_parts_start[0]), minute=int(time_parts_start[1]))
        return start_date_time_start
    except Exception:
        return None


def get_input():
    global answers
    if not debug:
        from PyInquirer import prompt
        """
        Hi
        From where you going?  -- Keep checking till valid loation. Give nearest suggestions
        To where you going?  -- Keep checking till valid loation. Give nearest suggestions
        Start date for flight -- parse it and check it makes sense?
        Time for start date to work  -- parse it to check it makes sense
        Return flight to be booked? -- based on this look for the end flight
        Return date for flight -- parse it and check it makes sense?
        Time for Return date to work  -- parse it to check it makes sense
        Frequency to check for price -- in minutes
        Email to send updates of the progress
        """

        questions_hi = [
            {
                'type': 'input',
                'name': 'dummy',
                'message': "Welcome to Compare Price!\nLets get started? (Press Enter to begin)",
            },
        ]
        answers = prompt(questions_hi)

        # questions_start_location = [
        #     {
        #         'type': 'input',
        #         "name": "start_location",
        #         "message": "Where is your trip starting from? ",
        #     },
        # ]
        #
        # answers = prompt(questions_start_location, answers)
        # while get_location_code(answers["start_location"], True):
        #     answers = prompt(questions_start_location, answers)
        #
        # questions_end_location = [
        #     {
        #         'type': 'input',
        #         "name": "end_location",
        #         "message": "Where is your trip ending at? ",
        #     },
        # ]
        # answers = prompt(questions_end_location, answers)
        # while get_location_code(answers["end_location"], True):
        #     answers = prompt(questions_end_location, answers)

        questions_is_return_journey = [
            {
                "type": "confirm",
                "name": "return",
                "message": "Return trip? ",
                'default': False,
            },
        ]
        answers = prompt(questions_is_return_journey, answers)

        questions_start_location_start_date = [
            {
                'type': 'input',
                'name': 'start_date',
                'message': "Which day you want to book your flight? (follow this format please : YYYY/MM/DD)",
            },
        ]
        answers = prompt(questions_start_location_start_date, answers)
        print(get_date(answers["start_date"]))
        while get_date(answers["start_date"]) is None:
            answers = prompt(questions_start_location_start_date, answers)
            print(get_date(answers["start_date"]))
            pprint(answers)
        answers["start_date"] = get_date(answers["start_date"])

        questions_start_location_time_range_start = [
            {
                'type': 'input',
                'name': 'start_date_time_range_start',
                'message': f"After what time are you looking flights for on {answers['start_date'].date()}? (Format HH:MM)",
            },
        ]
        answers = prompt(questions_start_location_time_range_start, answers)

        while get_time(answers["start_date_time_range_start"], answers["start_date"]) is None:
            answers = prompt(questions_start_location_time_range_start, answers)
            pprint(answers)

        questions_start_location_time_range_end = [
            {
                'type': 'input',
                'name': 'start_date_time_range_end',
                'message': f"Till what time are you looking flights for on {answers['start_date']}? (Format HH:MM)",
            },
        ]
        answers = prompt(questions_start_location_time_range_end, answers)

        while get_time(answers["start_date_time_range_end"], answers["start_date"]) is None:
            answers = prompt(questions_start_location_time_range_end, answers)
            pprint(answers)

        answers["start_date_time"] = (answers["start_date_time_range_start"], answers["start_date_time_range_end"])

        if answers["return"]:
            questions_end_location_start_date = [
                {
                    'type': 'input',
                    'name': 'end_date',
                    'message': "Which day you want to book your return flight? "
                               "(follow this format please : YYYY/MM/DD)",
                },
            ]
            answers = prompt(questions_end_location_start_date, answers)

            while get_date(answers["end_date"]) is None:
                answers = prompt(questions_end_location_start_date, answers)
                pprint(answers)
            answers["end_date"] = get_date(answers["end_date"])

            questions_end_location_time_range_start = [
                {
                    'type': 'input',
                    'name': 'end_date_time_range_start',
                    'message': f"After what time are you looking flights for on {answers['end_date']}? (Format HH:MM)",
                },
            ]
            answers = prompt(questions_end_location_time_range_start, answers)

            while get_time(answers["end_date_time_range_start"], answers["end_date"]) is None:
                answers = prompt(questions_end_location_time_range_start, answers)
                pprint(answers)

            questions_start_location_time_range_end = [
                {
                    'type': 'input',
                    'name': 'end_date_time_range_end',
                    'message': f"Till what time are you looking flights for on {answers['end_date']}? (Format HH:MM)",
                },
            ]
            answers = prompt(questions_start_location_time_range_end, answers)

            while get_time(answers["end_date_time_range_end"], answers["end_date"]) is None:
                answers = prompt(questions_start_location_time_range_end, answers)
                pprint(answers)

            answers["end_date_time"] = (answers["end_date_time_range_start"], answers["end_date_time_range_end"])


    # #  pyinstaller --onefile compare_price\compare_price.py
    else:

        answers = {
            "start_location": "chandigarh",
            "end_location": "bangalore",
            "start_date": "2019/01/27",
            "start_date_time": "06:00, 23:00",
            "end_date": "2019/02/25",
            "end_date_time": "06:00, 23:00",
            "return": True

        }

    answers
def get_location_code(location, validate_location = False):

    import pandas as pd
    df = pd.read_csv("india_country_code.csv")

    df_loc = df[df.apply(lambda row: location.lower() in row["City name"].lower(), axis=1)]
    if validate_location:
        if len(df_loc) != 0:
            return True
        else:
            return False
    return df_loc.iloc[0]["Airport Code"]

if __name__ == "__main__":
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    print(sys.argv)
    try:
        debug = bool(sys.argv[1])
    except Exception:
        debug = False

    get_input()
    try:
        start_date = answers["start_date"]
        if answers["return"]:
            end_date = answers["end_date"]
        else:
            end_date = None

        start_date_start_time, start_date_end_time = answers["start_date_time"]
        if answers["return"]:
            end_date_start_time, end_date_end_time = answers["end_date_time"]
        else:
            end_date_start_time, end_date_end_time = None, None



        start_location = get_location_code(answers["start_location"])
        end_location = get_location_code(answers["end_location"])

        pprint(f"{start_date}, {end_date}, {start_date_start_time}, {start_date_end_time}, {start_location}, {end_location}")

        price_obj = FindLowestPrice(start_date=start_date, end_date=end_date,
                                    start_location=start_location, end_location=end_location)
        start_price_list, end_price_list = price_obj.find_flight_in_time_range((start_date_start_time, start_date_end_time),
                                                                               (end_date_start_time, end_date_end_time))

        # pprint(start_price_list[0:3])


        def print_price(price_list):
            for price in price_list:
                def get_time_str(time):
                    return f"{time[0]}h {time[1]}m"
                pprint(f"Start time: {get_time_str(price['start_time'])}  Duration: {get_time_str(price['duration'])} "
                       f" End Time: {get_time_str(price['end_time'])}  Price: {price['price']} "
                       f" Flight ID : {price['flight_id']}  Site: {price['site']}")



        pprint("Cheapest start price is -> ")
        print_price(start_price_list[0:3])
        if end_price_list is not None:
            pprint("*"*60)
            print_price(end_price_list[0:3])
        print("help")
    except Exception as e:
        import traceback
        pprint(os.path.dirname(os.path.realpath(__file__)))
        pprint(traceback.format_exc())
        from time import sleep
        sleep(200)
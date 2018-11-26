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
from website_api import go_ibibo_find_price, makemytrip_find_price


class FindLowestPrice:
    def __init__(self, start_date, end_date, start_location, end_location):
        self.start_date = start_date
        self.end_location = end_location
        self.start_location = start_location
        self.end_date = end_date

    def _get_price_list(self, date):
        results = []
        results.extend(go_ibibo_find_price.GoIbibo().find_price(date, self.start_location, self.end_location))
        results.extend(makemytrip_find_price.MakeMyTrip().find_price(date, self.start_location, self.end_location))
        return results

    def _filter_by_time(self, start_price_list, start_time, end_time):

        filtered_time_list = list()
        for time in start_price_list:

            duration_actual = [0,0]

            duration_actual[0] = int(end_time[0]) - int(start_time[0])
            duration_actual[1] = int(end_time[1]) - int(start_time[1])

            if duration_actual[1] < 0:
                duration_actual[0] += 1

            if int(time["duration"][0]) > int(duration_actual[0]):
                continue

            if int(time["start_time"][0]) >= int(start_time[0]) and int(time["start_time"][1]) >= int(
                    start_time[1]) and int(time["start_time"][0]) <= int(end_time[0]) and int(time["start_time"][1]) <= int(
                    end_time[1]):
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
    def find_flight_in_time_range(self, start_date_time, end_date_time):
        start_price_list, end_price_list = self.find_lowest_price()

        start_price_list = self._filter_by_time(start_price_list, start_date_time[0], start_date_time[1])
        if end_date_time is None:
            return start_price_list, None
        end_price_list = self._filter_by_time(end_price_list, end_date_time[0], end_date_time[1])

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

    # TODO: Verify how the find_flight_in_time_range work with start_date_time
    # TODO: Allow to search with duration

if __name__ == "__main__":
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    # price_obj = FindLowestPrice(start_date=datetime.date(2018, 11, 11), end_date=datetime.date(2018, 11, 15),
    #                             start_location="DEL", end_location="BLR")
    # start_price_list, end_price_list = price_obj.find_flight_in_time_range(([10, 15], [17, 59]),
    #                                                                        ([10, 15], [22, 59]))
    #
    # # price_obj = FindLowestPrice(start_date=datetime.date(2018, 11, 11), end_date=None,
    #                             start_location="IXC", end_location="BLR")
    # start_price_list, end_price_list = price_obj.find_flight_in_time_range(([10, 15], [17, 59]),
    #                                                                        #None)
    # pprint("Start")
    # pprint(start_price_list[0:3])
    # if end_price_list is not None:
    #     pprint("*"*60)
    #     pprint(end_price_list[0:2])
    # print("help")
    #

    # from PyInquirer import prompt, print_json
    #
    # questions = [
    #     {
    #         'type': 'input',
    #         'name': 'dummy',
    #         'message': "Welcome to Compare Price!\n Lets get started? (Press Enter to begin)",
    #     },
    #     {
    #         "type": "list",
    #         "name": "start_location",
    #         "message": "Where is your trip starting from? ",
    #         "choices": [
    #             "Bangalore", "Chandigarh", "Patna", "Delhi",
    #         ],
    #     },
    #     {
    #         "type": "list",
    #         "name": "end_location",
    #         "message": "Where is your trip ending at? ",
    #         "choices": [
    #             "Bangalore", "Chandigarh", "Patna", "Delhi",
    #         ],
    #     },
    #     {
    #         "type": "confirm",
    #         "name": "return_journey",
    #         "message": "Is this a one way trip? ",
    #         'default': True,
    #     },
    #     {
    #         'type': 'input',
    #         'name': 'start_date',
    #         'message': "Which day you want to book your flight? (follow this format please : YYYY/MM/DD)",
    #     },
    #     {
    #         'type': 'input',
    #         'name': 'start_date_time',
    #         'message': "Between what time do you want your flight to be? (follow this format please : HH:MM, HH:MM )",
    #     },
    #     {
    #         'type': 'input',
    #         'name': 'end_date',
    #         'message': "Which day you want to book your flight? (follow this format please : YYYY/MM/DD)",
    #         "when" : lambda answers: answers["return_journey"]
    #     },
    #     {
    #         'type': 'input',
    #         'name': 'end_date_time',
    #         'message': "Between what time do you want your flight to be? (follow this format please : HH:MM, HH:MM )",
    #         "when" : lambda answers: answers["return_journey"]
    #     }
    #
    # ]
    #
    # answers = prompt(questions)

    answers = {
        "start_location" : "Chandigarh",
        "end_location" : "Bangalore",
        "start_date" : "2018/12/21",
        "start_date_time" : "14:00, 23:00",
        "end_date" : "2018/12/25",
        "end_date_time" : "14:00, 23:00",

    }
    try:
        # pprint(answers)


        def get_date(date):
            date = date.strip()
            date = date.split("/")
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            return date

        start_date = get_date(answers["start_date"])
        end_date = get_date(answers["end_date"])

        def get_time(time):
            time = time.strip()
            start_time, end_time = time.split(",")
            start_time = start_time.strip().split(":")
            end_time = end_time.strip().split(":")
            return start_time, end_time

        start_date_start_time, start_date_end_time = get_time(answers["start_date_time"])
        end_date_start_time, end_date_end_time = get_time(answers["end_date_time"])

        def get_location_code(location):
            dict_of_code = {
                    "Bangalore" : "BLR", "Chandigarh" : "IXC", "Patna" : "PAT", "Delhi" : "DEL",
            }
            return dict_of_code[location]

        start_location = get_location_code(answers["start_location"])
        end_location = get_location_code(answers["end_location"])

        pprint(f"{start_date}, {end_date}, {start_date_start_time}, {start_date_end_time}, {start_location}, {end_location}")

        price_obj = FindLowestPrice(start_date=start_date, end_date=end_date,
                                    start_location=start_location, end_location=end_location)
        # start_price_list, end_price_list = price_obj.find_flight_in_time_range((start_date_start_time, start_date_end_time),
        #                                                                        (end_date_start_time, end_date_end_time))

        start_price_list, end_price_list = price_obj.find_time_in_duration((1,20), (22,0), (4,20), (19,0))

        # pprint(start_price_list[0:3])

        # TODO: Have to see why the prettifying output step is failing. the dict format is wrong
        def print_price(price_list):
            for price in price_list:
                def get_time_str(time):
                    return f"{time[0]}h {time[1]}m"
                pprint(f"Start time: {get_time_str(price['start_time'])}  Duration: {get_time_str(price['duration'])}  End Time: {get_time_str(price['end_time'])}  Price: {price['price']}  Flight ID : {price['flight_id']}  Site: {price['site']}")



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
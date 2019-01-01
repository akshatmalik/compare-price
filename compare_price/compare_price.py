# from __future__ import print_function, unicode_literals

import sys

sys.path.insert(0, r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight")
import os
import sys
import datetime
from pprint import pprint
from website_api import makemytrip_find_price
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\website_api")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\compare_price")
sys.path.append(r"C:\Users\Akshat Malik\PycharmProjects\find_cheapest_flight\venv")


class FindLowestPrice:
    """
    Find the lowest price for the flight
    """
    def __init__(self, start_date: datetime, end_date: datetime, start_location: str, end_location: str):
        """
        Initalize the location and dates

        :param start_date:
        :param end_date:
        :param start_location:
        :param end_location:
        """
        self.start_date = start_date
        self.end_location = end_location
        self.start_location = start_location
        self.end_date = end_date

    def _get_price_list(self, date: datetime) -> list:
        """
        Takes in in date along with the date parameter and returns the consolidated price list from each website

        :param date: date for which the prices need to be found
        :return: List of flights for the given start date
        """

        results = []
        # results.extend(go_ibibo_find_price.GoIbibo().find_price(date, self.start_location, self.end_location))
        results.extend(makemytrip_find_price.MakeMyTrip().find_price(date, self.start_location, self.end_location))
        return results

    def _filter_by_time(self, price_list: list, start_time: datetime, end_time: datetime):
        """
        Find s flights between the start_time and end_time in price list given

        :param price_list:
        :param start_time:
        :param end_time:
        :return: List filtered with the time parameters
        """

        filtered_time_list = list()
        for time in price_list:

            if start_time <= time["start_time"] <= end_time:
                filtered_time_list.append(time)

        return filtered_time_list

    # noinspection PyShadowingNames
    def find_lowest_price(self):
        """
        Finds the price on the start location and end location if end location is given.

        :return: List of price list for start and end locations
        """
        start_price_list = self._get_price_list(self.start_date)
        start_price_list = sorted(start_price_list, key=lambda k: int(k['price']))

        if self.end_date is None:
            return start_price_list, None

        end_price_list = self._get_price_list(self.end_date)
        end_price_list = sorted(end_price_list, key=lambda k: int(k['price']))

        return start_price_list, end_price_list

    # noinspection PyShadowingNames
    def find_flight_in_time_range(self, start_date_times: (datetime, datetime), end_date_times: (datetime, datetime)):
        """
        Filters the found price list with the dats filters

        :param start_date_times: Tuple of start_date_time range. Its a tuple of start_time and end_time for the start
         date
        :param end_date_times: Tuple of end_date_time range. Its a tuple of start_time and end_time for the end
         date
        :return: The filtered list of start and end price list
        """
        start_price_list, end_price_list = self.find_lowest_price()

        start_price_list = self._filter_by_time(start_price_list, start_date_times[0], start_date_times[1])
        if end_date_times is None:
            return start_price_list, None
        end_price_list = self._filter_by_time(end_price_list, end_date_times[0], end_date_times[1])

        return start_price_list, end_price_list

    def find_time_in_duration(self, start_date_time, start_date_duration, end_date_time, end_date_duration):
        """
        Decrecated
        :param start_date_time:
        :param start_date_duration:
        :param end_date_time:
        :param end_date_duration:
        :return:
        """
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

import get_input

if __name__ == "__main__":
    import logging
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    print(sys.argv)
    try:
        debug = bool(sys.argv[1])
    except Exception:
        debug = False

    answers = get_input.get_input(debug)
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

        start_location = answers["start_location_code"]
        end_location = answers["end_location_code"]

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
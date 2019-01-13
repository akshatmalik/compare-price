# from __future__ import print_function, unicode_literals

import sys
from typing import Dict, List

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

    def __init__(self, start_date: List, end_date: List, start_location: str, end_location: str,
                 start_date_start_time: List, start_date_end_time: List,
                 end_date_start_time: List, end_date_end_time: List, ):
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
        self.start_date_start_time = start_date_start_time
        self.start_date_end_time = start_date_end_time
        self.end_date_start_time = end_date_start_time
        self.end_date_end_time = end_date_end_time


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
    def find_lowest_price(self) -> (Dict, Dict):
        """
        Finds the price on the start location and end location if end location is given.

        :return: List of price list for start and end locations
        """
        start_price_list = {}
        for date in self.start_date:
            start_price_list_temp = self._get_price_list(date)
            start_price_list_temp = sorted(start_price_list_temp, key=lambda k: int(k['price']))
            start_price_list[str(date.date())] = start_price_list_temp

        if self.end_date is None:
            return start_price_list, None

        end_price_list = {}
        for date in self.end_date:
            end_price_list_temp = self._get_price_list(date)
            end_price_list_temp = sorted(end_price_list_temp, key=lambda k: int(k['price']))
            end_price_list[str(date.date())] = end_price_list_temp

        return start_price_list, end_price_list

    # noinspection PyShadowingNames
    def find_flight_in_time_range(self):
        """
        Filters the found price list with the dats filters

        :param start_date_times: Tuple of start_date_time range. Its a tuple of start_time and end_time for the start
         date
        :param end_date_times: Tuple of end_date_time range. Its a tuple of start_time and end_time for the end
         date
        :return: The filtered list of start and end price list
        """
        # todo: duplicate this
        start_price_list, end_price_list = self.find_lowest_price()

        for date in start_price_list:
            start_price_list[date] = self._filter_by_time(start_price_list[date], self.start_date_start_time[date],
                                                          self.start_date_end_time[date])
        if self.end_date_start_time is None:
            return start_price_list, None
        for date in end_price_list:
            end_price_list[date] = self._filter_by_time(end_price_list[date], self.end_date_start_time[date],
                                                  self.end_date_end_time[date])

        return start_price_list, end_price_list

    # DEPRECATED
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
    while(True):
        try:
            start_date = answers["start_date"]
            if answers["return"]:
                end_date = answers["end_date"]
            else:
                end_date = None

            start_date_start_time = {}
            start_date_end_time = {}
            for date in answers["start_date_time"]:
                start_date_start_time[str(date[0].date())] = date[0]
                start_date_end_time[str(date[1].date())] = date[1]
            if answers["return"]:
                end_date_start_time = {}
                end_date_end_time = {}
                for date in answers["end_date_time"]:
                    end_date_start_time[str(date[0].date())] = date[0]
                    end_date_end_time[str(date[1].date())] = date[1]
            else:
                end_date_start_time, end_date_end_time = None, None

            start_location = answers["start_location_code"]
            end_location = answers["end_location_code"]


            pprint(f"{start_date}, {end_date}, {start_date_start_time}, {start_date_end_time}, {start_location}, {end_location}")

            price_obj = FindLowestPrice(start_date=start_date, end_date=end_date,
                                        start_location=start_location, end_location=end_location,
                                        start_date_start_time=start_date_start_time,
                                        start_date_end_time=start_date_end_time, end_date_start_time=end_date_start_time,
                                        end_date_end_time=end_date_end_time)

            start_price_list, end_price_list = price_obj.find_flight_in_time_range()

            # pprint(start_price_list[0:3])


            def print_price(price_list):
                for price in price_list:
                    pprint(f"Start time: {price['start_time']}  Duration: {price['duration']} "
                           f" End Time: {price['end_time']}  Price: {price['price']} "
                           f" Flight ID : {price['flight_id']}  Site: {price['site']}")


            pprint("Cheapest start price is -> ")
            for day in start_price_list.keys():
                pprint(f"Day - {day}"  )
                print_price(start_price_list[day][0:5])
            if end_price_list is not None:
                pprint("*"*60)
                for day in end_price_list.keys():
                    pprint(f"Day - {day}")
                    print_price(end_price_list[day][0:5])
                # print_price(end_price_list[0:3])
            print("help")
        except Exception as e:
            import traceback
            pprint(os.path.dirname(os.path.realpath(__file__)))
            pprint(traceback.format_exc())
            raise e
        from time import sleep
        sleep(get_input.get_int(answers["notification_time"]) * 60)
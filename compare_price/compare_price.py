import datetime
from pprint import pprint

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

            duration_actual[0] = end_time[0] - start_time[0]
            duration_actual[1] = end_time[1] - start_time[1]

            if duration_actual[1] < 0:
                duration_actual[0] += 1

            if int(time["duration"][0]) > int(duration_actual[0]):
                continue

            if int(time["start_time"][0]) >= int(start_time[0]) and int(time["start_time"][1]) >= int(
                    start_time[1]) and int(time["end_time"][0]) <= int(end_time[0]) and int(time["end_time"][1]) <= int(
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


if __name__ == "__main__":
    # price_obj = FindLowestPrice(start_date=datetime.date(2018, 11, 11), end_date=datetime.date(2018, 11, 15),
    #                             start_location="IXC", end_location="BLR")
    # start_price_list, end_price_list = price_obj.find_flight_in_time_range(([10, 15], [17, 59]),
    #                                                                        ([10, 15], [14, 59]))

    price_obj = FindLowestPrice(start_date=datetime.date(2018, 11, 11), end_date=None,
                                start_location="IXC", end_location="BLR")
    start_price_list, end_price_list = price_obj.find_flight_in_time_range(([10, 15], [17, 59]),
                                                                           None)
    pprint("Start")
    pprint(start_price_list[0:2])
    if end_price_list is not None:
        pprint("*"*60)
        pprint(end_price_list[0:2])
    print("help")

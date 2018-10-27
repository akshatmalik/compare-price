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
        results.extend(go_ibibo_find_price.find_price(date, self.start_location, self.end_location))
        results.extend(makemytrip_find_price.find_price(date, self.start_location, self.end_location))
        return results

    # noinspection PyShadowingNames
    def find_lowest_price(self):

        start_price_list = self._get_price_list(self.start_date)
        start_price_list = sorted(start_price_list, key=lambda k: k['price'])

        if self.end_date is None:
            return start_price_list, None

        end_price_list = self._get_price_list(self.end_date)
        end_price_list = sorted(end_price_list, key=lambda k: k['price'])

        return start_price_list, end_price_list

    def find_flight_in_time_range(self, start_time, end_time):
        pass


if __name__ == "__main__":
    price_obj = FindLowestPrice(start_date=datetime.date(2018, 11, 11), end_date=datetime.date(2018, 11, 15),
                                start_location="IXC", end_location="BLR")
    start_price_list, end_price_list = price_obj.find_lowest_price()
    pprint("Start")
    pprint(start_price_list[0:10])
    pprint("*"*60)
    pprint(end_price_list[0:10])
    print("help")

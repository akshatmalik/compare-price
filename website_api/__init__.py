import abc
import datetime
from typing import List


class Website(abc.ABC):
    """
    Template for the website class
    """

    def __init__(self):
        self._setup()

    @abc.abstractmethod
    def website_name(self):
        """
        name of the website
        :return:
        """
        pass

    @abc.abstractmethod
    def _setup(self):
        """
        Setup functions
        :return:
        """
        pass

    @abc.abstractmethod
    def _format_date(self, start_date: str) -> datetime:
        """
        Takes in string and return the datetime object for it

        :param start_date: date string
        :return:
        """
        return start_date

    @abc.abstractmethod
    def _format_price(self, price: str) -> str:
        """
        Take in the price and return the formatted str
        :param price:
        :return:
        """
        return price

    @abc.abstractmethod
    def _format_time(self, time: str) -> datetime:
        """
        Take in the time str and give the datetime for ut

        :param time:
        :return:
        """
        return time

    @abc.abstractmethod
    def _format_duration(self, time: str) -> datetime:
        """
        Take in the flight time and return the datetime duration for it

        :param time:
        :return:
        """
        return time

    @abc.abstractmethod
    def _format_flight_id(self, id: str) -> str:
        return id

    def find_price(self, start_date: datetime, start_location: str, end_location: str) -> List[dict]:
        """
        Applies the formatter functions to all the variables

        :param start_date:
        :param start_location:
        :param end_location:
        :return:
        """
        results = self._find_price(start_date, start_location, end_location)
        for result in results:
            result["price"] = self._format_price(result["price"])
            result["start_time"] = self._format_time(result["start_time"])
            result["end_time"] = self._format_time(result["end_time"])
            result["duration"] = self._format_duration(result["duration"])
            result["flight_id"] = self._format_flight_id(result["flight_id"])
            result["site"] = self.website_name()

        results = sorted(results, key=lambda k: k['price'])
        return results

    @abc.abstractmethod
    def _find_price(self, start_date: datetime, start_location: str, end_location: str) -> List[dict]:
        """
        Find the price and return the above formatted dictionary for it

        :param start_date:
        :param start_location:
        :param end_location:
        :return:
        """
        pass



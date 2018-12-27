import abc


class Website(abc.ABC):

    def __init__(self):
        self._setup()

    @abc.abstractmethod
    def website_name(self):
        pass

    @abc.abstractmethod
    def _setup(self):
        pass

    @abc.abstractmethod
    def _format_date(self, start_date):
        return start_date

    @abc.abstractmethod
    def _format_price(self, price):
        return price

    @abc.abstractmethod
    def _format_time(self, time):
        return time

    @abc.abstractmethod
    def _format_duration(self, time):
        return time

    @abc.abstractmethod
    def _format_flight_id(self, id):
        return id

    def find_price(self, start_date, start_location, end_location):
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
    def _find_price(self, start_date, start_location, end_location):
        pass



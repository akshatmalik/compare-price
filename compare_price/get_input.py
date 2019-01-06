import datetime
from pprint import pprint
from typing import List


def get_date(date: str) -> (datetime, None):
    """
    Takes the date from the answers and return the datettime object

    :param date: date in yyyy/mm/dd format
    :return:
    """
    date_parts = date.split("/")
    try:
        entered_date = datetime.datetime(year=int(date_parts[0]), month=int(date_parts[1]),
                                         day=int(date_parts[2]))
        if entered_date <= datetime.datetime.today():
            raise Exception("Falied compariosin")
        return entered_date
    except Exception as e:
        pprint(e)
        return None


def get_time(time: str, date: datetime) -> datetime:
    """
    Takes the time and date and returns the datetime object

    :param time: time in HH:MM format
    :param date: date as datetime object
    :return: the datetime object with the date as date and time as time
    """
    try:
        time_parts_start = time.strip().split(":")
        start_date_time = date
        start_date_time_start = start_date_time.replace(hour=int(time_parts_start[0]), minute=int(time_parts_start[1]))
        return start_date_time_start
    except Exception as e:
        print(e)
        return None


def get_location_code(location: str, validate_location: bool = False) -> {str, None}:
    """
    Takes in the location and returns the airport code. Limited only to India as of now

    :param location: city name you flying to
    :param validate_location: to just valicate the location or return the code
    :return:
    """
    import pandas as pd
    df = pd.read_csv("india_country_code.csv")

    df_loc = df[df.apply(lambda row: location.lower() in row["City name"].lower(), axis=1)]
    if validate_location:
        if len(df_loc) != 0:
            return True
        else:
            return False
    return df_loc.iloc[0]["Airport Code"]


def get_input(debug: bool) -> List[str]:
    """
    If it is debugging, then straight away give the answer key. Else ask for input

    :param debug: check for debug key
    :return: all the parameters for the ansheres
    """
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
        # TODO: Do the extra input and clean code
        questions_hi = [
            {
                'type': 'input',
                'name': 'dummy',
                'message': "Welcome to Compare Price!\nLets get started? (Press Enter to begin)",
            },
        ]
        answers = prompt(questions_hi)

        # LOCATIONS
        questions_start_location = [
            {
                'type': 'input',
                "name": "start_location",
                "message": "Where is your trip starting from? ",
            },
        ]

        answers = prompt(questions_start_location, answers)
        while get_location_code(answers["start_location"], True):
            answers = prompt(questions_start_location, answers)

        questions_end_location = [
            {
                'type': 'input',
                "name": "end_location",
                "message": "Where is your trip ending at? ",
            },
        ]
        answers = prompt(questions_end_location, answers)
        while get_location_code(answers["end_location"], True):
            answers = prompt(questions_end_location, answers)

        # RETURN JOURNEY
        questions_is_return_journey = [
            {
                "type": "confirm",
                "name": "return",
                "message": "Return trip? ",
                'default': False,
            },
        ]
        answers = prompt(questions_is_return_journey, answers)

        # START DATE
        questions_start_location_start_date = [
            {
                'type': 'input',
                'name': 'start_date',
                'message': "Which day you want to book your flight? (follow this format please : YYYY/MM/DD)",
            },
        ]
        answers = prompt(questions_start_location_start_date, answers)
        while get_date(answers["start_date"]) is None:
            answers = prompt(questions_start_location_start_date, answers)
        temp_date = [get_date(answers["start_date"])]
        answers["start_date"] = []
        answers["start_date"].extend(temp_date)

        # START DATE TIME RANGE -- START
        questions_start_location_time_range_start = [
            {
                'type': 'input',
                'name': 'start_date_time_range_start',
                'message': f"After what time are you looking flights for on {answers['start_date'][0].date()}? "
                           f"(Format HH:MM)",
            },
        ]
        answers = prompt(questions_start_location_time_range_start, answers)

        while get_time(answers["start_date_time_range_start"], answers["start_date"][0]) is None:
            answers = prompt(questions_start_location_time_range_start, answers)

        # START DATE TIME RANGE -- END
        questions_start_location_time_range_end = [
            {
                'type': 'input',
                'name': 'start_date_time_range_end',
                'message': f"Till what time are you looking flights for on {answers['start_date'][0].date()}? "
                           f"(Format HH:MM)",
            },
        ]
        answers = prompt(questions_start_location_time_range_end, answers)

        while get_time(answers["start_date_time_range_end"], answers["start_date"][0]) is None:
            answers = prompt(questions_start_location_time_range_end, answers)

        # MULTIPLE DATE RANGES
        questions_multiple_dates = [
            {
                'type': 'confirm',
                'name': 'multiple_dates',
                "message": "Do you want to track multiple dates? ",
                'default': False,
            }
        ]
        answers = prompt(questions_multiple_dates, answers)

        if answers["multiple_dates"] is True:

            # MULTIPLE DATE RANGES -- START
            questions_start_location_start_date = [
                {
                    'type': 'input',
                    'name': 'start_date_append',
                    'message': "Which day you want to book your flight? (follow this format please : YYYY/MM/DD)",
                },
            ]

            questions_do_you_want_to_enter_another_date = [
                {
                    'type': 'confirm',
                    'name': 'enter_another_date',
                    "message": "Do you want to enter another date?",
                    'default': False,
                }
            ]

            loop = True
            while loop:
                answers = prompt(questions_start_location_start_date, answers)
                while get_date(answers["start_date_append"]) is None:
                    answers = prompt(questions_start_location_start_date, answers)
                answers["start_date"].append(get_date(answers["start_date_append"]))
                answers = prompt(questions_do_you_want_to_enter_another_date, answers)
                loop = answers["enter_another_date"]

        # MAKE START DATE TIMES
        answers["start_date_time"] = []
        for date in answers["start_date"]:
            pprint(date)
            start_date_range = get_time(answers["start_date_time_range_start"], date)
            end_date_range = get_time(answers["start_date_time_range_end"], date)
            answers["start_date_time"].append((start_date_range, end_date_range))
            pprint(answers)

        # RETURN JOURNEY THINGS NOW
        if answers["return"]:

            # END DATE
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
            temp_date = [get_date(answers["end_date"])]
            answers["end_date"] = []
            answers["end_date"].extend(temp_date)

            # END DATE -- START TIME
            questions_end_location_time_range_start = [
                {
                    'type': 'input',
                    'name': 'end_date_time_range_start',
                    'message': f"After what time are you looking flights for on {answers['end_date'][0].date()}? "
                               f"(Format HH:MM)",
                },
            ]
            answers = prompt(questions_end_location_time_range_start, answers)

            while get_time(answers["end_date_time_range_start"], answers['end_date'][0]) is None:
                answers = prompt(questions_end_location_time_range_start, answers)

            # END DATE -- END TIME
            questions_start_location_time_range_end = [
                {
                    'type': 'input',
                    'name': 'end_date_time_range_end',
                    'message': f"Till what time are you looking flights for on {answers['end_date'][0].date()}? "
                               f"(Format HH:MM)",
                },
            ]
            answers = prompt(questions_start_location_time_range_end, answers)

            while get_time(answers["end_date_time_range_end"], answers['end_date'][0]) is None:
                answers = prompt(questions_start_location_time_range_end, answers)

            # MULTIPLE DATES
            questions_multiple_dates = [
                {
                    'type': 'confirm',
                    'name': 'multiple_dates',
                    "message": "Do you want to track multiple dates? ",
                    'default': False,
                }
            ]
            answers = prompt(questions_multiple_dates, answers)

            if answers["multiple_dates"] is True:

                # LOOP MULTIPLE DATES
                questions_start_location_start_date = [
                    {
                        'type': 'input',
                        'name': 'end_date_append',
                        'message': "Which day you want to book your flight? (follow this format please : YYYY/MM/DD) \n",
                    },
                ]

                questions_do_you_want_to_enter_another_date = [
                    {
                        'type': 'confirm',
                        'name': 'enter_another_date',
                        "message": "Do you want to enter another date?",
                        'default': False,
                    }
                ]

                loop = True
                while loop:
                    answers = prompt(questions_start_location_start_date, answers)
                    while get_date(answers["end_date_append"]) is None:
                        answers = prompt(questions_start_location_start_date, answers)
                    answers["end_date"].append(get_date(answers["end_date_append"]))
                    answers = prompt(questions_do_you_want_to_enter_another_date, answers)
                    loop = answers["enter_another_date"]

            # MAKE START DATE TIMES
            answers["end_date_time"] = []
            for date in answers["end_date"]:
                start_date_range = get_time(answers["end_date_time_range_start"], date)
                end_date_range = get_time(answers["end_date_time_range_end"], date)
                answers["end_date_time"].append((start_date_range, end_date_range))

            answers["start_location_code"] = get_location_code(answers["start_location"])
            answers["end_location_code"] = get_location_code(answers["end_location"])

        # pprint(answers)

    # #  pyinstaller --onefile compare_price\compare_price.py
    else:

        answers = {
            "start_location": "chandigarh",
            "end_location": "bengaluru",
            "start_date": [datetime.datetime(2019, 2, 1), datetime.datetime(2019, 2, 2), datetime.datetime(2019, 2, 3)],
            "start_date_time": [(datetime.datetime(2019, 2, 1, 9, 0), datetime.datetime(2019, 2, 1, 23, 0)),
                                (datetime.datetime(2019, 2, 2, 9, 0), datetime.datetime(2019, 2, 2, 23, 0)),
                                (datetime.datetime(2019, 2, 3, 9, 0), datetime.datetime(2019, 2, 3, 23, 0))],
            "end_date_time": [(datetime.datetime(2019, 3, 1, 9, 0), datetime.datetime(2019, 3, 1, 23, 0)),
                              (datetime.datetime(2019, 3, 2, 9, 0), datetime.datetime(2019, 3, 2, 23, 0)),
                              (datetime.datetime(2019, 3, 3, 9, 0), datetime.datetime(2019, 3, 3, 23, 0))],
            "end_date": [datetime.datetime(2019, 3, 1), datetime.datetime(2019, 3, 2), datetime.datetime(2019, 3, 3)],
            "return": True,
            "start_location_code": "IXC",
            "end_location_code": "BLR",
        }

    return answers

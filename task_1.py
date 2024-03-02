import os
from datetime import datetime, timedelta

os.system('clear')

TIME_FORMAT = "%H:%M:%S"
YEARS = 365
MONTHS = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = 24
MINUTES = 60
SECONDS = 60

"""
1. find additional days from start_time to next_day
2. find additional seconds from 00:00:00 to end_hours end_minutes end_seconds
3. subtract days from years
"""


def from_start_time_to_next_day(start_time):
    """
    find how many seconds until next_day from start_time
    """
    temp_time = datetime.strptime(start_time, TIME_FORMAT)
    end_of_date = datetime.strptime("23:59:59", TIME_FORMAT)

    return (end_of_date - temp_time + timedelta(seconds=1)).seconds


def from_midnight_to_end_time(end_time):
    """
    find seconds from midnight to end time
    """
    time = datetime.strptime(end_time, TIME_FORMAT)
    return timedelta(hours=time.hour, minutes=time.minute, seconds=time.second).seconds


def seconds_to_days(seconds):
    return timedelta(seconds=seconds)


def subtract_dates(date1_str, date2_str, date_format='%m-%d'):
    # Convert strings to datetime objects
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    # Perform subtraction
    difference = date1 - date2

    return difference


def main():
    s_year, s_month, s_days, s_hours, s_minutes, s_seconds = tuple(map(int, input().split()))
    e_year, e_month, e_days, e_hours, e_minutes, e_seconds = tuple(map(int, input().split()))
    start_time = f'{s_hours}:{s_minutes}:{s_seconds}'
    end_time = f'{e_hours}:{e_minutes}:{e_seconds}'

    # main_days are from rounded days to end_days includes years month's days
    result_days = 0
    result_seconds = 0
    days_in_years = (e_year - s_year) * YEARS

    start_month = s_month
    start_day = s_days + 1
    if MONTHS[s_month] < s_days + 1:
        start_month = 1 if s_month + 1 > 12 else s_month + 1
        start_day = 1

    end_month = e_month
    end_day = e_days

    result_days += subtract_dates(f'{end_month}-{end_day}', f'{start_month}-{start_day}').days

    result_days += days_in_years

    additional_days_and_secs = seconds_to_days(
        from_start_time_to_next_day(start_time) + from_midnight_to_end_time(end_time)
    )

    result_days += additional_days_and_secs.days
    result_seconds += additional_days_and_secs.seconds

    print(result_days, result_seconds)


if __name__ == '__main__':
    main()

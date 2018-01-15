import datetime
from dateutil.relativedelta import relativedelta

day_dict = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}


def meetup_day(year, month, day_of_the_week, which):
    start_day = datetime.date(year, month, 1)
    direction = 1
    if which in ('second', '2nd'):
        start_day = datetime.date(year, month, 1+7)
        direction = 1
    elif which in ('third', '3rd'):
        start_day = datetime.date(year, month, 1+2*7)
        direction = 1
    elif which in ('fourth', '4th'):
        start_day = datetime.date(year, month, 1+3*7)
        direction = 1
    elif which in ('fifth', '5th'):
        start_day = datetime.date(year, month, 1+4*7)
        direction = 1
    elif which == 'last':
        start_day = datetime.date(year, month, 1) + relativedelta(months=1, days=-1)
        direction = -1
    elif which == 'teenth':
        start_day = datetime.date(year, month, 13)
        direction = 1

    while start_day.isoweekday() != day_dict.get(day_of_the_week):
        start_day += datetime.timedelta(days=direction)
    return start_day


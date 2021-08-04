from django.http import HttpResponse
from datetime import datetime


def get_time():
    time_is_now = datetime.strftime(datetime.now(), '%H:%M')
    time_str = f'Московское время: {time_is_now}'
    return time_str

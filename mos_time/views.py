from django.http import HttpResponse
from datetime import datetime


def get_time(request):
    time_is_now = datetime.strftime(datetime.now(), '%H:%M')
    html = f'Московское время: {time_is_now}'
    return HttpResponse(html)

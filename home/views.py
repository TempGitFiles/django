from django.shortcuts import render
from mos_time.views import *


def index(request):
    context = {'mos_time': get_time()}
    return render(request, 'home/index.html', context)

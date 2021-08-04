from django.shortcuts import render
from mos_time.views import *
from tovar.models import *

def get_tovar_list():
    tovar_list = ['Товар 1', 'Товар 2', 'Товар 3']
    return tovar_list


def index(request):
    tovar = Tovar.objects.all()
    context = {'tovar': tovar, 'mos_time': get_time()}
    return render(request, 'tovar/index.html', context)

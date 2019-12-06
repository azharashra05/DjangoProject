from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def time_info_view(request):
    time=datetime.datetime.now()
    response='<h1 style="color:green">Hello current date and time at server is: '+str(time)+'</h1>'
    return HttpResponse(response)

from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    response='<h1 style="color:green">The current Date and Time at Sever is: '+str(date)+'</h1>'
    return HttpResponse(response)

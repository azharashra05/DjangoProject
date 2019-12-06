from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h1 style="color:red">Hello Friend Good Morning</h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1 style="color:blue">Hello Friend Good AfterNoon</h1>')


def good_evening_view(request):
    return HttpResponse('<h1 style="color:green">Hello Friend Good Evening</h1>')

def good_night_view(request):
    return HttpResponse('<h1 style="color:yellow">Hello Friend Good Night</h1>')

def thank_you_view(request):
    return HttpResponse('<h1 style="color:black">Thank You for visting our website</h1>')

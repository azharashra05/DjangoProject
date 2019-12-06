from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('<h1 style="color:pink">Response from First view</h1>')

def second_view(request):
    return HttpResponse('<h1 style="color:yellow">Response from Second view</h1>')

def third_view(request):
    return HttpResponse('<h1 style="color:red">Response from Third view</h1>')

def fourth_view(request):
    return HttpResponse('<h1 style="color:green">Response from Fourth view</h1>')

def fifth_view(request):
    return HttpResponse('<h1 style="color:blue">Response from Fifth view</h1>')

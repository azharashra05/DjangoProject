from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world_view(requset):
    return HttpResponse('<h1 style="color:blue">This is Response From Django Project</h1>')

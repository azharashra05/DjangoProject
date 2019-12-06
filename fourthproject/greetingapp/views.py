from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting_view(request):
    return HttpResponse("""<h1>Welcome to our website</h1>
    <h1 style="color:blue">Hello Friend Good Morning...Have a nice day</h1>
    <p1>Thanks for visiting our website</p1><br>
    <a href="https://www.youtube.com/watch?v=DH4fJaF6lMI">click here</a>
    """)

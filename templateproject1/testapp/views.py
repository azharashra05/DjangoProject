from django.shortcuts import render
import datetime


# Create your views here.
def template_view(request):
    dt=datetime.datetime.now()
    name="Azhar"
    roll_no=37
    marks=86
    my_dict={'date':dt,'name':name,'roll_no':roll_no,'marks':marks}
    return render(request,'testapp/results.html',context=my_dict)

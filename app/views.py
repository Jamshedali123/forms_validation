from django.shortcuts import render

# Create your views here.

from app.forms import *

from django.http import HttpResponse

def Student(request):
    SFEO=Studentform()
    d={'SFEO':SFEO}


    if request.method=='POST':
        SFDO=Studentform(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')

    return render(request,'Student.html',d)

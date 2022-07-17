from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    return render(request,'hello/index.html')

def denny(request):
    return HttpResponse('hello, denny!')

def date(request):
    time=datetime.datetime.now()
    return HttpResponse(time)

def greet(request,name):
    time=datetime.datetime.now()
    return render(request,'hello/greet.html',{'name':name,'time':time})


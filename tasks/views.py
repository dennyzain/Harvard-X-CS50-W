from django.shortcuts import render
# Create your views here.

def index(request):
    lists=['hermione', 'harry', 'ron']
    return render(request,'tasks/contents/index.html',{'lists':lists})

def add(request):
    return render(request,'tasks/contents/add.html')
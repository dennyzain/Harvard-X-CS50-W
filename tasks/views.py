from django.shortcuts import render
# Create your views here.

def index(request):
    lists=['hermione', 'harry', 'ron']
    return render(request,'index.html',{'lists':lists})

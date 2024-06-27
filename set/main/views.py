from django.shortcuts import render
from .models import New,User

def index(request):
    return render(request, 'main/index.html')

def news(request):
    news = New.objects.all()
    return render(request, 'main/news.html', {'news': news})

def event(request):
    return render(request, 'main/event.html')

def info(request):
    return render(request, 'main/info.html')

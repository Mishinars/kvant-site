from django.shortcuts import render
from django.http import FileResponse
from .models import *
import os


def index(request):
    return render(request, 'main/index.html')

def news(request):
    news = New.objects.all()
    return render(request, 'main/news.html', {'news': news})

def event(request):
    event = Event.objects.all()
    return render(request, 'main/event.html',{'event': event})

def info(request):
    return render(request, 'main/info.html')

def khimiya(request):
    return render(request, 'main/khimiya/main.html')

def fizika(request):
    return render(request, 'main/fizika/main.html')

def biologiya(request):
    return render(request, 'main/biologiya/main.html')

def robototekhnika(request):
    return render(request, 'main/robototekhnika/main.html')

def info_tech(request):
    return render(request, 'main/info_tech/main.html')

def hi_tech(request):
    return render(request, 'main/hi_tech/main.html')

def aero(request):
    return render(request, 'main/aero/main.html')



def pdf_view(request):  # функция для обращения к файлу(для нового файла создается новая)
    pdf_path = os.path.join('media', 'documents/zaglushka.pdf')
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')


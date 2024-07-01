from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('', index, name='Home'),
    path('news', news, name='news'),
    path('event', event, name='event'),
    path('info', info, name='info'),
    path('khimiya', khimiya, name='khimiya'),
    path('fizika', fizika, name='fizika'),
    path('biologiya', biologiya, name='biologiya'),
    path('robototekhnika', robototekhnika, name='robototekhnika'),
    path('info_tech', info_tech, name='info_tech'),
    path('hi_tech', hi_tech, name='hi_tech'),
    path('aero', aero, name='aero'),

    path('pdf/', pdf_view, name='pdf_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

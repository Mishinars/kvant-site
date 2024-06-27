from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('', index, name='Home'),
    path('news', news, name='news'),
    path('event', event, name='event'),
    path('info', info, name='info'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

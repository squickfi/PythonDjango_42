from django.urls import path

from ex01.views import *

urlpatterns = [
    path('django', django),
    path('display', display),
    path('templates', templates)
]
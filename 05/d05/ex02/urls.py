from django.urls import path
from ex02.views import *

urlpatterns = [
    path('init/', init),
    path('populate/', populate),
    path('display/', display),
]

from django.urls import path
from ex06.views import *


urlpatterns = [
    path('init/', init),
    path('populate/', populate),
    path('display/', display),
    path('update/', update)
]

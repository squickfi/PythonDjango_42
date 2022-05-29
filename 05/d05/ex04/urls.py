from django.urls import path
from ex04.views import *


urlpatterns = [
    path('init/', init),
    path('populate/', populate),
    path('display/', display),
    path('remove/', remove)
]

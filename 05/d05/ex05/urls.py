from django.urls import path
from ex05.views import *


urlpatterns = [
    path('populate/', populate),
    path('display/', display),
    path('remove/', remove)
]

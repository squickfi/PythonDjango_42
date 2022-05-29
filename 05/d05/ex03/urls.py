from django.urls import path
from ex03.views import *

urlpatterns = [
    path('populate/', populate),
    path('display/', display)
]

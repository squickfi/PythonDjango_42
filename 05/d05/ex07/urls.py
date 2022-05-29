from django.urls import path
from ex07.views import *


urlpatterns = [
    path('populate/', populate),
    path('display/', display),
    path('update/', update)
]

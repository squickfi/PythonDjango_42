from django.urls import path

from ex00.views import index

urlpatterns = [
    path('', index)
]
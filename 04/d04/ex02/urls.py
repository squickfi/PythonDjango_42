from django.urls import path

from ex02.views import index

urlpatterns = [
    path('', index)
]
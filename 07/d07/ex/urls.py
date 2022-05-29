from django.urls import path

from ex.views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('articles/', Articles.as_view(), name='articles'),
    path('articles/<slug:pk>', Detail.as_view(), name='articles_detail'),
    path('login/', Login.as_view(), name='login'),
    path('publications/', Publications.as_view(), name='publications'),
    path('detail/', Detail.as_view(), name='detail'),
    path('logout/', Logout.as_view(), name='logout'),
    path('favourite/', Favourite.as_view(), name='favourite'),
    path('publish/', Publish.as_view(), name='publish'),
    path('register/', Register.as_view(), name='register')
]

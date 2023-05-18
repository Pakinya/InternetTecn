from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='home'),
    path('goroskop', views.goroskop, name='zodiak'),
    path('result', views.result, name='result'),
    path('news', views.news, name='news')

]
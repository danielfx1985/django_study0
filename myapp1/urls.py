from django.urls import include, path

from django.contrib import admin
from django.urls import path
from myapp1 import views
urlpatterns = [

    path('',views.index),
    path('/test',views.test),
    path('/wenzhang',views.get_wenzhang),
    path('/news_list',views.news_list),
]

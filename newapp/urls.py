from django.contrib import admin
from django.urls import path
from django.urls import include
from newapp import views

app_name = 'newapp'

urlpatterns = [
path('', views.index, name='index'),
]
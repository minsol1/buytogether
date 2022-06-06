from django.contrib import admin
from django.urls import path
from AIchat import views

urlpatterns = [
    path('', views.AIhome,name='AIhome'), 
]
from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.login , name='login'),
    path('join',views.join , name='join'),
    path('logout',views.logout, name='logout'),
]
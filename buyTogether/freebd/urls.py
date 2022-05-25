from django.urls import path
from freebd import views

urlpatterns = [
    path('',views.freehome),
    path('freeCreate/', views.freeCreate),
]

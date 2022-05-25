from django.urls import path
from purbd import views

urlpatterns = [
    path('',views.home),
    path('necessity/',views.necessity),
    path('ott/',views.ott),
    path('food/',views.food),
    path('delivery/',views.delivery),
    path('create/',views.create),
  #  path('',views.createpur),

]
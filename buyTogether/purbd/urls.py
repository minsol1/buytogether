from django.urls import path
from purbd import views

urlpatterns = [
    path('',views.home , name='home'),
    path('purhome',views.phome, name='purhome'),
    path('category/<str:category>',views.p_category, name='category'),
    path('create',views.create , name='create'),
    path('detail/<int:post_id>',views.detail,name='detail'),
  #  path('',views.createpur),

]
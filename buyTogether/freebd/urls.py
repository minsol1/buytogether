from django.urls import path
from freebd import views

urlpatterns = [
    path('',views.freehome, name = 'freehome'),
    path('freeCreate/', views.freeCreate, name='freeCreate'),
    path('freeDetail/<int:free_id>', views.freedetail, name='freeDetail'),
    path('create_comment/<int:free_id>',views.create_comment, name='create_comment'),
]

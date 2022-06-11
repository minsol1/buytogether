from django.urls import path
from users import views

urlpatterns = [
    path('<str:user_name>',views.profilehome,name="profilehome"),
]

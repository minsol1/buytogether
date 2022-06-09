from django.urls import path
from users import views

urlpatterns = [
    path('<str:user_id>/',views.profilehome,name="profilehome"),
]

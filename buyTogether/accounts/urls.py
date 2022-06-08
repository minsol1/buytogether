from django.urls import path
from accounts import views

urlpatterns = [
    path('',views.login_views , name='login'),
    path('signup/', views.signup, name="signup"),
    path('logout/',views.logout_views, name='logout'),
]
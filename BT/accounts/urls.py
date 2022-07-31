from django.urls import path
from rest_auth.views import LoginView, LogoutView, PasswordChangeView,PasswordResetView, PasswordResetConfirmView
from accounts import views 
urlpatterns = [

    # 회원가입
    # path('rest-auth/registration', RegisterView.as_view(), name='join'),

]

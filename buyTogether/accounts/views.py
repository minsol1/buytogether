from pickle import NONE
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from .forms import UserSignupform,UserLoginform
from .models import User

# Create your views here.

def login_views(request):
    if request.method =='POST': #데이터베이스와 관련된 요청이면
        userID = request.POST['userID']
        password = request.POST['password']
        user = authenticate(userID=userID, password=password)
		#요청한 user와 데이터베이스의 user가 같은지 확인(인증)
        if user is not None: #user가 맞으면
            login(request, user)#login
        return redirect('home')
    else:
        form = UserLoginform()
        return render(request, 'accounts/login.html',{'form':form})

def logout_views(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserSignupform(request.POST)
        if form.is_valid():
            if request.POST['password'] == request.POST['password2']:
                user = form.save()
                login(request, user)
                # user = User.objects.create_user(
            #     userID = request.POST['userID'],
            #     nickname = request.POST['nickname'],
            #     password = request.POST['password'],
            #     email = request.POST['email'],
            # )
            # auth.login(request, user)
            return redirect('home')
        
            
        return render(request, 'accounts/signup.html',{'form':form})
    else:
        form = UserSignupform()
    return render(request, 'accounts/signup.html',{'form':form})

from django.shortcuts import redirect, render
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login()
            return redirect('home')
        else:
            render(request,'accounts/bad_login.html')
    else:
        return render(request,'accounts/login.html')

def join(request):
    return render(request,'accounts/join.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
from django.shortcuts import redirect, render
from .forms import Purmodelform
# Create your views here.

def home(request):
    return render(request,'purbd/home.html')

def food(request):
    # 글을 띄우는 코드
    return render(request,'purbd/food.html')

def necessity(request):
    return render(request,'purbd/necessity.html')

def delivery(request):
    return render(request,'purbd/delivery.html')

def ott(request):
    return render(request,'purbd/ott.html')

def create(request):
    if request.method == 'POST':
        form = Purmodelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form  = Purmodelform()
    return render(request,'purbd/create.html', {'form':form})
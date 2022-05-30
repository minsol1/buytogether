from django.shortcuts import get_object_or_404, redirect, render
from .forms import Purmodelform
from .models import Pur
# Create your views here.

def home(request):
    return render(request,'purbd/home.html')

def p_category(request,category):
    categorys={'food':0,'necessity':1,'ott':2,'delivery':3}
    posts = Pur.objects.filter(category=categorys[category])
    return render(request,'purbd/category.html',{'category':category,'posts':posts})

def detail(request, post_id):
    detail= get_object_or_404(Pur,id=post_id)
    return render(request, 'purbd/detail.html',{'detail':detail})

def create(request):
    if request.method == 'POST':
        form = Purmodelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form  = Purmodelform()
    return render(request,'purbd/create.html', {'form':form})
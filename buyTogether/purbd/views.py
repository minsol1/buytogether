from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import Purmodelform
from .models import Pur
from accounts.models import User
# Create your views here.

def home(request):
    return render(request,'home.html')

def phome(request):
    purchase = Pur.objects
    post_list = purchase.all().order_by('-id') #최신순 나열
    paginator = Paginator(post_list, 9) # 6개씩 잘라내기
    page = request.GET.get('page') # 페이지 번호 알아오기
    posts = paginator.get_page(page) # 페이지 번호 인자로 넘겨주기
    return render(request,'purbd/home.html',{'purchase':purchase, 'posts':posts})


def p_category(request,category):
    categorys={'food':0,'necessity':1,'ott':2,'delivery':3}

    posts = Pur.objects.filter(category=categorys[category]).order_by('-id') #최신순 나열
    return render(request,'purbd/category.html',{'category':category,'posts':posts})

def detail(request, post_id):
    detail= get_object_or_404(Pur,id=post_id)
    return render(request, 'purbd/detail.html',{'detail':detail})

def create(request):
    user_id =request.user.userID
    if request.method == 'POST':
        form = Purmodelform(request.POST)
        if form.is_valid():
            finished_form =form.save(commit=False)
            finished_form.ID=get_object_or_404(User,userID=user_id)
            finished_form.save()
            return redirect('home')
    else:
        form  = Purmodelform()
    return render(request,'purbd/create.html', {'form':form})


def auth(request):
    return render(request,'purbd/auth.html')

# def join(request,user_id):
#     post = Pur()
#     post.joinID.append(user_id)
#     post.save()
#     return redirect('purhome')
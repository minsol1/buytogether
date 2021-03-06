from django.shortcuts import render,redirect,get_object_or_404
from .forms import Freemodelform,CommentForm
from .models import Free
from accounts.models import User

# Create your views here.
def freehome(request):
    posts= Free.objects.filter().order_by('-writeDate')

    return render(request,'freebd/freehome.html',{'posts':posts})

def freeCreate(request):
    user_id =request.user.userID
    if request.method == 'POST':
        form = Freemodelform(request.POST)
        if form.is_valid():
            finished_form =form.save(commit=False)
            finished_form.ID=get_object_or_404(User,userID=user_id)
            finished_form.save()
            return redirect('freehome')
    else:
        form  = Freemodelform()
    return render(request,'freebd/freeCreate.html', {'form':form})

def freedetail(request, free_id):
    detail = get_object_or_404(Free,pk=free_id)
    comment_form = CommentForm()
    return render(request,'freebd/detail.html',{'detail':detail,'comment_form':comment_form})

def create_comment(request, free_id):
    filled_form = CommentForm(request.POST)
    user_id =request.user.userID

    if filled_form.is_valid():
        finished_form =filled_form.save(commit=False)
        finished_form.freeId=get_object_or_404(Free,pk=free_id)
        finished_form.ID=get_object_or_404(User,userID=user_id)
        finished_form.save()

    return redirect('freeDetail',free_id)
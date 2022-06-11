from django.shortcuts import get_object_or_404, render
from accounts.models import User
from purbd.models import Pur
# Create your views here.
def profilehome(request,user_name):
    user = get_object_or_404(User, username=user_name)
    p_post =  Pur.objects.filter(ID=user).order_by('-writeDate')


    return render(request,'users/profile.html',{'user':user , 'p_post':p_post})
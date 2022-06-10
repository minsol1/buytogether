from django.shortcuts import get_object_or_404, render
from accounts.models import User
# Create your views here.
def profilehome(request,user_name):
    user = get_object_or_404(User, username=user_name)
    return render(request,'users/profile.html',{'user':user})
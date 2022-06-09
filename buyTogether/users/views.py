from django.shortcuts import get_object_or_404, render

# Create your views here.
def profilehome(request,user_id):
    user = get_object_or_404(id=user_id)
    return render(request,'users/profile.html',{'user':user})
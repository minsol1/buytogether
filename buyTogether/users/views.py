from django.shortcuts import render

# Create your views here.
def profilehome(request):
    return render(request,'users/profile.html')
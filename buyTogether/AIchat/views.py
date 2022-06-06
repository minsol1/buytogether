from django.shortcuts import render

# Create your views here.
def AIhome(request):
    return render(request, 'AIchat/home.html')
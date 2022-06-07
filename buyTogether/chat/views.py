from django.shortcuts import render

# Create your views here.

def chathome(request):
    return render(request, 'chat/home.html')
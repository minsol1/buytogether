from django.shortcuts import render

# Create your views here.
def freehome(request):
    return render(request,'freebd/freehome.html')

def freeCreate(request):
    return render(request, 'freebd/freeCreate.html')
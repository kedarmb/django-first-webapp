from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def register(request):
    return render(request,'registration.html')

def thanks(request):
    return render(request,'thanks.html')
@csrf_protect
def login(request):
    return render(request,'login.html')
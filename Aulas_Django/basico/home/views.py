from django.shortcuts import render #Type: ignore
#from django.http import HttpResponse

def home(request):
    print('home')
    return render(request, 'assets_home/index.html')
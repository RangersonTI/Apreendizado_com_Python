from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    print('home')
    return render(request, 'assets_home/home.html')
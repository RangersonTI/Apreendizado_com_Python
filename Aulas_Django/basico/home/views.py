from django.shortcuts import render #Type: ignore
#from django.http import HttpResponse

def home(request):
    print('home')
    
    var = {
        'title': 'Home',
        'text': 'Minha Home'
    }
    return render(request, 'assets_home/index.html', var)
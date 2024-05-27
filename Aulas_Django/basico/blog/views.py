from django.shortcuts import render # type: ignore
#from django.http import HttpResponse

def blog(request):
    print("Olá, tudo bem?")
    return render(request,'assets_blog/blog.html')

def exemplo(request):
    return render(request,'assets_blog/exemplo.html')
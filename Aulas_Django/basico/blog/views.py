#from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    print("Olá, tudo bem?")
    return HttpResponse("<b>Olá, aqui é Django no blog</b>")

def exemplo(request):
    return HttpResponse("<i> Exemplo do blog </i>"+
                        '<br><br><a href="/blog/"><button> Salve </button></a>')
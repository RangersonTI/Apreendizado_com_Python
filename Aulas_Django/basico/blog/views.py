from django.shortcuts import render # type: ignore
#from django.http import HttpResponse

def blog(request):
    print("Olá, tudo bem?")
    title = {
        'title': 'Blog'
        }
    return render(request,'assets_blog/blog.html', title)

def exemplo(request):
    
    text = '<b>Erro Windows XP</b>'
    number = '4'
    var = {
        'title': 'Erro do Windows XP',
        'text': 'Erro do Windows XP'
    }
    
    return render(request,'assets_blog/exemplo.html', var)
from django.shortcuts import render
from .models import Category, Article

def articles(request) :
    articles = Article.objects.all()

     

    return render(request,'articles/list.html' , {
        'title' : 'Artículos',
        'articles': articles

    })
# Create your views here.

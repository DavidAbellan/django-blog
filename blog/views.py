from django.shortcuts import get_object_or_404, render
from .models import Category, Article

def articles(request) :
    articles = Article.objects.all()

     

    return render(request,'articles/list.html' , {
        'title' : 'Artículos',
        'articles': articles

    })

def article(request, article_id) :
    article = get_object_or_404(Article, id = article_id)
    return render(request, 'articles/detail.html', {
        'Articulo' : article
    })    
# Create your views here.

from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import Category, Article

###Paginación
from django.core.paginator import Paginator

def articles(request) :
    #sacar artículos
    articles = Article.objects.all()
    #paginar articulos
    paginator = Paginator(articles, 5)
    #Recoger numero pagina
    page_number = request.GET.get('page')
    page_articles = paginator.get_page(page_number)

     

    return render(request,'articles/list.html' , {
        'title' : 'Artículos',
        'articles': page_articles

    })

def article(request, article_id) :
    article = get_object_or_404(Article, id = article_id)
    return render(request, 'articles/detail.html', {
        'Articulo' : article
    })    
# Create your views here.

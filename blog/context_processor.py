from blog.models import Category, Article

def get_categories(request) :
    ids = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.values_list('id','name')
    return {
        'categories' : categories,
        'ids' : ids
    }

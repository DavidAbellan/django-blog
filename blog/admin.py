from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin) :
    readonly_fields = ('created_at',)
class ArticleAdmin(admin.ModelAdmin) :
    search_fields=('title','content')
    readonly_fields = ('user','created_at','updated_at')    
    #Hook para coger el user e autoidentificarlo en panel de administracion
    def save_model(self,request,obj,form,change) :
        if not obj.user_id :
            obj.user_id = request.user.id
        obj.save()    
  


admin.site.register(Category,CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
#Configuración extra

   
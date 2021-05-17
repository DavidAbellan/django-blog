from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin) :
  readonly_fields=('updated_at','created_at')
  search_fields=('title','content')


admin.site.register(Page,PageAdmin)


title="Django Blog"
subtitle="Panel de Gestión"





admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle



# Register your models here.

from django.contrib import admin
from .models import Page
admin.site.register(Page)
title="Django Blog"
subtitle="Panel de Gestión"

admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle

# Register your models here.

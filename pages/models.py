from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=70, verbose_name='Título')
    #content = models.TextField(verbose_name='Contenido')
    #Editor de texto enriquecido dentro de panel de admin
    content = RichTextField(verbose_name='Contenido')
     
    #agregar orden a las páginas 
    order = models.IntegerField(default=0,verbose_name="Orden")

    slug= models.CharField(max_length=150, verbose_name='URL',unique=True) 
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at= models.DateField(auto_now_add=True, verbose_name="Creación")
    updated_at= models.DateField(auto_now=True, verbose_name="Actualización")

    class Meta:
        verbose_name="Página"
        verbose_name_plural="Páginas"

    def __str__(self):
        return self.title    



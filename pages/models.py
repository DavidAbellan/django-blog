from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=70, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    slug= models.CharField(max_length=150, verbose_name='URL',unique=True) 
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at= models.DateField(auto_now_add=True, verbose_name="Creación")
    updated_at= models.DateField(auto_now=True, verbose_name="Actualización")

    class Meta:
        verbose_name="Página"
        verbose_name_plural="Páginas"

    def __str__(self):
        return self.title    



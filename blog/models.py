from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(models.Model) :
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at= models.DateField(auto_now_add=True, verbose_name="Creación")
    class Meta :
        verbose_name="Categoría"
        verbose_name_plural="Categorías"
    def __str__(self):
        return self.name


class Article(models.Model) :
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', default='null')
    #Editable = false para que no se pueda cambiar de user en la admin
    user = models.ForeignKey(User, editable=False, verbose_name= "Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías",blank=True)
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at= models.DateField(auto_now_add=True, verbose_name="Creación")
    updated_at= models.DateField(auto_now=True, verbose_name="Actualización")
    class Meta :
        verbose_name="Artículo"
        verbose_name_plural="Artículos"
    def __str__(self):
        return self.title    



# Create your models here.

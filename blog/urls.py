from django.urls import path
from . import views

#por temas de organización lo suyo es que cada app
#tenga su fichero url

urlpatterns = [
    path('articulos/', views.articles, name="lista_articulos")

]

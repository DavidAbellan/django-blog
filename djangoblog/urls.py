"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from mainapp import views 

urlpatterns = [
    path('', views.index, name="inicio"),
    path('admin/', admin.site.urls),
    path('about/', views.about, name= "sobrenosotros" ),
    path('register/', views.register_page, name= "registro" ),
    path('login/', views.login_user, name= "login" ),
    path('logout/', views.logout_user, name= "logout" ),


    path('',include('pages.urls')),
    path('',include('blog.urls'))

]

#Ruta imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

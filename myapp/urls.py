"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from myapp.views import *

urlpatterns = [

    # path('categories',view=category),
    path('', view=index, name='index'),
    path('about/', view=about, name='about'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),


    # path('categories/<slug:catid>/', category, name='category'),
   
    # re_path(r'^archieve/(?P<year>[0-9]{4})/', view=archieve, name='archieve'),
    # path('category/<int:catid>/', view=category),

]

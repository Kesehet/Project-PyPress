"""PyPress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from pyPressApp import views
import image
from pyPressApp.models import *




mList = ['admin/','pyadmin/','pyadmin/edit/<editPageSlug>']
urlpatterns = [
    path(mList[0],admin.site.urls),
    path(mList[1],views.adminIndex),
    path(mList[2],views.adminEditPage),
    path('pyadmin/<appname>',views.adminApps),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

pages = PyPress_Pages.objects.all()
for s in pages:
    urlpatterns += [path(s.slug,views.renderPages)]
    print(s.slug)







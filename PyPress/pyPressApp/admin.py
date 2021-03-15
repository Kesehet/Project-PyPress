from django.contrib import admin
from .models import *


@admin.register(PyPress_Pages)
class PyPress_Pages(admin.ModelAdmin):
    list_display = ["name","head","body","footer","slug"]

@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ["title","text"]
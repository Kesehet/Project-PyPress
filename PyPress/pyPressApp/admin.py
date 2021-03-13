from django.contrib import admin
from .models import PyPress_Pages


@admin.register(PyPress_Pages)
class PyPress_Pages(admin.ModelAdmin):
    list_display = ["name","head","body","footer"]
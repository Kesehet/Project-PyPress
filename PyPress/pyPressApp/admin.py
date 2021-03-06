from django.contrib import admin
from .models import *


@admin.register(PyPress_Pages)
class PyPress_Pages(admin.ModelAdmin):
    list_display = ["name","post","slug"]

@admin.register(Settings)
class Settings(admin.ModelAdmin):
    list_display = ["DefaultPage"]

@admin.register(ThemeVariables)
class ThemeVariables(admin.ModelAdmin):
    list_display = ["VariableName","VariableData"]

@admin.register(ThemeDesign)
class ThemeDesign(admin.ModelAdmin):
    list_display = ["HomePage"]

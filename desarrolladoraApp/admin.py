from django.contrib import admin
from desarrolladoraApp.models import desarrolladora
# Register your models here.
class DesarrolladoraAdmin (admin.ModelAdmin):
    list_display =("nombre","creado")
    search_fields =("nombre",)
    list_filter= ("creado",)
    ordering = ("nombre",)
admin.site.register(desarrolladora, DesarrolladoraAdmin)
from django.contrib import admin
from jugandoApp.models import Juego

# Register your models here.
class JuegoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "desarrolladora", "plataforma", "tipo")
    search_fields = ("nombre", "desarrolladora__nombre")
    list_filter = ("desarrolladora", "plataforma", "tipo")
    ordering = ("nombre",)
admin.site.register(Juego, JuegoAdmin)

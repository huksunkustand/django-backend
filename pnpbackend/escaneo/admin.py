from django.contrib import admin
from escaneo.models import Escaneo

# Register your models here.
@admin.register(Escaneo)
class EscaneoAdmin(admin.ModelAdmin):
    pass

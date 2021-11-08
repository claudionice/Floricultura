from django.contrib import admin
from floricultura.models import Planta,Vaso 

class PlantaAdmin (admin.ModelAdmin):
    list_display = ('id', 'especie', 'nome_cientifico', 'estacao')
    list_display = ('id', 'especie')
    search_fields = ('especie',)
    list_per_page = 20

admin.site.register (Planta, PlantaAdmin)

class VasoAdmin (admin.ModelAdmin):
    list_display = ('id','material', 'tamanho')
    list_display = ('id', 'material')
    search_fields = ('tamanho',)

admin.site.register (Vaso, VasoAdmin)
# Register your models here.

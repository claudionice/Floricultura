from django.contrib import admin
from floricultura.models import plantas. vasos 

class PlantasAdmin (admin.ModelAdmin):
    list_display = ('id', 'especie', 'nome_cientifico', 'estacao')
    list_display = ('id', 'especie')
    search_fields = ('especie',)
    list_per_page = 20

admin.site.register (plantas, PlantasAdmin)

class VasosAdmin (admin.ModelAdmin):
    list_display = ('id','material', 'tamanho')
    list_display = ('id', 'material')
    search_fields = ('tamanho',)

admin.site.register (vasos, VasosAdmin)
# Register your models here.

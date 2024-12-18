from django.contrib import admin
#importantdo o modelo de carros
from cars.models import Car,Brand


class CarAdmin(admin.ModelAdmin):
    #lista os campos que eu tenho na tabela
    list_display = ('model','brand','factory_year',"model_year",'value')
    #campos de busca vai funcionar para buscar modelos
    search_fields = ('model',) 

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)

#modelo e classe configurada
admin.site.register(Car,CarAdmin)

admin.site.register(Brand,BrandAdmin)
from django.contrib import admin


from .models import *




class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'name', 'item')
    search_fields = ['name', 'item']


admin.site.register(Products, ProductAdmin)



admin.site.register(Electronics)
admin.site.register(ElJubilazo)
admin.site.register(Stores)
admin.site.register(Vefase)
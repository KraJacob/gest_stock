from pyexpat import model
from django.contrib import admin

from extrat.models import Agence, Fournisseur, Tva, TypeClient, Unite, Client
from stocks.models import FournisseurProduit

class AgenceAdmin(admin.ModelAdmin):
    fields = ['name', 'city', 'adress', 'phone_number', 'email', 'postal_code','status',]
    list_display = ('name', 'adress', 'city', 'postal_code', 'phone_number', 'email', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    
class FournisseurProduitInline(admin.TabularInline):
    model = FournisseurProduit
    extra = 1    
    
class FournisseurAdmin(admin.ModelAdmin):    
    inlines = [FournisseurProduitInline]   
    fields = ['name','address', 'contact', 'email','status',]
    list_display = ('name', 'address', 'contact', 'email', 'status', 'created_at', 'updated_at')
    search_fields = ('name', 'contact', 'email')
    list_filter = ('name', 'created_at', 'updated_at')
    ordering = ('-created_at',) 
    
class UniteAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'code')    
    
admin.site.register(Agence, AgenceAdmin)

admin.site.register(TypeClient)
admin.site.register(Client)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Tva)

admin.site.register(Unite, UniteAdmin)

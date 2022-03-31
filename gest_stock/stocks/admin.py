from re import search
from django.contrib import admin
from stocks.models import *

class LigneBonRetourInline(admin.TabularInline):
    model = LigneBonRetour
    extra = 1
    
class BonRetourAdmin(admin.ModelAdmin):
    inlines = [LigneBonRetourInline]
    list_display = ('num_bon_retour', 'date_bon_retour', 'agence', 'status')
    list_filter = ('agence', 'status')
    search_fields = ('num_bon_retour', 'date_bon_retour', 'agence', 'status')
    
class LigneBonSortieInline(admin.TabularInline):
    model = LigneBonSortie
    extra = 1
    
class BonSortieAdmin(admin.ModelAdmin):
    inlines = [LigneBonSortieInline]
    list_display = ('num_bon_sortie', 'date_bon_sortie', 'agence', 'status')
    list_filter = ('agence', 'status')
    search_fields = ('num_bon_sortie', 'date_bon_sortie', 'agence', 'status')
    
class LigneBonTransfertInline(admin.TabularInline):
    model = LigneBonTransfert
    extra = 1
    
class BonTransfertAdmin(admin.ModelAdmin):
    inlines = [LigneBonTransfertInline]
    list_display = ('num_bon_transfert', 'date_bon_transfert', 'agence_source', 'agence_destination')
    list_filter = ('agence_source', 'agence_destination')
    search_fields = ('num_bon_transfert', 'date_bon_transfert', 'agence_source', 'agence_destination')      
    
class ProduitUniteInline(admin.TabularInline):
    model = ProduitUnite
    extra = 1
    
class ProduitAdmin(admin.ModelAdmin):
    inlines = [ProduitUniteInline]
    list_display = ('name','description','qte_init','qte_min','qte_max','qte_stock','type_produit')
    list_filter = ('name', 'type_produit')
    search_fields = ('name','description','qte_init','qte_min','qte_max','qte_stock','type_produit')                         
    
admin.site.register(TypeProduit)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(BonRetour, BonRetourAdmin)
admin.site.register(BonSortie, BonSortieAdmin)
admin.site.register(BonTransfert, BonTransfertAdmin)

admin.site.register(FournisseurProduit)
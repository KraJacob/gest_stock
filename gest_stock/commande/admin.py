from django.contrib import admin

from commande.models import BonLivraison, Commande, Facture, LigneBonLivraison, LigneCommande, LigneFacture, TypeCommande, TypeFacture

class LigneBonLivraisonInline(admin.TabularInline):
    model = LigneBonLivraison
    extra = 1
    
class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 1
    
class LigneFactureInline(admin.TabularInline):
    model = LigneFacture
    extra = 1
    
class BonLivraisonAdmin(admin.ModelAdmin):
    inlines = [LigneBonLivraisonInline]
    list_display = ('num_bon_livraison', 'date_bon_livraison', 'client', 'agence','status')
    list_filter = ('client', 'agence', 'status')
    search_fields = ('num_bon_livraison', 'date_bon_livraison', 'client', 'agence', 'type_commande', 'status')
    
class CommandeAdmin(admin.ModelAdmin):
    inlines = [LigneCommandeInline]
    list_display = ('num_commande', 'date_commande', 'client', 'agence', 'type_commande', 'status')
    list_filter = ('client', 'agence', 'type_commande', 'status')
    search_fields = ('num_commande', 'date_commande', 'client', 'agence', 'type_commande', 'status')
    
class FactureAdmin(admin.ModelAdmin):
    inlines = [LigneFactureInline]
    list_display = ('num_facture', 'date_facture', 'client', 'agence', 'type_facture', 'status')
    list_filter = ('client', 'agence', 'type_facture', 'status')
    search_fields = ('num_facture', 'date_facture', 'client', 'agence', 'type_facture', 'status')
    
class LigneBonLivraisonAdmin(admin.ModelAdmin):
    list_display = ('bon_livraison', 'produit', 'qte_commande', 'qte_livree', 'qte_restante')
    list_filter = ('bon_livraison', 'produit')
    search_fields = ('bon_livraison', 'produit')
    
class LigneCommandeAdmin(admin.ModelAdmin):
    list_display = ('commande', 'produit', 'qte_commande', 'qte_livree', 'qte_restante')
    list_filter = ('commande', 'produit')
    search_fields = ('commande', 'produit')
    
class LigneFactureAdmin(admin.ModelAdmin):
    list_display = ('facture', 'produit', 'qte_commande', 'qte_livree', 'qte_restante')
    list_filter = ('facture', 'produit')
    search_fields = ('facture', 'produit')                                           

admin.site.register(Commande, CommandeAdmin)
admin.site.register(TypeFacture)
admin.site.register(Facture, FactureAdmin)
admin.site.register(BonLivraison, BonLivraisonAdmin)
admin.site.register(TypeCommande)

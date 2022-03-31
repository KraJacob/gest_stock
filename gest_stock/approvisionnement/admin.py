from asyncore import read
from dataclasses import field
from django.contrib import admin
from approvisionnement.models import Approvisionnement, BonDeReception, LigneApprovisionnement, LigneBonDeReception

class LigneApprovisionnementInline(admin.TabularInline):
    readonly_fields = ('prix_total',)
    fields = ('produit', 'unite', 'quantite', 'prix_unitaire', 'prix_total')
    model = LigneApprovisionnement
    extra = 1
    
    def prix_total(self, obj):
        if obj.prix_unitaire:
            return obj.prix_unitaire * obj.quantite
        else:
            return '-'
        
    class Meta:
        js = ('static/js/approvisionnement.js',)
        
    
class ApprovisionnementAdmin(admin.ModelAdmin):
    inlines = [LigneApprovisionnementInline]
    list_display = ('num_approvisionnement', 'date_approvisionnement', 'agence', 'status')
    list_filter = ('agence', 'status')
    search_fields = ('num_approvisionnement', 'date_approvisionnement', 'agence', 'status')
    
    class Meta:
        js = ('js/approvisionnement.js',)
        
class LigneBonDeReceptionIline(admin.TabularInline):
    model = LigneBonDeReception
    extra = 1        
    
class BonDeReceptionAdmin(admin.ModelAdmin):
    inlines = [LigneBonDeReceptionIline]
    list_display = ('num_bon_reception', 'date_bon_reception', 'agence', 'status')
    list_filter = ('agence', 'status')
    search_fields = ('num_bon_reception', 'date_bon_reception', 'agence', 'status')
    
admin.site.register(Approvisionnement, ApprovisionnementAdmin)
admin.site.register(BonDeReception, BonDeReceptionAdmin)   
admin.site.site_header = 'Gestion des approvisionnements'     

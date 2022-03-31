from django.db import models

from extrat.models import Agence, Fournisseur, Tva, Unite
from stocks.models import Produit

class Approvisionnement(models.Model):
    num_approvisionnement = models.CharField(max_length=50, unique=True)
    date_approvisionnement = models.DateField()
    date_reception = models.DateField()
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    tva = models.ForeignKey(Tva, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date_approvisionnement)
    
class LigneApprovisionnement(models.Model):
    approvisionnement = models.ForeignKey(Approvisionnement, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    
    def __str__(self):
        return str(self.quantite)
    
class BonDeReception(models.Model):
    num_bon_reception = models.CharField(max_length=50, unique=True)
    date_bon_reception = models.DateField()
    approvisionnement = models.ForeignKey(Approvisionnement, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    tva = models.ForeignKey(Tva, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date_bon_reception)   
    
class LigneBonDeReception(models.Model):
    bon_de_reception = models.ForeignKey(BonDeReception, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    qte_commandee = models.IntegerField()
    qte_recue = models.IntegerField()
    qte_restante = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.bon_de_reception)         

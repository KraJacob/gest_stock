from django.db import models
from extrat.models import Unite
from stocks.models import Agence,Client,Produit

class TypeCommande(models.Model):
    libelle = models.CharField(max_length=50)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.libelle
    
class Commande(models.Model):
    num_commande = models.CharField(max_length=50, default='')
    date_commande = models.DateField()
    date_livraison = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    type_commande = models.ForeignKey(TypeCommande, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_commande)   
    
class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    qte_commande = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    prix_unitaire =models.IntegerField(default=0)
    prix_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def prix_total_commande(self):
        return self.qte_commande * self.prix_unitaire
    
    
    def __str__(self):
        return str(self.commande)   
    
class TypeFacture(models.Model):
    libelle = models.CharField(max_length=50)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.libelle
    
class Facture(models.Model):
    num_facture = models.CharField(max_length=50, default='')
    date_facture = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    type_facture = models.ForeignKey(TypeFacture, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_facture)
    
class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte_facture = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.facture)
    
class BonLivraison(models.Model):
    num_bon_livraison = models.CharField(max_length=50, default='')
    date_bon_livraison = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_livraison)
    
class LigneBonLivraison(models.Model):
    bon_livraison = models.ForeignKey(BonLivraison, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    prix_unitaire = models.IntegerField(default=0)
    qte_bon_livraison = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    prix_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_livraison)
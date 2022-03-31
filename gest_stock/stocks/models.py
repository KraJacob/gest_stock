from django.db import models

from extrat.models import Agence, Client, Fournisseur, Unite

    
class TypeProduit(models.Model):
    libelle = models.CharField(max_length=50)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.libelle
    
class Produit(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    qte_init =models.IntegerField(default=0)
    qte_min =models.IntegerField(default=0)
    qte_max =models.IntegerField(default=0)
    qte_stock =models.IntegerField(default=0)
    type_produit = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name    
    
class BonRetour(models.Model):
    num_bon_retour = models.CharField(max_length=50, default='')
    date_bon_retour = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_retour)
    
class LigneBonRetour(models.Model):
    bon_retour = models.ForeignKey(BonRetour, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    qte_bon_retour = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_retour)
    
class BonSortie(models.Model):
    num_bon_sortie = models.CharField(max_length=50, default='')
    date_bon_sortie = models.DateField()
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_sortie)
    
class LigneBonSortie(models.Model):
    bon_sortie = models.ForeignKey(BonSortie, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    qte_bon_sortie = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_sortie)
    
class BonTransfert(models.Model):
    num_bon_transfert = models.CharField(max_length=50, default='')
    date_bon_transfert = models.DateField()
    agence_source = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='t_agence_source')
    agence_destination = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='t_agence_destination')
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_transfert)
    
class LigneBonTransfert(models.Model):
    bon_transfert = models.ForeignKey(BonTransfert, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE) 
    qte_bon_transfert = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_transfert)
    
class BonTransfertInterne(models.Model):
    num_bon_transfert_interne = models.CharField(max_length=50, default='')
    date_preparation = models.DateField()
    date_bon_transfert_interne = models.DateField()
    agence_source = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='int_agence_source')
    agence_destination = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='int_agence_destination')
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_transfert_interne)
    
class LigneBonTransfert_Interne(models.Model):
    bon_transfert_interne = models.ForeignKey(BonTransfertInterne, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE) 
    qte_bon_transfert_interne = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_transfert_interne)
    
class BonTransfertExterne(models.Model):
    num_bon_transfert_externe = models.CharField(max_length=50, default='')
    date_bon_transfert_externe = models.DateField()
    agence_source = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='ext_agence_source')
    agence_destination = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='ext_agence_destination')
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_transfert_externe)
    
class LigneBonTransfertExterne(models.Model):
    bon_transfert_externe = models.ForeignKey(BonTransfertExterne, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE) 
    qte_bon_transfert_externe = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_transfert_externe)
    
class BonTransfertInterneExterne(models.Model):
    num_bon_transfert_interne_externe = models.CharField(max_length=50, default='')
    date_bon_transfert_interne_externe = models.DateField()
    agence_source = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='source')
    agence_destination = models.ForeignKey(Agence, on_delete=models.CASCADE, related_name='destination')
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.num_bon_transfert_interne_externe)
    
class LigneBonTransfertInterne_Externe(models.Model):
    bon_transfert_interne_externe = models.ForeignKey(BonTransfertInterneExterne, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE) 
    qte_bon_transfert_interne_externe = models.IntegerField(default=0)
    qte_livree = models.IntegerField(default=0)
    qte_restante = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.bon_transfert_interne_externe)
    
class FournisseurProduit(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix_unitaire = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.fournisseur) + ' ' + str(self.produit)  
    
class ProduitUnite(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    unite = models.ForeignKey(Unite, on_delete=models.CASCADE)
    prix_unitaire = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.produit)  + ' ' + str(self.unite)    

       

                       
                                                                                                                                                  
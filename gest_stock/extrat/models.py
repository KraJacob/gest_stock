from django.db import models


class Agence(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name

class Tva(models.Model):
    taux = models.IntegerField(default=0)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.taux)  
    
    class Meta:
        verbose_name = 'Tva'
        verbose_name_plural = 'Tva' 
    
    
class Fournisseur(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Fournisseur'
        verbose_name_plural = 'Fournisseurs'
    
    
class Unite(models.Model):
    libelle = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.libelle
       
class Soclivraison(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    
    def __str__(self):
        return self.name  
    
class Livreur(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default='', blank=True)
    Soc_livraison = models.ForeignKey(Soclivraison, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    
    def __str__(self):
        return self.name      


class TypeClient(models.Model):
    libelle = models.CharField(max_length=50)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('active', 'active'), ('inactive', 'inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.libelle    
    

class Client(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=25)
    address = models.CharField(max_length=50, default='')
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    type_client =models.ForeignKey(TypeClient, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    
    def __str__(self):
        return self.name              
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Personne(models.Model):
    SEX_TYPE = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length = 15)
    sexe = models.CharField(max_length=1, choices=SEX_TYPE)
    birthdate = models.DateField()
    address = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"
        abstract = True

    def __str__(self):
        return self.name


class Proprio(Personne):
    id_proprio = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.name + " " + self.surname 


class Agenceimo(models.Model):
    id_agence = models.BigAutoField(primary_key=True)
    agency_name = models.CharField(max_length=20)
    background_image = models.ImageField()
    profile_image = models.ImageField()
    description = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    proprio= models.ForeignKey(Proprio, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Agenceimo"
        verbose_name_plural = "Agenceimos"

    def __str__(self):
        return self.agency_name + " " + self.background_image + " " + self.profile_image + " " + self.description + " " + self.date_created
    
class Contratelectronique(models.Model):
    id_contrat = models.BigAutoField(primary_key=True)
    nom_vendeur = models.CharField(max_length=25)
    nom_prenant = models.CharField(max_length=25)
    proprio= models.ForeignKey(Proprio, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Contratelectronique"
        verbose_name_plural = "Contratelectroniques"

    def __str__(self):
        return self.nom_vendeur + " " + self.nom_prenant
    
class Reclamation(models.Model):
    id_contrat = models.BigAutoField(primary_key=True)


class Pay(models.Model):
    id_pay = models.BigAutoField(primary_key=True)
    montant = models.IntegerField(null=True)
    contratelectronique = models.ForeignKey(Contratelectronique, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "pay"
        verbose_name_plural = "payers"

    def __str__(self):
        return self.montant
    
class Conditionlocation(models.Model):
    id_locate = models.BigAutoField(primary_key=True)

    TYPE_LOCATE = (
        ('P', 'Pièce'),
        ('CS', 'Chambre + Salon'),
        ('V', 'Villa'),
        ('ME', 'Maison entière'),
    )

    TYPE_CONTRUCTION = (
        ('E', 'Embanco'),
        ('SD', 'Semi-dure'),
        ('ED', 'Endure'),
    )

    TYPE_SANITAIRE = (
        ('WDI', 'WC-DOUCHE-INTERNE'),
        ('WDE', 'WC-DOUCHE-EXTERNE'),
    )

    TYPE_SOURCE_EAU = (
        ('PUI', 'PUIT-INTERNE'),
        ('PUE', 'PUIT-EXTERNE'),

        ('POI', 'Pompe-interne'),
        ('POE', 'Pompe-externe'),
    )


    type_location = models.CharField(max_length=2, choices=TYPE_LOCATE)
    type_construction = models.CharField(max_length=2, choices=TYPE_CONTRUCTION)
    type_sanitaire = models.CharField(max_length=3, choices=TYPE_SANITAIRE)
    type_source_eau = models.CharField(max_length=3, choices=TYPE_SOURCE_EAU)


    
    class Meta:
        verbose_name ="Conditionlocation"
        verbose_name_plural = "Conditionlocations"

    def __str__(self):
        return self.type_location + " " + self.type_construction + " " + self.type_sanitaire + " " + self.type_source_eau



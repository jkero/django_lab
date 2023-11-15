from django.db import models

# Create your models here.
from django.db import models


class Plante(models.Model):
    plante_texte = models.CharField(max_length=200)
    plante_ec_min = models.DecimalField(max_digits=2, decimal_places=2)
    plante_ec_max = models.DecimalField(max_digits=2, decimal_places=2)
    plante_ph_min = models.DecimalField(max_digits=2, decimal_places=2)
    plante_ph_max = models.DecimalField(max_digits=2, decimal_places=2)
    plante_prod = models.CharField(max_length=200)



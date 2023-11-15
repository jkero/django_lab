from django.db import models

# Create your models here.
from django.db import models


class Plante(models.Model):
    plante_texte = models.CharField(max_length=200)
    plante_ec_min = value = models.DecimalField(max_digits=2, decimal_places=2)
    plante_ec_max = value = models.DecimalField(max_digits=2, decimal_places=2)
    plante_ph_min = value = models.DecimalField(max_digits=2, decimal_places=2)
    plante_ph_max = value = models.DecimalField(max_digits=2, decimal_places=2)


class PlanteVar(models.Model):
    planteprinc = models.ForeignKey(Plante, on_delete=models.CASCADE)
    plantevar_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

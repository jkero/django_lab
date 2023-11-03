from django.db import models

# Create your models here.

class LeParam1(models.Model):
    param_nom = models.CharField(max_length=200)
    param_date = models.DateTimeField("publication")

    def __str__(self):
        return self.param_nom
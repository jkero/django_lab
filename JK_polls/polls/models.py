import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    tot_votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?")
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def to_be_published(self):
        now = timezone.now()
        return self.pub_date > now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text

"""
TODO: modèle pour retourner q + c + % par réponse (vote par c/sum votes par q)
"""
# ItemPrice.objects.aggregate(Sum('price'))
# class Stats(models.Model):
#     dico = {}
#     def
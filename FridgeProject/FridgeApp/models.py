from django.db import models
from django import forms

# Create your models here.
class Aliments(models.Model):
    name = models.CharField(max_length = 500, unique= True)

    def __str__(self) -> str:
        return self.name

        
class Recettes(models.Model):
    name = models.CharField(max_length = 75)
    howToCook = models.URLField()
    picture = models.URLField()
    aliments = models.ManyToManyField(Aliments, related_name="recettes", blank= True)

    def __str__(self) -> str:
        return self.name
    
       
class NameForm(forms.Form):
    Choisissez = forms.CharField(label='Choisissez') 


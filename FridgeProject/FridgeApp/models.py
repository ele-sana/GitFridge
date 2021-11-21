from django.db import models

# Create your models here.
class Aliments(models.Model):
    name = models.CharField(max_length = 500)

    def __str__(self) -> str:
        return self.name

        
class Recettes(models.Model):
    name = models.CharField(max_length = 75)
    howToCook = models.URLField()
    picture = models.URLField()

    def __str__(self) -> str:
        return self.name
    
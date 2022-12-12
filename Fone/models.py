from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Fone(models.Model):
    carName = models.CharField(max_length=255, default="Car Name")
    carModel = models.CharField(max_length=255, default="Car Model")
    carFactory = models.CharField(max_length=255, default="Factory")
    driver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ratingDriver = models.IntegerField()
    trophyDriver = models.IntegerField()
    founder = models.CharField(max_length=256, default="Founder")

    def __str__(self):
        return self.carName

    def get_absolute_url(self):
        return reverse("Fone-list")

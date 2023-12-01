from django.db import models
from django.contrib.auth.models import *

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    yoshi = models.PositiveIntegerField()
    kasb = models.CharField(max_length=44)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    mavzu = models.CharField(max_length=80)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.muallif.ism}ning maqolasi"

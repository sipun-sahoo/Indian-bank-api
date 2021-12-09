
from django.db import models

# Create your models here.
class Indianbank(models.Model):
 bankname = models.CharField(max_length=50)
 accno = models.IntegerField()
 ifsccode = models.CharField(max_length=50)
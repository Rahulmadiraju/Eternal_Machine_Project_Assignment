from django.db import models

# Create your models here.
class MachineValue(models.Model):
    machine_id = models.IntegerField()
    axis = models.CharField(max_length=1)
    value = models.FloatField()

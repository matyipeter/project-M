from django.db import models

# Create your models here.


class Appointment(models.Model):
    tipus = models.CharField(max_length=100)
    honap = models.CharField(max_length=100)
    nap = models.IntegerField()
    idopont = models.TimeField()
    free = True

    def reserve(self):
        self.free = False

    def __str__(self):
        return self.honap
        
    
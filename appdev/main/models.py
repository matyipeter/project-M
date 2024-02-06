from django.db import models

# Create your models here.


class Appointment(models.Model):
    honap = models.CharField(max_length=100)
    nap = models.IntegerField()
    idopont = models.TimeField()
    free = models.BooleanField(default=True)

    # FOREIGN KEY

    def reserve(self):
        self.free = False

    def __str__(self):
        return self.honap
        

# class Customer(models.Model)
    
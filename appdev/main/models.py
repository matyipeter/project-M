from django.db import models

# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    honap = models.CharField(max_length=100)
    nap = models.IntegerField()
    nap_neve = models.CharField(max_length=20, default="hetfo")
    idopont = models.TimeField()
    free = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def reserve(self):
        self.free = False

    def __str__(self):
        return self.honap
    
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    filenev = models.CharField(max_length=50, default="macska.jpg")
        


    


    
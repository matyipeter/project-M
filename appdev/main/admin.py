from django.contrib import admin
from .models import Appointment, Customer, Service, Message

# Register your models here.
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(Service)
admin.site.register(Message)

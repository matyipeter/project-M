from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Appointment

# Create your views here.

def index(request):
    return render(request, "main/index.html")


class Idopont(View):
    def get(self, request):
        return render(request, 'main/appointment.html', {"tipus":""})

    def post(self, request):
        value = request.POST["dropdown"]
        print(value)
        return redirect(reverse("main:foglalas2", kwargs={"tipus":str(value)}))
    
class Idopont2(View):
    def get(self, request, tipus):
        obj_list = Appointment.objects.filter(tipus=tipus)
        honapok = set([i.honap for i in obj_list])
        return render(request, 'main/appointment.html', {"tipus":tipus, "honapok":honapok})
    
    def post(self, request, tipus):
        value = request.POST["honap"]
        print(value)
        return redirect(reverse("main:foglalas3", kwargs={"honap":value, "tipus":tipus}))

class Idopont3(View):
    def get(self, request, tipus, honap):
        napok = Appointment.objects.filter(tipus=tipus, honap=honap)
        days = set([i.nap for i in napok])
        return render(request, 'main/book.html', {"tipus":tipus,"honap":honap, "days":days})

class Idopont4(View):
    def get(self, request, tipus, honap, nap):
        obj_list = Appointment.objects.filter(tipus=tipus, honap=honap, nap=nap)
        idopontok = [i.idopont for i in obj_list]
        idopontok.sort()

        return render(request, 'main/book2.html', {"idopontok":idopontok})



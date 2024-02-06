from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView
from datetime import datetime

from .models import Appointment

# Create your views here.

def index(request):
    return render(request, "main/index.html")


class Idopontok(ListView):

    template_name = "main/appointment.html"
    honapok = ["Január", "Február", "Március", "Április", "Május", "Június"]
    current_month = honapok[(datetime.now().month)-1]
    queryset = Appointment.objects.filter(free=True, honap=current_month).values("nap").distinct()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["month"] = self.current_month
        return context

class Idopontok2(View):

    def get(self, request, honap, nap):
        queryset = Appointment.objects.filter(free=True, honap=honap, nap=nap)
        appo = [i.idopont.strftime("%H:%M") for i in queryset]
        appo.sort()
        return render(request, "main/appointment2.html", {"object_list":appo, "honap":honap, "nap":nap})
    
class Reserve(View):

    def get(self, request, honap, nap, idopont):
        template = "main/book.html"
        return render(request, template, {"honap":honap,"nap":nap,"idopont":idopont})
    
    def post(self, request, honap, nap, idopont):
        appo = Appointment.objects.get(honap=honap, nap=nap, idopont=idopont)
        appo.reserve()
        appo.save()
        return redirect("main:index")
        


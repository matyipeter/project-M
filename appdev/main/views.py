from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, ListView
from datetime import datetime
from django.http import HttpResponseRedirect

from .models import Appointment, Customer, Service, Message
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.

class Index(ListView):
    template_name = "main/index.html"
    queryset = Service.objects.all()


class Idopontok(ListView):

    template_name = "main/appointment.html"
    honapok = ["Január", "Február", "Március", "Április", "Május", "Június"]
    napok = ["Hétfő"]
    current_month = honapok[(datetime.now().month)-1]
    queryset = Appointment.objects.filter(free=True, honap=current_month).values("nap").distinct().order_by("nap")


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
        full_name = request.POST["full_name"]
        email= request.POST["email"]

        form = Customer(full_name=full_name, email=email)
        form.save()

        message = render_to_string("main/email_temp.html", {
            "name":full_name,
            "honap":honap,
            "nap":nap,
            "idopont":idopont,
            'protocol': 'https' if request.is_secure() else 'http',
        })

        n_email = EmailMessage("foglalás", message, to=[email])
        n_email.content_subtype = "html"

        if n_email.send():
            print('Successful email sending')
        else:
            print('FAIL')
            return redirect("main:error")

        appo = Appointment.objects.get(honap=honap, nap=nap, idopont=idopont)
        appo.customer = form
        appo.reserve()
        appo.save()
        return HttpResponseRedirect(reverse("main:thanks"))
    

class Uzenet(View):

    def post(self, request):
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["uzenet"]

        new = Message(name=name, email=email, message=message)
        new.save()
        return redirect("main:thanks")


class Error(TemplateView):
    template_name = "main/error.html"

class Test(TemplateView):
    template_name = "main/test.html"

class Thanks(TemplateView):
    template_name = "main/thanks.html"
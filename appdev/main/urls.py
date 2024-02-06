from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("foglalas/", views.Idopontok.as_view(), name="foglalas"),
    path("foglalas/<str:honap>/<int:nap>", views.Idopontok2.as_view(), name="foglalas2"),
    path("foglalas/<str:honap>/<int:nap>/<str:idopont>", views.Reserve.as_view(), name="reserve")
]

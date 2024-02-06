from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("foglalas/", views.Idopont.as_view(), name="foglalas"),
    path("foglalas/<str:tipus>", views.Idopont2.as_view(), name="foglalas2"),
    path("foglalas/<str:tipus>/<str:honap>", views.Idopont3.as_view(), name="foglalas3"),
    path("foglalas/<str:tipus>/<str:honap>/<int:nap>", views.Idopont4.as_view(), name='foglalas4'),
]

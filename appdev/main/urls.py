from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("foglalas/", views.Idopontok.as_view(), name="foglalas"),
    path("foglalas/<str:honap>/<int:nap>", views.Idopontok2.as_view(), name="foglalas2"),
    path("foglalas/<str:honap>/<int:nap>/<str:idopont>", views.Reserve.as_view(), name="reserve"),
    path("error/", views.Error.as_view(), name="error"),
    path("test/", views.Test.as_view(), name="test"),
]

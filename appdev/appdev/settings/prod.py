from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://visblearning.store']
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "project2",
        "USER": "root",
        "PASSWORD": "Macskalaci22",
        "HOST": "localhost",
        "PORT": ""
    }
}
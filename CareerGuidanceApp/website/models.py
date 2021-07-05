from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User)
    email=models.EmailField(null=True)
    phone=models.BigIntegerField()
    
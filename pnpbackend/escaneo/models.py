from unittest.util import _MAX_LENGTH
import django.utils.timezone
from django.db import models

# Create your models here.
class Escaneo(models.Model):
    name = models.CharField(max_length=150 , default=None)
    academic_training = models.CharField(max_length=150, default= None)
    place_residence = models.CharField(max_length=250, default= None)
    residence_address = models.CharField(max_length=250, default= None)
    observation = models.CharField(max_length=500 , default=None)
    user_creation = models.CharField(max_length=100, default=None)
    date_creation = models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_user')
    user_modify = models.CharField(max_length=100)
    date_modify = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_modify')




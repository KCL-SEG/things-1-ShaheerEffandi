from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db.models import Model
# Create your models here.

class Thing(Model):
    name = models.CharField(max_length=30,
     unique=True,
     blank=False,
     )
    description = models.TextField(unique=False, max_length=120, blank=True)
    quantity = models.IntegerField(
    validators = [
    MaxLengthValidator(100, message='Must be less than 100'),
    MinLengthValidator(0, message='Must be more than 0'),
    ]
    )

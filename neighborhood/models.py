from django.db import models
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    person_id = models.CharField(max_length=200)
    id_card = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    status = models.CharField(max_length=4)
    created_at = models.DateTimeField(default=timezone.now)

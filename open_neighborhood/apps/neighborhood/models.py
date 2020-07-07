from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    id_card = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    birth = models.DateField()
    status = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
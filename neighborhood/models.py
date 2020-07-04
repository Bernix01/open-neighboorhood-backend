from django.db import models
from django.utils import timezone


# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    id_card = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    birth = models.DateField()
    status = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + self.second_name


class Block(models.Model):
    block_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    block_id = models.ForeignKey('Block', on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.house_id


class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
    )
    house_id = models.ForeignKey(
        'House',
        on_delete=models.CASCADE,
    )
    landlord = models.BooleanField()

    def __str__(self):
        return self.person_id



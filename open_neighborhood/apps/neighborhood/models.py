from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    id_card = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    birth = models.DateField()
    status = models.BooleanField()
    email = models.CharField(max_length=100,null=False , default='user@user.com' )
    password = models.CharField(max_length=12,null=False, default= '')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Block(models.Model):
    block_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.block_id


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    block_id = models.ForeignKey('Block', on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.house_id


class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person',on_delete=models.CASCADE,)
    house_id = models.ForeignKey('House',on_delete=models.CASCADE,)
    landlord = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.resident_id

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey('Person',on_delete=models.CASCADE,)
    phone = models.CharField(max_length=10)
    home_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.employee_id
    
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role_id

class Role_employee(models.Model):
    re_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey('Employee',on_delete=models.CASCADE,)
    role_id = models.ForeignKey('Role',on_delete=models.CASCADE,)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.re_id



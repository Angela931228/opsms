from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category= models.CharField(max_length=200)
    code   = models.CharField(max_length=200)
    status   = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.product_name

class Staff(models.Model):
    staff_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    number   = models.CharField(max_length=200)
    address   = models.CharField(max_length=200)
    email   = models.CharField(max_length=200)
    phone_number  = models.IntegerField(default=0)
    staff_salary = models.IntegerField(default=0)
    def __str__(self):
        return self.staff_name

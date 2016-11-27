from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category= models.CharField(max_length=200)
    code   = models.CharField(max_length=200)
    status   = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    expiry_date = models.DateField(default=datetime.now, blank=True)
    discount_rate = models.FloatField(default=1.0)
    markdown = models.IntegerField(default=1)
    def __str__(self):
        return self.product_name
    def _get_total(self):
       "Returns the total"
       return self.price * self.discount_rate
    current_price = property(_get_total)

class Promo_event(models.Model):
    name = models.CharField(max_length=200)
    event_type= models.CharField(max_length=200)
    start_date   = models.DateField(default=datetime.now, blank=True)
    end_date   = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
class DiscoutingTable(models.Model):
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    promo_event_id= models.ForeignKey(
        'Promo_event',
        on_delete=models.CASCADE,
    )
    discount_rate= models.FloatField(default=1.0)
    start_date   = models.DateField(default=datetime.now, blank=True)
    end_date   = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.product_id.product_name 

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

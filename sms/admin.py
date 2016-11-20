from django.contrib import admin

# Register your models here.
from .models import Product,Staff

admin.site.register(Product)
admin.site.register(Staff)
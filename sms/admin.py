from django.contrib import admin

# Register your models here.
from .models import Product,Staff,Promo_event,DiscoutingTable

admin.site.register(Product)
admin.site.register(Staff)
admin.site.register(Promo_event)
admin.site.register(DiscoutingTable)
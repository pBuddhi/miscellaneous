from django.contrib import admin
from .models import RoomRate,Supplier,RateOfExchange,SailingDate

# Register your models here.
mymodels = [RoomRate,Supplier,RateOfExchange,SailingDate]
admin.site.register(mymodels)


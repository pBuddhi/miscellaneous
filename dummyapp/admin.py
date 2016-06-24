from django.contrib import admin
from .models import *
# Register your models here.
mymodels = [Booking,Region,Country,Destination,Search,Accommodation,Room,Package,Inclusion,RateOfExchange,AirportCode,PackageQuote,AirportCodesImport]
admin.site.register(mymodels)

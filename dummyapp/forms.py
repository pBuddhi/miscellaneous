from django import forms
from .models import Search,Booking,AirportCodesImport

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['query','checkin','checkout','duration']

class BookingForm( forms.ModelForm ):
	class Meta:
		model = Booking
		fields = '__all__'

from data_importer.importers import XLSImporter
class MyXLSImporterModel(XLSImporter):
	class Meta:
		model = AirportCodesImport
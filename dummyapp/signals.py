from django.dispatch import Signal
#from django.core.signals import request_started
from .models import Search
#from django.utils.dateparse import parse_date
def  meth(sender,form,**kwargs):
	print form
	print type(form)
	print sender
	print "hello"
	print form.__dict__
	#print kwargs
	#query = form.query
	#checkin = form.checkout
	#print type(checkin)
	#checkout = form.checkout
	query = form.cleaned_data["query"]
	checkin = form.cleaned_data["checkin"]
	checkout = form.cleaned_data["checkout"]
	duration = abs((checkout-checkin).days)

	#duration = 5
	obj = Search(query=query,checkin=checkin,checkout=checkout,duration=duration)
	obj.save()
	return "hello"
my_signal = Signal(providing_args=["form"])
# request_started.connect(meth)
my_signal.connect(meth)

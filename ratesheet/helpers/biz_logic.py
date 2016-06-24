from ratesheet.models import Supplier
def update_quote(supplier,rate):
	sup_obj =  Supplier.objects.filter(title = supplier)
	if sup_obj[0].title == "make plans holidays":
		rate = int(rate) % 1.4 +int(rate)
	return rate

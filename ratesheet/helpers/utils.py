from django.db.models import Q
from ratesheet.models import RoomRate,RateOfExchange,SailingDate

def rate_of_exchange(native_currency,amount):
	roe_object = RateOfExchange.objects.filter(title=native_currency).latest('timestamp')
	print roe_object.rate_of_exchange
	return int(roe_object.rate_of_exchange) * int(amount)


def get_hotel_quote(room_rate_hash,check_in,check_out,duration):
	total_rooms = RoomRate.objects.filter( Q(title = room_rate_hash ) & Q(valid_from__lte = check_in) & Q(valid_until__gte=check_in))
	hotel_rooms = total_rooms.filter( is_cruise=False)
	
	sailing_date_obj = SailingDate.objects.filter( sailing_date = check_in )
	print sailing_date_obj[0]
	available_cruise_rooms = sailing_date_obj[0].roomrate_set.filter( title = room_rate_hash )
	print available_cruise_rooms


	rate = available_cruise_rooms[0].rate_per_person
	tax = available_cruise_rooms[0].rate_currency
	inclusion = available_cruise_rooms[0].inclusion
	from ratesheet.helpers.biz_logic import update_quote
	rate = update_quote(available_cruise_rooms[0].supplier,rate)
	currency = available_cruise_rooms[0].rate_currency
	if not ( currency == "INR" ):
		rate_in_inr = rate_of_exchange( currency,rate )
	else:
		rate_in_inr = rate
	hotel_quote = {'rate_in_inr':rate_in_inr,'inclusion':inclusion}
	return hotel_quote





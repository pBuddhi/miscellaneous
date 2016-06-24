from django.shortcuts import render,redirect
from .models import Package,Destination,AirportCode,PackageQuote
from django.http import HttpResponse
import logging
import json
import re
from signals import my_signal
from .forms import *
from  django.views.decorators.cache import cache_page
from django.core.signals import request_started
from django.core.cache import cache
from dummyapp.helpers.utils import caching_view,render_to_pdf
from urllib import urlencode
import urllib2
import urllib
import requests
from django.template import Context
from coupons.models import *
# Create your views here.

def firstview(request):
	# if request.method == 'POST':
	# 	return render('secondview')
	# pkgs = Package.objects.all()
	# for i in range(0,len(pkgs)):
	# 	print pkgs[i]
	return render(request,"first.html")


def secondview(request):
	#request_started.send(sender="meh")
	if request.method == "POST":
		form = SearchForm( request.POST )
		print "afsdf"
		my_signal.send(sender="me",form=form)
		# if not form.is_valid():
		# 	return firstview( request )
		return render(request,"second.html")

def logging_view(request):
	if not request.session.exists(request.session.session_key):
		request.session.create()
	logger = logging.getLogger("loggly_logs")
	sr = "(%s:%s)" % ("key",request.session.session_key )
	logger.error('Something went wrong!')
	logger.info(sr)
	try:
		return render(request,"logging.htm")
	except Exception,e:
		logger.exception(e)
		return render(request,"logging1.html")
	return render(request,"logging.html")

def logglykey(request):
	logglykey = request.POST.get("logglykey","")
	request.session["logglykey"] = logglykey
	print request.session["logglykey"]
	dic = {"result":"hello"}
	return HttpResponse(
            json.dumps(dic),
            content_type="application/json"
        )

def search(request):
	print "asd"
	if request.method == 'POST':
		print "sad"
		search_form = SearchForm( request.POST )
		# if search_form.is_valid():
		# 	print "ASDfa"
		query = search_form.data['search']
		check_in = search_form.data['checkin']
		check_out = search_form.data['checkout']
		#from urllib import urlencode
		query_string = urlencode({'query':query,'check_in':check_in,'check_out':check_out})
		print query_string
			#destination = Destination.objects.filter(title = query )
			#packages = Package.objects.filter(destination = destination )
		return redirect('/search-result?'+query_string)
		#else:
		#render(request,"search.html")
	 
	return render(request,"search.html")

#@cache_page(60)
def search_result( request ):
	# string = request.GET.urlencode()
	# #print string
	# cache_key = "search_result_cache"+string
	# print cache_key
	# results = cache.get(cache_key)
	# if not results:

	# 	print "view veiw"
	# 	airports = AirportCode.objects.all()
	# 	print airports
	# 	query = request.GET.get('query','')
	# 	check_in = request.GET.get('check_in','')
	# 	check_out = request.GET.get('check_out','')
	# 	print type(request.GET.get('check_in',''))
	# 	#return render(request,"search.html")

	# 	# query = request.POST.get('search','')
	# 	# check_in = request.POST.get('checkin','')
	# 	# check_out = request.POST.get('checkout','')
	# 	des = Destination.objects.filter(title = query )
	# 	packages = Package.objects.filter(destination = des )
	# 	package = packages.latest('id')
	# 	print package.hash_1
	# 	print packages
	# 	# for package in packages:
	# 	# 	package_quote = Package.get_quote( package,check_in,check_out )
	# 	# 	print package_quote
	# 	# 	print package.slug
	# 	results =  render(request,"search_result.html",{"package":package,"id":package.id,"destination" : package.destination.title})
	# 	cache.set(cache_key,results,60)
	# return results
	caching_view(request)
	return render(request,"search.html")

def package_detail( request,slug1,slug2,hash_1,package_id ):
	package = Package.objects.get(pk=package_id)
	print package
	print package.slug1
	print package.slug2

	return render(request,'package_detail.html')

def formatter( request ):
	return render( request , 'formatter.html' )

def formatter_result( request ):
	print "formatter called"
	query = request.POST.get("query","")
	words = query.split("RTSVC")
	words_new = []
	for word in words[:-1]:
		word = word.strip()
		word = word.split("  E  0")[0]
		#word = re.sub("\\*","",word)
		word = word[3:10]+word[12:18]+word[20:23]+u" to "+word[23:27]+word[32:]
		airport = AirportCode.objects.get(code=word[13:16])
		word = re.sub(word[13:16],airport.airport_name+"("+word[13:16]+")",word)

		print word[-20:-17]
		airport = AirportCode.objects.get(code=word[-20:-17])
		word = re.sub(word[-20:-17],airport.airport_name+"("+word[-20:-17]+")",word)
		#word_new = re.sub(" ","    ",word)
		#word = re.sub("....to...."," to ",word)
		#word_new = re.sub("...."," ",word)
		#print codes
		words_new.append(word)

		
	print words_new
	# words_new_1 = []
	# for word in words_new:
	# 	word = word[3:10]+word[12:18]+word[19:22]+u" - "+word[22:26]+word[29:]
	# 	words_new_1.append(word)
	# print words_new_1
	# print words_new_1[:-1]
	return render( request, "formatter_result.html",	 {"words":words_new})

# def airport_codes( request ):
# 	query = request.POST.get("query","")
# 	words = query.split("\n")
# 	for word in words:
# 		q = AirportCodesNew(title=word[:-4],code=word[-4:])
# 		q.save()
# 	return render( request, "formatter_result.html",{ "words": words })

def airport_codes( request ):
	# query = request.POST.get("query","")
	# words = query.split("\n")
	# for word in words:
	# 	q = AirportCodesNew(title=word[:-4],code=word[-4:])
	# 	q.save()

	mylist = MyXLSImporterModel(source="/home/buddhi/Downloads/airport-codes.xls")
	mylist = mylist.cleaned_data
	for i,val in enumerate(mylist):
		row_no,data = mylist[i]
		obj = AirportCode()
		obj.airport_name = data['airport_name']
		obj.code = data['airport_code']
		obj.title = obj.airport_name + obj.code
		obj.save()
	words = AirportCode.objects.all()
	return render( request, "formatter_result.html",{ "words": words })


# def airtport_codes_new( request ):
# 	#query = request.POST.get("query","")
# 	#print query
# 	codes = AirportCodes.objects.all()
# 	for code in codes:
# 		title = code.title
# 		q = AirportCodesNew(title = title[:-4],code = title[-4:] )
# 		q.save()
# 	return render( request, "formatter_result.html",{ "words": codes })

# def airport_codes_new( request ):
# 	#query = request.POST.get("query","")
# 	#print query
# 	airports = AirportCodesNew.objects.all()
# 	print airports[0]
# 	for airport in airports:
# 		code = airport.code
# 		print code[0:3]
# 		# q = code[0]+code[1]+code[2]
# 		airport.code_new = code[0:3]

# 		airport.save()
		
# 	return render( request, "formatter_result.html",{ "words": airports })

# def final_airport_codes( request ):
# 	airports = AirportCodesNew.objects.all()
# 	for airport in airports:
# 		code = airport.code
# 		a = AirportCode(title=airport.title,code=airport.code_new)
# 		a.save()
# 	words = AirportCode.objects.all()
# 	return render( request, "formatter_result.html",{ "words": words })

def final_airport_codes( request ):
	airports = AirportCode.objects.all()
	words = []
	for airport in airports:
		title = airport.title
		title_and_airportname = title.split("-")
		title = title_and_airportname[0]
		title = title.strip()

		try:
			airport_name = title_and_airportname[1]
			airport_name = airport_name.strip()
			airport.title = title
			airport.airport_name = airport_name
		except Exception:
			airport.title = title
			airport.airport_name = ""
		# title = title.strip()
		# airport_name = airport_name.strip()
		airport.save()
		#words.append(title+" and this " + airport_name)
		#a = AirportCode(title=airport.title,code=airport.code_new)
		#a.save()
	words = AirportCode.objects.all()
	return render( request, "formatter_result.html",{ "words": words })


def booking( request ):
	booking_form  = BookingForm()

	# post_data = [('From', "01139586919"),('To', "09897658560"),('Body',"this is new")]     # a sequence of two element tuples
	# result = urllib2.urlopen('https://oceanatravels3:06789637503cc47262657202361690bf527454e1@twilix.exotel.in/v1/Accounts/oceanatravels3/Sms/send', urllib.urlencode(post_data))
	# content = result.read()
	sid = "oceanatravels3"
	token = "06789637503cc47262657202361690bf527454e1"
	phone_num = "01139586919"
	to = "09897658560"
	body = "hello buddy"
	payload = {"From": phone_num,"To":to,"Body":body }
 	#response = requests.post('https://oceanatravels3:06789637503cc47262657202361690bf527454e1@twilix.exotel.in/v1/Accounts/oceanatravels3/Sms/send', data=payload)
 	response = requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': phone_num,
            'To': to,
            'Body': body
	})
	print response
	print response.text
	return render( request, "booking_page.html" , { "booking_form":booking_form } )

def booking_request( request ):
	booking_form = BookingForm( request.POST )
	if booking_form.is_valid():
		booking_form.save()
		return HttpResponse("afsdkjdls")
	else:
		return render( request, "booking_page.html" , { "booking_form":booking_form } )


def pdfview(request):
    #Retrieve data or whatever you need
    res = ["1","2","3"]
    return render_to_pdf(
            'pdftemplate.html',
            {
                'pagesize':'A4',
                #'mylist': res,
            }
        )

def itinerary( request ):

	pkgs = Package.objects.all()
	pkg_list = [pkgs[0]]
	context = {"pkgs":pkgs }
	return render( request,"itinerary_list.html",context)

def itinerary_detail( request, package_id ):
	pkg = Package.objects.get(id = package_id )
	return render( request, "itinerary_detail.html",{"pkg":pkg})

def pdf_generator( request ):

	html = request.POST.get('html_data','').encode("utf-8")
	pkg_id  = request.POST.get('pkg_id','')
	html_file = open('dummyapp/templates/templatefile.html','wb')
	html_file.write(html)
	html_file.close()
	temp_file = 'templatefile.html'
	return render_to_pdf( temp_file,{'pkg_id':pkg_id} )

def homepage( request ):
	if request.method=="POST":
		form  = SearchForm( request.POST )
		if form.is_valid():
			return HttpResponse("adsfhj")
		else:
			return render( request,'homepage.html',{'form':form })

	return render( request, 'homepage.html' )

def search_result_page( request ):
	form  = SearchForm( request.POST )
	if form.is_valid():
		return HttpResponse("adsfhj")
	else:
		return render( request,'homepage.html',{'form':form })

def filter( request ):
	pkgs = Package.objects.all()
	pkg_list = pkgs[11:]
	context = {"pkgs":pkg_list}
	return render( request,'hotel-list-view.html' ,context )

def video( request ):
	return render( request,'video_template.html')

def apply_coupon( request ):
	package_quote = PackageQuote.objects.get( pk=6 )
	return render( request,'apply_coupon.html', {'pkg_quote': package_quote } )
# def coupon_applied( request ):
# 	price = request.POST.get('price','')
# 	coupon_code = request.POST.get('coupon_code','')
# 	print coupon_code
# 	print type(coupon_code)
# 	coupon  = Coupon.objects.get(code = coupon_code)
# 	print coupon
# 	value = coupon.value
# 	coupon_type = coupon.type
# 	campaign = coupon.campaign
# 	pkg_name = "maldives_coupon"
# 	pkg_hash = "qwer"
# 	if not coupon.expired():
# 		pkg_quote = PackageQuote.objects.get(pkg_hash = pkg_hash)
# 		print pkg_quote
# 		pkg_quote.coupon_code = coupon_code
# 		price = int(price)-coupon.value
# 		pkg_quote.price_with_coupon = price
# 		pkg_quote.save()
# 		print pkg_quote.coupon_code
# 		print "yay"
		
# 	return render( request, 'coupon_applied.html', {'price':price })

def coupon_applied( request ):
	price = request.POST.get('price','')
	coupon_code = request.POST.get('coupon_code','')
	print coupon_code
	print type(coupon_code)
	coupon  = Coupon.objects.get(code = coupon_code)
	print coupon
	value = coupon.value
	coupon_type = coupon.type
	campaign = coupon.campaign
	pkg_name = "maldives_coupon"
	pkg_hash = "qwer"
	coupon_price  = price
	if not coupon.expired():
		pkg_quote = PackageQuote.objects.get(pkg_hash = pkg_hash)
		print pkg_quote
		pkg_quote.coupon_code = coupon_code
		coupon_price = int(price)-coupon.value
		pkg_quote.price_with_coupon = price
		pkg_quote.save()
		print pkg_quote.coupon_code
		print "yay"

	dic = {"coupon_price":coupon_price }	
	return HttpResponse(
            json.dumps(dic),
            content_type="application/json"
        )
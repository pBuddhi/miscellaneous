from __future__ import unicode_literals
from django.utils.text import slugify
from django.db import models
import time
import hashlib

BUDGET_TYPE_CHOICES = (
	('ECO', 'ECO'),
	('DELX', 'DELX'),
	('LUX', 'LUX'),
)

class Booking( models.Model ):
	guest_name_1 = models.CharField( max_length = 250 )
	guest_name_2 = models.CharField( max_length = 250 )
	phone_num_1 = models.CharField( max_length = 250 )
	phone_num_2 = models.CharField( max_length = 250 )
	email_id_1 = models.CharField( max_length = 250 )
	email_id_2 = models.CharField( max_length =250 )
	destination = models.CharField( max_length = 250,blank=True )
	hotel = models.TextField( max_length = 250 ,blank=True)
	room = models.CharField( max_length = 250 ,blank=True)
	check_in = models.CharField( max_length = 250 ,blank=True)
	check_out = models.CharField( max_length = 250 ,blank=True)
	tours = models.TextField( max_length = 250 ,blank=True)
	transfers = models.TextField( max_length = 250 ,blank=True)
	inclusions = models.TextField( max_length = 250 ,blank=True)
	price_quoted_in_foreign_currency = models.CharField( max_length = 250 ,blank=True)
	foreign_currency = models.CharField( max_length = 250,blank=True )
	price_quoted_in_inr = models.CharField( max_length = 250 ,blank=True)

	created_at = models.DateTimeField( auto_now_add = True )


class Search( models.Model ):
	query = models.CharField( max_length = 255 )
	checkin = models.DateField()
	checkout = models.DateField()
	duration = models.IntegerField()

	created_at = models.DateTimeField( auto_now_add = True )

	def __unicode__( self ):
		return u'%s' % ( self.query )


class Region( models.Model ):
	title = models.CharField( max_length = 255 )

	def __unicode__( self ):
		return u'%s' % ( self.title )


class Country( models.Model ):
	title = models.CharField( max_length = 255 )
	region = models.ForeignKey( Region )

	def __unicode__( self ):
		return u'%s, %s' % ( self.title, self.region )


class Destination( models.Model ):
	title = models.CharField( max_length = 255 )
	country = models.ForeignKey( Country )

	def __unicode__( self ):
		return u'%s, %s' % ( self.title, self.country )


class Accommodation( models.Model ):
	title = models.CharField( max_length = 255 )
	destination = models.ForeignKey( Destination )
	accommodation_type = models.CharField( max_length =250 ,default = "hotel" )
	star_rating = models.CharField( max_length = 250 ,default = 5 )

	def __unicode__( self ):
		return u'%s, %s' % ( self.title, self.destination )


class Room( models.Model ):
	title = models.CharField( max_length = 255 )
	accommodation = models.ForeignKey( Accommodation )

	room_rate_hash = models.CharField( max_length = 255, blank = True )

	def __unicode__( self ):
		return u'%s, %s' % ( self.title, self.accommodation )


class Inclusion( models.Model ):
	title = models.CharField( max_length = 255 )
	destination = models.ForeignKey( Destination )

	def __unicode__( self ):
		return u'%s, %s' % ( self.title, self.destination )


class Package( models.Model ):
	title = models.CharField( max_length = 255 )
	destination = models.ForeignKey( Destination )
	destination_title = models.CharField( max_length =250 ,null= True )
	duration = models.IntegerField()
	budget_type = models.CharField( max_length = 255, choices = BUDGET_TYPE_CHOICES )

	#room = models.ForeignKey( Room,null=True )
	accommodation = models.ForeignKey( Accommodation )
	default_inclusion = models.ManyToManyField( Inclusion, related_name = 'package_default_inclusion',
		blank = True )
	optional_inclusion = models.ManyToManyField( Inclusion, related_name = 'package_optional_inclusion',
		blank = True )
	slug1  = models.SlugField(editable=False,null=True)
	slug2 = models.SlugField(editable=False,null= True)
	hash_1 = models.CharField(max_length=10,null=True,unique=True,editable=False)
	is_voucher_exist = models.BooleanField(default=False)
	transfer_type = models.CharField( max_length = 250,default = 'shared' )
	def get_destination( self ):
		
		return self.destination.title

	def get_quote( self,check_in,check_out ):
		from helpers.utils import get_package_quote
		return get_package_quote( self, check_in, check_out )

	def get_absolute_url( self ):
		from django.core.urlresolvers import reverse
		return reverse( 'package_detail', args=[ self.slug1,self.slug2,self.hash_1,str( self.id ) ] )

	def save(self, *args, **kwargs):
		self.slug1 = slugify(self.destination.title)+"-honeymoon-package"
		self.slug2 = slugify(self.accommodation.title)
		if self.pk is None:
			hash = hashlib.sha1()
			hash.update(str(time.time()))
			self.hash_1 = hash.hexdigest()[:-10]
		super(Package, self).save(*args, **kwargs)

	def __unicode__( self ):
		return u'%s' % ( self.title )

class RateOfExchange( models.Model ):
	title = models.CharField( max_length = 250 )
	rate_of_exchange = models.CharField( max_length =250 )
	timestamp = models.DateTimeField( auto_now_add=True )
	
	def __unicode__( self ):
		return u'%s' % ( self.title )

# class AirportCodes( models.Model ):
# 	title = models.CharField( max_length = 300 )
# 	def __unicode__( self ):
# 		return u'%s' % ( self.title )

# class AirportCodesNew( models.Model ):
# 	title = models.CharField( max_length = 300 )
# 	code = models.CharField( max_length = 10 )
# 	code_new = models.CharField( max_length = 10 )
# 	def __unicode__( self ):
# 		return u'%s' % ( self.title )

class AirportCode( models.Model ):
	title = models.CharField( max_length = 300 ,blank=True)
	code = models.CharField( max_length = 10,blank=True )
	airport_name = models.CharField( max_length = 250,blank = True )
	def __unicode__( self ):
		return u'%s' % ( self.title )

# class Search( models.Model ):
# 	query =models.CharField(max_length = 250 )
# 	check_in = models.CharField(max_length = 250 )
# 	check_out= models.CharField(max_length = 250 )
# 	duration  = models.CharField(max_length = 250 )
# 	def __unicode__( self ):
# 		return u'%s' % ( self.query )

class PackageQuote( models.Model ):
	title = models.CharField( max_length = 250 )
	pkg_hash = models.CharField( max_length = 250 )
	coupon_code = models.CharField( max_length =250,blank = True )
	price = models.CharField( max_length =250 )
	price_with_coupon = models.CharField( max_length =250 ,blank =True)

class AirportCodesImport( models.Model ):
	city_name = models.CharField( max_length = 250 )
	airport_code = models.CharField( max_length = 250 )
	airport_name = models.CharField( max_length =250 )
	country_name = models.CharField( max_length = 250 )
	country_abbrev = models.CharField( max_length =250 )
	world_area_code = models.CharField( max_length =250 )





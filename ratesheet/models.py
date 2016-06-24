from __future__ import unicode_literals

from django.db import models


class Supplier( models.Model ):
	title = models.CharField( max_length = 255 )

	def __unicode__( self ):
		return u'%s' % ( self.title )

class SailingDate( models.Model ):
	title = models.CharField( max_length =250 )
	sailing_date = models.DateField( blank=True, null=True )

	def __unicode__( self ):
		return u'%s' % ( self.title )


class RoomRate( models.Model ):
	title = models.CharField( max_length = 255 )

	destination = models.CharField( max_length = 255 )
	accommodation = models.CharField( max_length = 255 )
	room = models.CharField( max_length = 255 )
	duration = models.IntegerField()
	is_cruise =models.BooleanField(default=False)
	sailing_dates = models.ManyToManyField( SailingDate ,null=True)
	surcharge = models.CharField( max_length =250,default='0' )
	supplier = models.ForeignKey( Supplier )
	rate_per_person = models.CharField( max_length = 255 )
	rate_currency = models.CharField( max_length = 255 )
	tax = models.CharField( max_length = 255, blank = True )
	inclusion = models.TextField( blank = True )
	valid_from = models.DateField( blank = True, null = True )
	valid_until = models.DateField( blank = True, null = True )

	remark = models.TextField( blank = True )

	def __unicode__( self ):
		return u'%s' % ( self.title )

class RateOfExchange( models.Model ):
	title = models.CharField( max_length = 250 )
	rate_of_exchange = models.CharField( max_length =250 )
	timestamp = models.DateTimeField( auto_now_add=True )
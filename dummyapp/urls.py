from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page
from django.conf import settings

urlpatterns = [
	url(r'^$',views.firstview,name='firstview'),
   	url(r'^second$',views.secondview,name='secondview'),
   	url(r'^search$',views.search,name='search'),
   	url(r'^search-result$',views.search_result,name='search_result'),
   	url(r'^logging$',views.logging_view,name='logging_view'),
	#url(r'^package-detail/(?P<package_id>\d+)/$', views.package_detail, name='package_detail' ),
	#url(r'^package-detail/(?P<package_id>\d+)/$',views.package_detail,name='package_detail')
 	url(r'^(?P<slug1>[-\w\d]+)/(?P<slug2>[-\w\d]+)-(?P<hash_1>[-\w\d]+)/(?P<package_id>\w+)/$', views.package_detail, name='package_detail'),
   	url(r'^logglykey$',views.logglykey,name='logglykey'),
   	url(r'^formatter$',views.formatter,name='formatter'),
   	url(r'^formatter/result$',views.formatter_result,name='formatter_result'),
    url(r'^airport/codes$',views.airport_codes,name='airport_codes'),
    url(r'^final/airport/codes$',views.final_airport_codes,name='final_airport_codes'),
    url(r'^booking$',views.booking,name='booking'),
    url(r'^booking/request$',views.booking_request,name='booking_request'),

    url(r'^pdf$',views.pdfview,name='pdfview'),
    url(r'^itinerary$',views.itinerary,name='itinerary'),
    url(r'^itinerary/detail/(?P<package_id>\d+)$',views.itinerary_detail,name='itinerary_detail'),
    url(r'^pdf_generator$',views.pdf_generator,name='pdf_generator'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT}),
    url(r'^homepage$',views.homepage ,name='homepage'),
    url(r'^search/result$',views.search_result_page ,name='search_result_page'),
    url(r'^filter$',views.filter ,name='filter'),
    url(r'^video$',views.video ,name='video'),
    url(r'^apply-coupon$',views.apply_coupon ,name='apply_coupon'),
    url(r'^coupon-applied$',views.coupon_applied ,name='coupon_applied'),





    ]

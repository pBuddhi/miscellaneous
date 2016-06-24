from django.shortcuts import render,redirect

def get_package_quote(package,check_in,check_out):
	from ratesheet.helpers.utils import get_hotel_quote
	hotel_quote = get_hotel_quote( package.room.room_rate_hash, check_in, check_out,package.duration )
	rate_in_inr = hotel_quote['rate_in_inr']
	inclusion = hotel_quote['inclusion']
	return u'%d %s %s' % (rate_in_inr,"per person",inclusion)

def meth(sender):
	print "print pint pririnsdf"
	print sender
	return
from  django.views.decorators.cache import cache_page

@cache_page(60)
def caching_view(request):
	for i in range(100000):
		print "hello"
	return True

# import cStringIO as StringIO
# from xhtml2pdf import pisa
# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
# from cgi import escape
# from reportlab.pdfgen import canvas

# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     #result = StringIO.StringIO()\
#     filename = "assets/pdf_file_1.pdf"
#     result = open(filename, 'wb') # Changed from file to filename

#     pdf = pisa.pisaDocument(StringIO.StringIO(html), result)
#     result.close()
#     result1 = StringIO.StringIO()
#     pdf1 = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8"))
  

#     print type(pdf)
#     if not pdf.err:
#     	#response = HttpResponse(result1.getvalue(), content_type='application/pdf')
#     	#response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
#     	# p = canvas.Canvas(response)	    
#     	# p.save()
#     	# output_file = open('pdf_file.pdf', 'wb')
#     	# output_file.write(response)
#     	# output_file.close()
#         return HttpResponse(result1.getvalue(), content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

from weasyprint import HTML, CSS
# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context).encode("utf-8")
#     #result = StringIO.StringIO()\
#     filename = "assets/pdf_file_1.pdf"
#     #result = open(filename, 'wb') # Changed from file to filename
#     #stylesheets = ["assets/pdf.css","assets/global/plugins/font-awesome/css/font-awesome.min.css","assets/global/plugins/simple-line-icons/simple-line-icons.min.css","assets/global/plugins/bootstrap/css/bootstrap.min.css","assets/global/plugins/bootstrap/css/bootstrap.min.css","assets/global/plugins/bootstrap-switch/css/bootstrap-switch.min.css","assets/global/plugins/bootstrap-daterangepicker/daterangepicker.min.css","assets/global/plugins/morris/morris.css","assets/global/plugins/fullcalendar/fullcalendar.min.css","assets/global/plugins/jqvmap/jqvmap/jqvmap.css","assets/global/css/components.min.css","assets/global/css/plugins.min.css","assets/layouts/layout2/css/layout.min.css","assets/layouts/layout2/css/themes/blue.min.css","assets/layouts/layout2/css/custom.min.css"]
#     pdf_file = HTML(string=html).write_pdf('assets/mywebsite.pdf')
#     http_response = HttpResponse(pdf_file, content_type='application/pdf')
#     http_response['Content-Disposition'] = 'filename="report.pdf"'
#     # result.write(pdf)
#     # result.close()
#     # result1 = StringIO.StringIO()
#     # pdf1 = pisa.pisaDocument(StringIO.StringIO(html, result1))
#     # response = HttpResponse(result1.getvalue(), content_type='application/pdf')
#     #     #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
#     #     # p = canvas.Canvas(response)       
#     #     # p.save()
#     #     # output_file = open('pdf_file.pdf', 'wb')
#     #     # output_file.write(response)
#     #     # output_file.close()
#     # return HttpResponse(result1.getvalue(), content_type='application/pdf')

#     # HTML('http://youtube.com/').write_pdf('assets/mywebsite.pdf',
#     # stylesheets=[CSS(string='body { font-family: Arial }')])
#     return http_response

def render_to_pdf( template_src, context_dict ):
    #template = get_template( template_src )
    # html_file = open('template_file_2.html','wb')
    # html_file.write(template_src)
    # #html_file.save()
    # html_file.close()
    # html_file = 'template_file_2.html'
    template  = get_template( template_src )
    #html_file.close()
    context = Context( context_dict )
    html = template.render( context_dict ).encode("UTF-8")
    pdf = HTML(string=html).write_pdf('media/pkg_id_'+context['pkg_id'] + '.pdf',stylesheets=[])
    from dummyapp.models import Package
    pkg = Package.objects.get(id=context['pkg_id'])
    pkg.is_voucher_exist = True
    pkg.save()
    print pkg
    # response = HttpResponse(pdf,content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=filename1.pdf'
    #response['X-Sendfile'] = "assets/mywebsite.pdf"

    #print response
    return redirect('itinerary')

# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()

#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
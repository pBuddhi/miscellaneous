from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template import Context
from django.shortcuts import render,redirect
from django.template.loader import render_to_string



# def send_custom_email_mandrill(email_to,temp_vars):
# 	msg = EmailMessage(to=[email_to],from_email='varun@tveen.in')
# 	msg.template_name = "email_template.html"  # slug from Mandrill
# 	msg.global_merge_vars = temp_vars
# 	msg.use_template_subject = True
# 	msg.use_template_from = False																																																																																																																																																																																																																																																																																																																																																																																																																																												
# 	msg.send()
def send_custom_email_mandrill(email_to,temp_vars):
	text_content = "this is text content"
	context = Context(temp_vars)
	html_content = render_to_string('email_template.html', context)

	#msg = EmailMultiAlternatives(to=[email_to],from_email='varun@oceanatravels.com')
	msg = EmailMultiAlternatives(  subject="Your Subject",
  	body="This is a simple text email body.",
  	from_email="Varun Bansal <varun@oceanatravels.com>",
  	to=['support@oceana.freshdesk.com','buddhi9417@gmail.com']
  	#headers={"Reply-To": "support@oceana.freshdesk.com"}
  	)
	msg.attach_alternative(html_content, "text/html")

	# msg.template_name = "email_template.html"  # slug from Mandrill
	# msg.global_merge_vars = temp_vars
	# msg.use_template_subject = True
	# msg.use_template_from = False																																																																																																																																																																																																																																																																																																																																																																																																																																												
	msg.send()


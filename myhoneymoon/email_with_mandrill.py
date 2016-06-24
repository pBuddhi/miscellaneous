from django.core.mail import EmailMessage
def send_custom_email_mandrill(email_to,temp_vars):
	msg = EmailMessage(to=[email_to])
	msg.template_name = "test-email"  # slug from Mandrill
	msg.global_merge_vars = temp_vars
	msg.use_template_subject = True
	msg.use_template_from = True
	msg.send()
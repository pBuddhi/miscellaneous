from django.utils.log import AdminEmailHandler
import sys
import traceback
class MyCustomAdminEmailHandler(AdminEmailHandler):
    # emit copied and overridden from v1.8 so we can add the request .user into the message
    def emit(self, record):
        from django.views.debug import ExceptionReporter

        print record
        print record.getMessage()
        email_to = 'support@oceana.freshdesk.com'
        email_body = record.getMessage()
        print record.lineno
        current_user = None
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                ('internal' if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 else 'EXTERNAL'),
                record.getMessage()
            )
            # filter = get_exception_reporter_filter(request)
            # request_repr = '\n{}'.format(force_text(filter.get_request_repr(request)))
            # current_user = request.user
        except Exception:

            print 'asdfjl'

            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
            request_repr = "unavailable"
        subject = self.format_subject(subject)

        if record.exc_info:
            exc_info = record.exc_info
        else:
            print "no info"
            exc_info = (None, record.getMessage(), None)

        message = "mssg:%s" % (self.format(record))
        reporter = ExceptionReporter(request, is_email=True, *exc_info)
        html_message = reporter.get_traceback_html() if self.include_html else None
        #text_message = reporter.technical_404_response(exc_info)
        text_message= "jeuy"
        temp_vars = {
        'FOO': email_to,
          'msg': message,
          'url': text_message,
          'lineno': record.lineno,
          'pathname': record.pathname,

          'email_body': email_body
          #'image':'http://www.oceanatravels.com/site_media/img/oceana-logo.png'
        }
        from email_with_mandrill import *

        send_custom_email_mandrill(email_to,temp_vars)
        #self.send_mail(subject, record.getMessage(), fail_silently=True, html_message=html_message)
        # requests.post(settings.SLACK_WEBHOOK_URL, json={
        #     "fallback": message,
        #     "pretext": "An error occured",
        #     "color": "#ef2a2a",
        #     "fields": [
        #         {
        #             "title": "Error",
        #             "value": message,
        #             "short": False
        #         }
        #     ]
        # })
from ConfigParser import RawConfigParser
#config = RawConfigParser()
#config.read('/etc/auth_tveen/tveen_settings.ini')
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_PATH = '/var/live_code/oceana_project/oceana/'
ENV = 'myhoneymoon'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('BUDDHI PRAKASH','support@oceana.freshdesk.com'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'myhoneymoon',
        'USER': 'root',
        'PASSWORD': 'bossisgreat',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306'
    }  
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/home/buddhi/Desktop/myhoneymoon' + '/travelo_assets/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/site_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/buddhi/Desktop/myhoneymoon' + '/assets/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#STATIC_URL = '/static/'

# Additional locations of static files
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )
STATIC_URL = '/assets/'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "travelo_assets")+"/ajax",
    # os.path.join(BASE_DIR, "travelo_assets")+"/components",
    # os.path.join(BASE_DIR, "travelo_assets")+"/css",
    # os.path.join(BASE_DIR, "travelo_assets")+"/fonts",
    # os.path.join(BASE_DIR, "travelo_assets")+"/images",
    # os.path.join(BASE_DIR, "travelo_assets")+"/js",
]


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3+kxt-niq8k4jyoq!24!%qe-x2u*&-!v%kw13iz@qj5ujyv@1m'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = ENV + '.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = ENV + '.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

INSTALLED_APPS = (
    #'uti',
    'csvimport.app.CSVImportConf',
    'sendgrid',
    'coupons',
    'dummyapp',
    'ratesheet',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
#    'ocndata',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
from dummyapp.custom_handler import MyCustomAdminEmailHandler
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'formatters': {
#         'simple': {
#             'format': '%(asctime)s PARAM django: %(message)s',
#             'datefmt': '%Y-%m-%dT%H:%M:%S',
#         },
#     },

#     'handlers': {
#                 'SysLog':{
#           'level':'DEBUG',
#           'class':'logging.handlers.SysLogHandler',
#           'formatter': 'simple',
#           'address':('logs4.papertrailapp.com', 49541)
#         },
           
#         'mail_admins': {
#             'level': 'DEBUG',
#             #'filters': ['require_debug_false'],
#             'class': 'dummyapp.custom_handler.MyCustomAdminEmailHandler',
#             #'class': 'django.utils.log.AdminEmailHandler',
#             # 'email_backend':'djrill.mail.backends.djrill.DjrillBackend',
#             'include_html': True

#         }
#     },
#     'loggers': {
#      # 'file': {
#      #            'level': 'ERROR',
#      #            'class': 'logging.FileHandler',
#      #            'filename': './logs/debug.log',
#      #        },
#          'django.request': {
#         'handlers': ['mail_admins'],
#         'level': 'ERROR',
#         'propagate': False,
#         },
#         'loggly_logs': {
#             'handlers': ['mail_admins','SysLog'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     }
# }
#settings for loggly
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'formatters': {
      'django': { 
         'format':'django: %(message)s',
       },
    },

   'handlers': {
      'logging.handlers.SysLogHandler': {
         'level': 'DEBUG',
         'class': 'logging.handlers.SysLogHandler',
         'facility': 'local7',
         'formatter': 'django',
         'address' : '/dev/log',
       },
        'mail_admins': {
            'level': 'DEBUG',
            #'filters': ['require_debug_false'],
            'class': 'dummyapp.custom_handler.MyCustomAdminEmailHandler',
            #'class': 'django.utils.log.AdminEmailHandler',
            #'email_backend':'djrill.mail.backends.djrill.DjrillBackend',
            'email_backend': 'sgbackend.SendGridBackend',
            'include_html': True

        }
   },

   'loggers': {
      'loggly_logs':{
         'handlers': ['logging.handlers.SysLogHandler'],
         'propagate': True,
         'format':'django: %(message)s',
         'level': 'DEBUG',
       },
             'django.request':{
         'handlers': ['logging.handlers.SysLogHandler'],
         'propagate': True,
         'format':'django: %(message)s',
         'level': 'DEBUG',
       },
    }
}
# settings for papertraiil
# LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'formatters': {
#       'django': { 
#          'format':'django: %(message)s',
#        },
#     },

#     'formatters': {
#         'simple': {
#             'format': '%(asctime)s PARAM django: %(message)s',
#             'datefmt': '%Y-%m-%dT%H:%M:%S',
#         },
#     },

#    'handlers': {
#         'SysLog':{
#           'level':'DEBUG',
#           'class':'logging.handlers.SysLogHandler',
#           'formatter': 'simple',
#           'address':('logs4.papertrailapp.com', 49541)
#         }

#    },

#    'loggers': {
#       'loggly_logs':{
#          'handlers': ['SysLog'],
#          'propagate': True,
#          'format':'django: %(message)s',
#          'level': 'DEBUG',
#        },
#         'django': {
#             'handlers': ['SysLog'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_TLS = True
# EMAIL_PORT = 587

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'buddhi9417@gmail.com'
# EMAIL_HOST_PASSWORD = 'bossisgreat'

# EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

# MANDRILL_API_KEY = "KaN3swPW5B3pWB1qNOHQbQ"

SEND_BROKEN_LINK_EMAILS = True

#setting to include assets




CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}   

EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = "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"
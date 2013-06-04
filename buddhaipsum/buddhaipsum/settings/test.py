# ===========================================
# ./settings/test.py
#  This is a template
#
#  Change:
#  Line 21-   DATABASES- NAME
#  
#  LINE 32-   ALLOWED_HOSTS
#  LINE 37-   TEMPLATE_DIRS
#
# ===========================================

from .base import * 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'D:/DjangoDev/DB/api.db',                      
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      
        'PORT': '',                 
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['webdev.datumlogic.com']

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#	'/Users/gene/Documents/TextMate/python/Survey/Survey/TEMPLATES',
)
# ===================
# api/urls.py
# ===================

from django.conf.urls import patterns, include, url

from .views import Admins

urlpatterns = patterns('',
	# Allow access to the contacts resource collection    
	url(r'^admins/?$', Admins.as_view()),    
	
	# Allow access to a single contact resource    
	url(r'^admins/(?P<admin_id>[0-9]+)/?$', Admins.as_view()),
)
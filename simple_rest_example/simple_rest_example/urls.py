# =============================
# simple_rest_example/urls.py
# =============================

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
	url(r'^phonebook/', include('phonebook.urls')), 
	url(r'^admin/', include(admin.site.urls)),
)
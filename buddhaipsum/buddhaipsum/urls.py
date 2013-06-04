# =============================
# buddhaipsum/urls.py
# =============================

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
	url(r'^api/', include('api.urls')),
	#url(r'^ipsum/', include('ipsum.urls')), 
	url(r'^admin/', include(admin.site.urls)),
)

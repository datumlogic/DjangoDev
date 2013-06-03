from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^polls/', include('polls.urls', namespace="polls")),  
url(r'^admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'Survey.views.home', name='home'),
    # url(r'^Survey/', include('Survey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

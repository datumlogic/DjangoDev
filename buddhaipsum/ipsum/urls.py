# =============================
# ipsum/urls.py
# =============================
from django.conf.urls import patterns, url

from .views import IpsumPages

urlpatterns = patterns('',
	# ex: /ipsum/
	url(r'^$', IpsumPages.as_view()),
)
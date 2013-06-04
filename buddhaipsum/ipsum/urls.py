# =============================
# ipsum/urls.py
# =============================
from django.conf.urls import patterns, url

from ipsum import views

urlpatterns = patterns('',
	# ex: /ipsum/
	url(r'^$', views.index, name='index'),
)
# =============================
# ipsum/urls.py
# =============================
from django.conf.urls import patterns, url

from ipsum import views

urlpatterns = patterns('',
	# ex: /ipsum/
	url(r'^$', views.index, name='index'),
	# ex: /polls/5/
	url(r'^(?P<ipsum_words>\d+)/$', views.words, name='words'),
	# ex: /polls/5/4/
	url(r'^(?P<ipsum_words>\d+)/(?P<ipsum_sentences>\d+)/$', views.sentences, name='sentences'),
)
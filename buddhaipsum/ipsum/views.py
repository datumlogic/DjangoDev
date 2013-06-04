from django.http import HttpResponse #we can loose this later...
#from django.shortcuts import render, get_object_or_404
#from django.http import Http404

#from django.shortcuts import get_object_or_404, render 
#from django.http import HttpResponseRedirect, HttpResponse 
#from django.core.urlresolvers import reverse


#empty- index is where we'll show the form is 
def index(request):
	return HttpResponse(""You’re looking at the index")



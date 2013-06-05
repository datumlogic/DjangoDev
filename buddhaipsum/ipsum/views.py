from django.http import HttpResponse #this import may not be needed later

from ipsum.ModelBuilders import PageBuilder

from simple_rest.auth.decorators import signature_required, admin_required, login_required

# just for demo now. This should take a KeyID as an arg and lookup the secret in a database
def secret_key(request, *args, **kwargs):
	return 'test'

#global singleton instance for the ModelBuilder class
builder = None


def index(request):
	return HttpResponse("This is Index.html<br />This page will contain the form to set the variables for the ipsum generator.")


def words(request, ipsum_words):
	return HttpResponse("This is the WORD detail: %s" % ipsum_words)

@login_required
def sentences(request, ipsum_words, ipsum_sentences):
	# global builder cache's the PageBuilder class/latin-Dictionary.txt in memory
	global builder
	if builder == None:
		builder = PageBuilder('latin_dictionary.txt')
	rtn = builder.buildPage(1,ipsum_words,1,ipsum_sentences,1)
	return HttpResponse(rtn)
	#return HttpResponse("This is the SENTENCES detail: <br />%s %s" % (ipsum_words,ipsum_sentences))
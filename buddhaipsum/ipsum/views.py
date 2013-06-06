from django.http import HttpResponse #this import may not be needed later

from simple_rest import Resource
from simple_rest.auth.decorators import signature_required, admin_required, login_required

from django.template import Context, loader

from ipsum.ModelBuilders import PageBuilder

# just for demo now. This should take a KeyID as an arg and lookup the secret in a database
def secret_key(request, *args, **kwargs):
	return 'test'

#global singleton instance for the ModelBuilder class
#everytime the view calls IpsumPages, a new class instances is created, so cannot use a class member var
builder = None

class IpsumPages(Resource):

	def get(self, request, contact_id=None, **kwargs):
		template = loader.get_template('ipsum/index.html') 
		context = Context()
		return HttpResponse(template.render(context))
		#return HttpResponse("This is a GET request", content_type='application/json', status=200)
		
	def post(self, request, *args, **kwargs):
		minwords= request.POST.get('minwords')
		maxwords=request.POST.get('maxwords')
		minsentences=request.POST.get('minsentences')
		maxsentences=request.POST.get('maxsentences')
		paragraphs=int(request.POST.get('paragraphs'))
		#rtnX='NON'
		global builder;
		if builder == None:
			builder = PageBuilder('latin_dictionary.txt')
			#rtnX='init'
		rtn = builder.buildPage(minwords,maxwords,minsentences,maxsentences,paragraphs)
		#return HttpResponse(rtn)
		template = loader.get_template('ipsum/result.html')
		context = Context({'ipsum_page':rtn,})
		return HttpResponse(template.render(context))

# ====================
# phonebook/views.py
# ====================

from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource

from .models import ApiUser

from simple_rest.auth.decorators import admin_required

# just for demo now. This should take a KeyID as an arg and lookup the secret in a database
def secret_key(request, *args, **kwargs):
	return 'test'

@admin_required
class Admins(Resource):

	def get(self, request, admin_id=None, **kwargs):
		json_serializer=serializers.get_serializer('json')()
		if admin_id:
			admins=json_serializer.serialize(ApiUser.objects.filter(pk=admin_id))
		else:
			admins=json_serializer.serialize(ApiUser.objects.all())
		return HttpResponse(admins, content_type='application/json', status=200)

	def post(self, request, *args, **kwargs):
		ApiUser.objects.create(
			emailAddr=request.POST.get('emailAddr'),
			appName=request.POST.get('appName'),
			keyID=request.POST.get('keyID'))
		return HttpResponse(status=201) #created    

	def delete(self, request, admin_id):        
		admin=ApiUser.objects.get(pk=admin_id)        
		admin.delete()        
		return HttpResponse(status=200)
#			def post(self, request, *args, **kwargs):
#				form = TestForm(request.POST)
#				if (form.is_valid()):
#					minwords= request.POST.get('minwords')
#					maxwords=request.POST.get('maxwords')
#					minsentences=request.POST.get('minsentences')
#					maxsentences=request.POST.get('maxsentences')
#					paragraphs=request.POST.get('paragraphs')
#					#rtnX='NON'
#					global builder;
#					if builder == None:
#						builder = PageBuilder('latin_dictionary.txt')
#						#rtnX='init'
#					rtn = builder.buildPage(minwords,maxwords,minsentences,maxsentences,paragraphs)
#					#return HttpResponse(rtn)
#					template = loader.get_template('ipsum/result.html')
#					context = Context({'ipsum_page':rtn,})
#					return HttpResponse(template.render(context))

def get(self, request, contact_id=None, **kwargs):
	#template = loader.get_template('ipsum/index.html') 
	#context = Context()
	#return HttpResponse(template.render(context))
	#return HttpResponse("This is a GET request", content_type='application/json', status=200)
	form = TestForm() # An unbound form
	return render_to_response('ipsum/test.html', {'form': form,})
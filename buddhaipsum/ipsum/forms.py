from django import forms

class TestForm(forms.Form):
	minwords = forms.CharField(max_length=4)           
	maxwords = forms.CharField(max_length=4) 
	minsentences = forms.CharField(max_length=4) 
	maxsentences = forms.CharField(max_length=4) 
	paragraphs = forms.CharField(max_length=34) 
	keyID = forms.CharField(max_length=12) 
	sig =  forms.CharField(max_length=36) 
	t =  forms.CharField(max_length=16) 
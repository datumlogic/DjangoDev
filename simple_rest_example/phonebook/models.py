# =====================
# phonebook/models.py
# =====================

from django.db import models

class Contact(models.Model):
	title = models.CharField(max_length=10, default='(no title)')    
	fname = models.CharField(max_length=30)    
	lname = models.CharField(max_length=30)    
	phone_number = models.CharField(max_length=12)
	
	def __unicode__(self):
	        return (self.fname + ' ' + self.lname + ' ' + self.phone_number)


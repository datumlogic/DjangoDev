# =====================
# api/models.py
# =====================

from django.db import models

class ApiUser(models.Model):
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	emailAddr = models.CharField(max_length=256)
	appName = models.CharField(max_length=16)
	secretKey = models.CharField(max_length=36)
	keyID = models.CharField(max_length=12)
	dtUpdated = models.DateField(auto_now=True)
	pendingDelete = models.BooleanField()
	def __unicode__(self):
		return (self.keyID  + ' for /' + self.appName)


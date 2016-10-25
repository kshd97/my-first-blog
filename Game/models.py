from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
#from django.contrib.auth.models import User


class GroupDetails(models.Model):
	grpid = models.AutoField(primary_key = True)
	StartTime = models.IntegerField(max_length = 10)
	EndTime = models.IntegerField(max_length = 10)
	City = models.CharField(max_length=20)
	Location = models.CharField(max_length=100)
	Sport = models.CharField(max_length=40)

	def __str__(self):
		return self.City



	
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from Game.models import GroupDetails

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	address = models.CharField(max_length=100)
	grpid = models.ForeignKey(GroupDetails,on_delete=models.SET_NULL,null=True)
	mbno = models.CharField(max_length=10)


	def __str__(self):
		return self.user.first_name
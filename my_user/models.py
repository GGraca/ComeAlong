from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	#Relations
	"""projects_owned"""
	"""projects_participated"""
	"""applications"""

	#Fields
	"""name""" #from AbstractUser
	"""username""" #from AbstractUser
	avatar = models.ImageField(upload_to = 'img/',  default = 'default/img/user.png')
	description = models.TextField()

	city = models.CharField(max_length=50, null=True, default=None)
	country = models.CharField(max_length=50, null=True, default=None)

	facebook = models.URLField(max_length=100, null=True, default=None)
	linkedin = models.URLField(max_length=100, null=True, default=None)
	github = models.URLField(max_length=100, null=True, default=None)
	website = models.URLField(max_length=100, null=True, default=None)

	def __unicode__(self):
		return self.username

#2F3954
#C1E8E3
#EFEFEF
#C1C1B5
#9E9E9C
#recruitment
#oportunities

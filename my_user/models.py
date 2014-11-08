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
	avatar = models.ImageField(upload_to = 'img/',  default = 'img/default/user.jpg')
	description = models.TextField()

	def __unicode__(self):
		return self.username

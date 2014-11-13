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

#2F3954
#C1E8E3
#EFEFEF
#C1C1B5
#9E9E9C
#recruitment
#oportunities

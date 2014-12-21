from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
	avatar = models.ImageField(upload_to = 'img/',  default = 'default/img/user.png')
	description = models.TextField()

	city = models.CharField(max_length=50, null=True, default=None)
	country = models.CharField(max_length=50, null=True, default=None)

	facebook = models.URLField(max_length=100, null=True, default=None)
	linkedin = models.URLField(max_length=100, null=True, default=None)
	github = models.URLField(max_length=100, null=True, default=None)
	website = models.URLField(max_length=100, null=True, default=None)

	class Meta:
		abstract = True


class MyUser(AbstractUser, Profile, models.Model):
	#Relations
	"""projects_owned"""
	"""projects_participated"""
	"""applications"""
	"""projects_following"""

	#Atributes
	id = models.AutoField(primary_key=True)
	"""name""" #from AbstractUser
	"""username""" #from AbstractUser

	def __unicode__(self):
		return self.username

	def get_absolute_url(self):
		return u'/users/%s' % self.username

class Group(Profile, models.Model):
	id = models.AutoField(primary_key=True)


#2F3954
#C1E8E3
#EFEFEF
#C1C1B5
#9E9E9C
#recruitment
#oportunities

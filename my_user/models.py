from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
	nickname = models.CharField(max_length=200)
	birthday = models.DateField('birthday', auto_now_add=True , blank=True)
	#avatar = models.ImageField(upload_to = 'img/')

	def age():
		pass

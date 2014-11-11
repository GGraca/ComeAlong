from django.db import models
from my_user.models import MyUser

class Project(models.Model):
    #Relations
    founder = models.ForeignKey(MyUser, related_name="projects_owned")
    participants = models.ManyToManyField(MyUser, related_name = "projects_participated", blank=True)
    """vacancies"""
    """applications"""



    #Fields
    title = models.CharField(max_length=100)
    display_image = models.ImageField(upload_to="img/",  default = 'img/default/project.jpg')
    short_description = models.TextField()
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Vacancy(models.Model):
    #Relations
    project = models.ForeignKey(Project, related_name="vacancies")

    #Fields
    title = models.CharField(max_length=100)
    total = models.IntegerField()
    available = models.IntegerField()

    def closed(self):
        return self.total - self.available

    def __unicode__(self):
        return self.title


class Application(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="applications")
    project = models.ForeignKey(Project, related_name="applications")

    #Fields
    pitch = models.TextField()
    #result

    def __unicode__(self):
        return self.user.username + " -> " + self.project.title


class Participation(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="positions")
    project = models.ForeignKey(Project, related_name="positions")
    """titles """

class Title(models.Model):
    #Relations
    participation = models.ForeignKey(Participation, related_name="titles")

    #Fields
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

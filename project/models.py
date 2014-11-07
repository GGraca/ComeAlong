from django.db import models
from my_user.models import MyUser

class Project(models.Model):
    #Relations
    founder = models.ForeignKey(MyUser, related_name="projects_owned")
    participants = models.ManyToManyField(MyUser, related_name = "projects_participated", blank=True)
    """applications"""

    #Fields
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title



class Application(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="applications")
    project = models.ForeignKey(Project, related_name="applications")

    #Fields
    pitch = models.TextField()

    def __unicode__(self):
        return self.user.username + " -> " + self.project.title

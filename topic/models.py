from django.db import models
from my_user.models import MyUser
from project.models import Project

class Topic(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="topics")
    project = models.ForeignKey(Project, related_name="topics")

    #Fields
    closed = models.BooleanField(default=False);
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="comments")
    topic = models.ForeignKey(Topic, related_name="comments")

    #Fields
    description = models.TextField()

    def __unicode__(self):
        return self.description

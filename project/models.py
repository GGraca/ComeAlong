from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from my_user.models import MyUser, Group

class Event(models.Model):
    #Relations
    """projects"""

    #Fields
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    #Relations
    founder = models.ForeignKey(MyUser, related_name="projects_owned")
    participants = models.ManyToManyField(MyUser, related_name = "projects_participated", blank=True)
    event = models.ForeignKey(Event, related_name="projects", null=True, default=None)
    followers = models.ManyToManyField(MyUser, related_name = "projects_following", blank=True)

    """vacancies"""
    """applications"""
    """positions"""

    """limit = models.Q(app_label='my_user', model='MyUser') | \
        models.Q(app_label='my_user', model='Group')
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='content page',
        limit_choices_to=limit,
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(
        verbose_name='related object',
        null=True,
    )
    founder = generic.GenericForeignKey('content_type', 'object_id')"""

    #Fields
    title = models.CharField(max_length=100)
    display_image = models.ImageField(upload_to="img/",  default = 'default/img/project.jpg')
    cover_image = models.ImageField(upload_to="img/",  default = 'default/img/project.jpg')
    short_description = models.TextField()
    description = models.TextField()

    def has_vacancies(self):
        return self.vacancies.exclude(available=0)



    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return u'/projects/%d' % self.id

class Update(models.Model):
    project = models.ForeignKey(Project, related_name="updates")
    version = models.CharField(max_length=50)
    description = models.TextField()


class Vacancy(models.Model):
    #Relations
    project = models.ForeignKey(Project, related_name="vacancies")

    #Fields
    title = models.CharField(max_length=100)
    total = models.IntegerField()
    available = models.IntegerField()

    def closed(self):
        return self.total - self.available

    def isValid(self):
        if(self.title != "" and int(self.total) > 0):
            self.available=self.total
            return True;
        return False

    def __unicode__(self):
        return self.title


class Application(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="applications")
    project = models.ForeignKey(Project, related_name="applications")
    """roles"""

    #Fields
    pitch = models.TextField()

    RESULT_CHOICES = (
        ('W', 'Waiting'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    )
    result = models.CharField(max_length=1,
                                      choices=RESULT_CHOICES,
                                      default='W')


    def __unicode__(self):
        return self.user.username + " -> " + self.project.title


class Participation(models.Model):
    #Relations
    user = models.ForeignKey(MyUser, related_name="positions")
    project = models.ForeignKey(Project, related_name="positions")
    """titles"""

    def __unicode__(self):
        return self.user.username + " -> " + self.project.title

class Title(models.Model):
    #Relations
    application = models.ForeignKey(Application, related_name="roles", null=True)
    participation = models.ForeignKey(Participation, related_name="titles", null=True)

    #Fields
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

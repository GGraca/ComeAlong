from django import forms
from models import Project, Application

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ("founder", "title", "description")

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        #fields = ("founder", "title", "description")

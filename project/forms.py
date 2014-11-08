from django import forms
from models import Project, Application
from redactor.widgets import RedactorEditor

class ProjectForm(forms.ModelForm):

    description = forms.CharField(widget=RedactorEditor())
    class Meta:
        model = Project
        fields = ("title",  "short_description", "description") #"display_image",

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ("pitch",)

from django import forms
from models import Project, Application
from redactor.widgets import RedactorEditor

class ProjectForm(forms.ModelForm):

    description = forms.CharField(widget=RedactorEditor())
    class Meta:
        model = Project
        fields = ("title",  "display_image", "short_description", "description")

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ("pitch",)

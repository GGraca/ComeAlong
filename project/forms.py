from django import forms
from models import Project, Application, Vacancy
from redactor.widgets import RedactorEditor

class ProjectForm(forms.ModelForm):

    description = forms.CharField(widget=RedactorEditor())
    class Meta:
        model = Project
        fields = ("title",  "display_image", "cover_image", "short_description", "description")

class ApplicationForm(forms.ModelForm):

    pitch = forms.CharField(widget=RedactorEditor())

    def __init__(self, project, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.project = project
        self.set_roles()

    def set_roles(self):
        roles = self.project.vacancies.exclude(available=0)
        if(roles):
            choices = []
            for r in roles:
                choices += [[r.title, r.title]]

            self.fields["roles"] = forms.MultipleChoiceField(choices = choices, widget  = forms.CheckboxSelectMultiple)

    class Meta:
        model = Application
        fields = ("pitch",)

class AcceptApplicationForm(forms.Form):
    def __init__(self, app, *args, **kwargs):
        super(AcceptApplicationForm, self).__init__(*args, **kwargs)
        choices = []
        for r in app.roles.all():
            choices += [[r.title, r.title]]
        self.fields["roles"] = forms.MultipleChoiceField(choices = choices, widget  = forms.CheckboxSelectMultiple)


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ("title",  "total")

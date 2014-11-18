from django import forms
from models import MyUser
from redactor.widgets import RedactorEditor

class MyUserForm(forms.ModelForm):

    city = forms.CharField(required=False)
    country = forms.CharField(required=False)
    email = forms.CharField(required=False)
    
    website = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    linkedin = forms.URLField(required=False)
    github = forms.URLField(required=False)

    description = forms.CharField(widget=RedactorEditor(), required=False)

    class Meta:
        model = MyUser
        fields = (
            "first_name",
            "last_name",
            "avatar",

            "city",
            "country",

            "email",
            "website",

            "facebook",
            "linkedin",
            "github",

            "description",
        )

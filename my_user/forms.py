from django import forms
from models import MyUser

class MyUserForm(forms.ModelForm):

    city = forms.CharField(required=False)
    country = forms.CharField(required=False)
    email = forms.CharField(required=False)
    website = forms.CharField(required=False)
    facebook = forms.CharField(required=False)
    linkedin = forms.CharField(required=False)
    github = forms.CharField(required=False)

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

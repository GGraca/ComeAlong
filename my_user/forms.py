from django import forms
from models import MyUser

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("first_name", "last_name", "email", "avatar", "description")

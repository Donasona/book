from django import forms
from user_app.models import User

class Registerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email","password"]

class Loginform(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)



   
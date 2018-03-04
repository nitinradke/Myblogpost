from django import forms
from first_practice.models import userinfo

class NewUserForm(forms.ModelForm):
    class Meta():
        model = userinfo
        fields = "__all__"

class basicform(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()

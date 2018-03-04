from django import forms
from django.core import validators
from first_app.models import info_table

class NewUserForm(forms.ModelForm):
    class Meta:
        model = info_table
        fields = "__all__"

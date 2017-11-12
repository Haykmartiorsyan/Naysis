from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = True

    class Meta:
        model = Project
        fields = ['projectname', 'email', 'password']



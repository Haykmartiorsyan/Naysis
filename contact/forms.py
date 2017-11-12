from django import forms
from project.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = [""]
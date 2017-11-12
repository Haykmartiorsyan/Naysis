from django import forms
from project.models import PostComment
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        fields = ('name', 'email', 'web_site', 'message')
        model = PostComment

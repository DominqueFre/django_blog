from django import forms
from .models import Collaborate


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = Collaborate
        fields = ('name', 'email', 'message')

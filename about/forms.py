from .models import Collaborate
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = Collaborate
        fields = ('name', 'email', 'message')

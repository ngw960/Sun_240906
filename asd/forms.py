from django import forms
from .models import Panel

class LoginForm(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class PanelForm(forms.ModelForm):
    class Meta:
        model = Panel
        fields = ['capacity', 'location', 'modelNamev', 'manufacturer', 'maintenance', 'quantity', 'size', 'date', 'record', 'cause']



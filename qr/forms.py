# forms.py

from django import forms

class ScanForm(forms.Form):
    isbn = forms.CharField(label='ISBN', required=False)
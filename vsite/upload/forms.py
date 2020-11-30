from django import forms
from .models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    fields = {'docfile','name','category'}



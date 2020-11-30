from django import forms
from .models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='')
    fields = {'docfile','name','category'}



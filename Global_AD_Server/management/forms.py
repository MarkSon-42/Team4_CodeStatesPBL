from django import forms
from .models import MediaTypeInfo, AdInfo

class MediaTypeInfoForm(forms.Form):
    id = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    type = forms.CharField(max_length=45)

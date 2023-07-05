from django import forms
from .models import MediaTypeInfo, AdInfo

class MediaTypeInfoForm(forms.Form):
    id = forms.IntegerField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    type = forms.CharField(max_length=45)
class AdInfoForm(forms.Form):
    media_type = forms.IntegerField()
    name = forms.CharField(max_length=45)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    mod_date = forms.DateTimeField()
    definition = forms.CharField(max_length=500)
    cost = forms.IntegerField()
    advertiser = forms.CharField(max_length=45)
    click_cnt = forms.IntegerField()
    url = forms.CharField(max_length=255)
    content_path = forms.CharField(max_length=255)
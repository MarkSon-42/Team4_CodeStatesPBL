from django.shortcuts import render
from django.views import View
from .models import MediaTypeInfo
from .forms import MediaTypeInfoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class MediaTypeManageView(View):
    def post(self, request):
        response_data = {}
        form = MediaTypeInfoForm(request.POST)
        if form.is_valid():
            mediatype = MediaTypeInfo()
            mediatype.id = form.cleaned_data['id']
            mediatype.width = form.cleaned_data['width']
            mediatype.height = form.cleaned_data['height']
            mediatype.type = form.cleaned_data['type']
            mediatype.save()

            response_data['code'] = "0"
            response_data['msg'] = "OK" 
            return JsonResponse(response_data)
        else:
            response_data['code'] = "9"
            response_data['msg'] = "Form Not Invalied"
            return JsonResponse(response_data)

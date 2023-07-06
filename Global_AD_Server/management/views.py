from django.shortcuts import render
from django.views import View
from .models import MediaTypeInfo, AdInfo
from .forms import MediaTypeInfoForm, AdInfoForm
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
            obj, created = MediaTypeInfo.objects.get_or_create(
                id = form.cleaned_data['id'],
                width = form.cleaned_data['width'],
                height = form.cleaned_data['height'],
                type = form.cleaned_data['type']
            )
            if created:
                mediatype.save()
                response_data['code'] = "0"
                response_data['msg'] = "OK" 
                return JsonResponse(response_data)
            else:
                response_data['code'] = "8"
                response_data['msg'] = "Duplicated Data"
                return JsonResponse(response_data)
        else:
            response_data['code'] = "9"
            response_data['msg'] = "Form Not Invalied"
            return JsonResponse(response_data)

@method_decorator(csrf_exempt, name='dispatch')
class AdManageView(View):
    def post(self, request):
        response_data = {}
        form = AdInfoForm(request.POST)
        if form.is_valid():
            fk = MediaTypeInfo.objects.get(id=form.cleaned_data['media_type'])
            obj, created = AdInfo.objects.get_or_create(
                media_type = fk,
                name = form.cleaned_data['name'],
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
                definition = form.cleaned_data['definition'],
                cost = form.cleaned_data['cost'],
                advertiser = form.cleaned_data['advertiser'],
                mod_date = form.cleaned_data['mod_date'],
                click_cnt = form.cleaned_data['click_cnt'],
                url = form.cleaned_data['url'],
                content_path = form.cleaned_data['content_path']
            )
            if created:
                obj.save()
                response_data['code'] = "0"
                response_data['msg'] = "OK" 
                return JsonResponse(response_data)
            else:
                response_data['code'] = "8"
                response_data['msg'] = "Duplicated Data"
                return JsonResponse(response_data)
        else:
            response_data['code'] = "9"
            response_data['msg'] = "Form Not Invalied"
            return JsonResponse(response_data)
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


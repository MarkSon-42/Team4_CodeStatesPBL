from django.shortcuts import render
from django.core import serializers
# Create your views here.
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from .models import AdInfo


class AdListView(View):
    def get(self, request):
        ads = AdInfo.objects.all() #이 안에 AdInfo테이블안에 모든 튜플을 가져다 놓음
        post_list = serializers.serialize('json', ads) # 그리고 그걸 list 형태로 바꿈 
        responseData = {'data' : post_list}
        return JsonResponse(responseData)
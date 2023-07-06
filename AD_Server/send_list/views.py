from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import *
from django.http import JsonResponse
from django.views import View
import random

# ------ get_client_ip : 클라이언트의 ip를 반환하는 함수 ------
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # request.META 딕셔너리를 사용하여 클라이언트의 IP 주소를 가져옴
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        # IP 주소들은 쉼표로 구분되어 있으므로, 첫 번째 IP 주소만 추출
        # print(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
        # print(ip)

    return ip


# ------process_client_req() : 클라이언트의 요청을 처리하는 함수 ------

def process_client_req(request):
    ip_address = request.META.get('REMOTE_ADDR')
    blocked_ips = Blacklist.objects.values_list('ipaddress', flat=True)
    # Blacklist 모델에서 차단된 IP 주소들을 가져와 blocked_ips 변수에 저장
    responseData = {'data' : post_list}
    if ip_address in blocked_ips:
        return JsonResponse(responseData)
    
    # return HttpResponseForbidden("접근이 차단되었습니다.")
    # 만약 ip_address가 blocked_ips에 포함되어 있다면, 접근이 차단되었다는 403 Forbidden 응답을 반환
    # 접근이 허용된 경우, 원하는 동작을 수행하는 코드 작성
    # ...

def sendAdListView(request):
    response_data = {}
    ip = get_client_ip(request)
    blocked_ips = Blacklist.objects.values_list('ipaddress', flat=True)
    if ip in blocked_ips:
        response_data["code"] = 2
        response_data["msg"] = "Blocked IP Address"
        response_data["data"] = None
        return JsonResponse(response_data)
    ad_list = []
    media_type_main = MediaTypeInfo.objects.get(id=1)
    media_type_sub = MediaTypeInfo.objects.get(id=2)
    ad_list.extend(random.sample(list(AdInfo.objects.filter(media_type=media_type_main)), 1))
    ad_list.extend(random.sample(list(AdInfo.objects.filter(media_type=media_type_sub)),3))
    
    response_data["code"] = 0
    response_data["msg"] = "OK"
    response_data["data"] = [] 
    for a in ad_list:
        result = {}
        selected_fields = ['id', 'media_type_id', 'name', 'definition', 'url', 'content_path']
        for field in selected_fields:
            result[field] = str(getattr(a, field))
        response_data["data"].append(result)
    print(response_data)
    return JsonResponse(response_data)

from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import Blacklist
from django.http import JsonResponse


# ------ get_client_ip : 클라이언트의 ip를 반환하는 함수 ------

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # request.META 딕셔너리를 사용하여 클라이언트의 IP 주소를 가져옴
    
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        # IP 주소들은 쉼표로 구분되어 있으므로, 첫 번째 IP 주소만 추출
        print(ip)
    
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)

    return ip


# ------process_client_req() : 클라이언트의의 요청을 처리하는 함수 ------
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


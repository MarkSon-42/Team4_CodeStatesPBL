from django.shortcuts import render
from django.http import HttpResponseForbidden
from .models import Blacklist

def index(request):
    ip_address = request.META.get('REMOTE_ADDR')
    blocked_ips = Blacklist.objects.values_list('ipaddress', flat=True)
    
    if ip_address in blocked_ips:
        return HttpResponseForbidden("접근이 차단되었습니다.")
    
    # 접근이 허용된 경우, 원하는 동작을 수행하는 코드 작성
    # ...
    
    return render(request, 'index.html')

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'adtest/index.html')

# def webview(request):
#     return render(request, 'adtest/webview.html')
from django.urls import path
from . import views

app_name = 'adtest'
urlpatterns = [
    path('index/', views.index, name="index"),
    # path('index/webview/', views.webview, name="webview"),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('send_ad_list', sendAdListView, name="sendADListView"),
]
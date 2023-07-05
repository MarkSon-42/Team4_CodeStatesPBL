from django.urls import path
from .views import *

urlpatterns = [
    path('mediatype', MediaTypeManageView.as_view(), name="MediaTypeManageView"),
    path('ad', AdManageView.as_view(), name="AdManageView"),
]

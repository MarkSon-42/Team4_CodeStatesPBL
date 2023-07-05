from django.urls import path
from .views import *

urlpatterns = [
    path('', MediaTypeManageView.as_view(), name="MediaTypeManageView"),
]

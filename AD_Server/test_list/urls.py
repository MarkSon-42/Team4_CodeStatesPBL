from django.urls import path
from .views import * 

urlpatterns = [
    path('adlist', AdListView.as_view(), name = "MediaTypeManageView")
]

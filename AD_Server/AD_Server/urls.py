from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('test_list/', include('test_list.urls'))
]



=======
    path('test_list/', include('test_list.urls')),
    path('send_list/', include('send_list.urls')),
]
>>>>>>> origin/eojin-branch

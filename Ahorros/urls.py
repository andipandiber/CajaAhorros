
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('apps.users.urls')),
    re_path('', include('apps.roles.urls')),
    re_path('', include('apps.home.urls')),
]

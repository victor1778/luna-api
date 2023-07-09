from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('api.urls')),
    path('v1/auth/',include('dj_rest_auth.urls')),
    path('v1/auth/registration/', include('dj_rest_auth.registration.urls')),
]

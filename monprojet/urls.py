from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cvapp.urls')),         # Inclus toutes les URLs définies dans cvapp/urls.py
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

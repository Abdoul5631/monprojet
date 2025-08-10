from django.contrib import admin
from django.urls import path, include
from .import views  # Importez les vues de votre application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cvapp.urls')),  # URLs de ton application cvapp
    path('auth/', include('django.contrib.auth.urls')),  # URLs d'authentification
    path('accounts/',include('django.contrib.auth.urls')),#inclure les urls d'authentification
    path('list/', views.cv_list, name='cv_list'),
    path('submit/', views.submit_cv, name='submit_cv'),
    path('success/', views.cv_success, name='cv_success'),
    path('detail/<int:pk>/', views.cv_detail, name='cv_detail'),  # Chemin pour les détails
]
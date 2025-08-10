from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.cv_list, name='home'),  # Page d'accueil
    path('list/', login_required(views.cv_list), name='cv_list'),  # Liste des CVs
    path('submit/', login_required(views.submit_cv), name='submit_cv'),  # Soumettre un CV
    path('success/', login_required(views.cv_success), name='cv_success'),  # Confirmation
    path('detail/<int:pk>/', login_required(views.cv_detail), name='cv_detail'),  # Détails d'un CV
    path('delete/<int:pk>/', login_required(views.cv_delete), name='cv_delete'),  # Suppression d'un CV
    path('edit/<int:pk>/', login_required(views.cv_edit), name='cv_edit'),  # Modification d'un CV
    path('create/', login_required(views.cv_create), name='cv_create'),  # Création d'un nouveau CV
    path('cv-download/<int:pk>/', views.download_cv, name='download_cv'),  # Téléchargement d'un CV
    path('download_all/', login_required(views.download_all_cvs), name='download_all_cvs'),  # Téléchargement de tous les CVs
    path('<int:cv_id>/update/', views.cv_update, name='cv_update'),  # Mise à jour d'un CV
    path('payment/', views.payment, name='payment'),
    path('login/',LoginView.as_view(template_name='cvapp/login.html'), name='login'),  # Utilisation de la vue de connexion de Django
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
]

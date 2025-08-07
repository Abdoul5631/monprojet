from django.contrib import admin
from .models import CV  # Importer le modèle CV

# Enregistrer le modèle dans l'administration Django
@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')  # Colonnes affichées dans l'admin
    search_fields = ('full_name', 'email')  # Permet la recherche par ces champs



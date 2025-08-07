from django.db import models  # Import des modèles de Django
from django.conf import settings  # Pour AUTH_USER_MODEL
from taggit.managers import TaggableManager  # Import pour les tags
from django.contrib.auth.models import AbstractUser  # Pour le modèle utilisateur personnalisé


# Classe pour personnaliser l'utilisateur
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        app_label = 'cvapp'


# Classe pour les CVs
class CV(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Utilisation de AUTH_USER_MODEL pour éviter les problèmes d'import
        on_delete=models.CASCADE,
        related_name="cvs",
        verbose_name="Utilisateur",
        null=False,
        blank=False,
        default=1,  # Remplacez "1" par l'ID d'un utilisateur existant si nécessaire
    )
    full_name = models.CharField(max_length=100, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse e-mail")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Téléphone")
    summary = models.TextField(blank=True, verbose_name="Résumé professionnel")
    skills = models.TextField(blank=True, verbose_name="Compétences")
    experience = models.TextField(blank=True, verbose_name="Expérience professionnelle")
    education = models.TextField(blank=True, verbose_name="Formation académique")
    profession = models.CharField(max_length=100, blank=True, null=True, verbose_name="Profession")
    bio = models.TextField(blank=True, null=True, verbose_name="Biographie")
    linkedin = models.URLField(blank=True, null=True, verbose_name="Lien LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="Lien GitHub")
    address = models.TextField(default="", blank=True, verbose_name="Adresse")
    category = models.CharField(
        max_length=100,
        choices=[("IT", "Informatique"), ("Marketing", "Marketing"), ("Design", "Design"), ("Finance", "Finance")],
        default="IT",
        verbose_name="Catégorie",
    )
    nom = models.CharField(max_length=100)
    portfolio = models.FileField(upload_to='portfolios/', null=True, blank=True)
    tags = TaggableManager(verbose_name="Tags")
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CVs"


# Classe pour le profil de l'utilisateur
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Utilisation du modèle utilisateur personnalisé
        on_delete=models.CASCADE,
        related_name="profile"
    )
    # Vous pouvez ajouter d'autres champs personnalisés ici

    def __str__(self):
        return self.user.username

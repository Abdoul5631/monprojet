import os
from pathlib import Path
import dj_database_url

# Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Sécurité
SECRET_KEY = 'votre-clé-secrète-django-à-générer'
DEBUG = True  # Assurez-vous de mettre `False` en production
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Applications Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',  # Pour la gestion des tags
    'cv',  # Votre application CV
    'cvapp',  # Votre application cvapp
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL principale et configuration WSGI
ROOT_URLCONF = 'cvproject.urls'
WSGI_APPLICATION = 'cvproject.wsgi.application'

# Configuration base de données (SQLite par défaut)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Gestion des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Paramètres linguistiques
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_TZ = True

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Inclure un dossier `static` dans votre projet
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Dossier pour collectstatic en production

# Configuration des fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Paramètres de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Dossier des templates ajouté ici
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',
            ],
        },
    },
]

# Configuration e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ton_email@gmail.com'  # Remplacez par votre adresse email
EMAIL_HOST_PASSWORD = 'ton_mot_de_passe'  # Remplacez par votre mot de passe

# Logs (optionnel, à configurer pour production)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

# Autres configurations spécifiques
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'cvapp.CustomUser'  # Assurez-vous que le modèle CustomUser est bien défini dans cvapp
LOGIN_REDIRECT_URL = '/'  # Redirection après connexion réussie
LOGOUT_REDIRECT_URL = '/'  # Redirection après déconnexion réussie

# Configuration pour l'interface d'administration (si nécessaire)
# Si vous voulez gérer les utilisateurs via l'admin, assurez-vous que l'admin est activé

# Configuration pour Render
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise pour servir les fichiers statiques
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Utilisation de la base de données de Render (si DATABASE_URL existe)
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)



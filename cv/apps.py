from django.apps import AppConfig


class CvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cvproject.cv'

class CvappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cvproject.cvapp'


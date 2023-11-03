from django.apps import AppConfig


class App2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_2'
    verbose_name = "La seconde application"

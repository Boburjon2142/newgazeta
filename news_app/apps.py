from django.apps import AppConfig


class NewsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_app'

    def ready(self):
        # Ensure modeltranslation registers translation options
        from . import translation  # noqa: F401

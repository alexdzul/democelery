from django.apps import AppConfig


class NetworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'democelery.network'

    def ready(self):
        import democelery.network.signals

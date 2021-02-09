from django.apps import AppConfig


class BasicAppConfig(AppConfig):
    name = 'basic_app'

    def ready(self):
        from . import refresher as scheduler
        scheduler.start()

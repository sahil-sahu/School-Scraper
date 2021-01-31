from django.apps import AppConfig


class BasicAppConfig(AppConfig):
    name = 'basic_app'

    def ready(self):
        
        from scheduler import refresher
        refresher.starter()

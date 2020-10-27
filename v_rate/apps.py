from django.apps import AppConfig


class VRateConfig(AppConfig):
    name = 'v_rate'

    def ready(self):
        import v_rate.signals

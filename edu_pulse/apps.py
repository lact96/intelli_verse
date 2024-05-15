# edu_pulse/apps.py
from django.apps import AppConfig

class EduPulseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_pulse'

    def ready(self):
        import edu_pulse.signals

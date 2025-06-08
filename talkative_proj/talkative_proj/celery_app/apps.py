import os
from celery import Celery as _Celery
from django.apps import AppConfig
from django.conf import settings
from kombu import Queue

os.environ.setdefault("DEFAULT_SETTINGS_MODULE", "settings")
app = _Celery(settings.CELERY_APP_NAME)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Add this block for queues
app.conf.task_queues = (
    Queue("celery_talkative_processor"),
)

app.conf.task_routes = {
    "talkative_proj.celery_app.tasks.add": {"queue": "celery_talkative_processor"},
}

class CeleryAppConfig(AppConfig):
    name = 'celery_app'

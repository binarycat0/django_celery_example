from celery.app import Celery

from django.conf import settings

app = Celery('django_celery_example', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    result_backend=settings.CELERY_RESULT_BACKEND,
    beat_scheduler="django_celery_beat.schedulers:DatabaseScheduler",
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
)

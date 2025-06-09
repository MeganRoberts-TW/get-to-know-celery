import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_to_know_celery.settings')

app = Celery('get_to_know_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

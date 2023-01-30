from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_app = Celery("postage")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.conf.beat_schedule = {
    'every_15_seconds': {
        'task': 'mainapp.tasks.send_email_15',
        'schedule': 60,

    }
}
celery_app.autodiscover_tasks()


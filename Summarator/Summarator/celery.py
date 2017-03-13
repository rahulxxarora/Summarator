from __future__ import absolute_import
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Summarator.settings')
    
from django.conf import settings
from celery import Celery
    
celery_app = Celery('Summarator',
    backend='amqp',
    broker='amqp://guest@localhost//')
    
# This reads, e.g., CELERY_ACCEPT_CONTENT = ['json'] from settings.py:
celery_app.config_from_object('django.conf:settings')
    
# For autodiscover_tasks to work, you must define your tasks in a file called 'tasks.py'.
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
    
@celery_app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
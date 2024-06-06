from celery import Celery
from datetime import timedelta
import os
from celery import signals
# from __future__ import absolute_import, unicode_literals


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shop.settings')
celery_app = Celery('Shop')


celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.conf.update(
    worker_log_format="[%(asctime)s] [%(levelname)s] [%(process)d] [%(task_name)s(%(task_id)s)] %(message)s",
    worker_log_color=True,
)
celery_app.autodiscover_tasks()

# """
#     commands :  celery -A Shop worker -l INFO
#     beat commands : celery -A Shop beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
#
# """


# celery_app.autodiscover_tasks()
celery_app.conf.broker_url = 'localhost'
celery_app.conf.result_backend = 'localhost'
# celery_app.conf.task_serializer = 'json'
# celery_app.conf.result_serializer = 'pickle'
# celery_app.conf.accept_content = ['json','pickle']
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 4

from celery import Celery
from datetime import timedelta
# from __future__ import absolute_import, unicode_literals
import os
# from core.logger import logger


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shop.settings')

celery_app = Celery('Shop')

celery_app.config_from_object("Shop.celery_conf", namespace="CELERY")

celery_app.autodiscover_tasks()

# """
#     redis-server
#     commands :  celery -A Shop worker -l INFO
#     beat commands : celery -A Shop beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
#
# """


celery_app.conf.broker_url = 'redis://localhost:6379'
celery_app.conf.result_backend = celery_app.conf.broker_url
celery_app.conf.broker_connection_retry_on_startup = True
celery_app.conf.accept_content = ['json','pickle']
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'json'
CELERY_TIMEZONE = 'Asia/Tehran'
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 4
# celery
# CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
# broker_connection_retry = os.getenv('broker_connection_retry')

# celery_app.conf.update(
#     worker_log_format="[%(asctime)s] [%(levelname)s] [%(process)d] [%(task_name)s(%(task_id)s)] %(message)s",
#     worker_log_color=True,
# )
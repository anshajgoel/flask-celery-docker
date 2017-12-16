from celery import Celery
import os
import requests
import logging
from conf import CeleryConfig

logger = logging.getLogger(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

celery_app = Celery()
celery_app.config_from_object(CeleryConfig)


@celery_app.task(bind=True, max_retries=10)
def celery_task_name(self, json_data, url):
    try:
        # Logic goes here
        return #whatever you want!
    except requests.exceptions.RequestException as e:
        logger.error(e)
        num_retries = celery_task_name.request.retries
        seconds_to_wait = 2.0 ** num_retries

        raise celery_task_name.retry(countdown=seconds_to_wait)

from flask import Flask, request, abort
import os
from .tasks import celery_task_name
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


flask_app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))


@flask_app.route('/my-route', methods=['POST'])
def function_name():
    # Logic goes here!
    celery_task_name.delay()
    return "Sent to celery task!"


@flask_app.route('/health-check', methods=['GET', 'POST'])
def health_check():
    return "OK"


if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=8001)

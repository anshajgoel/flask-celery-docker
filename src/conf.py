import boto3
import logging
import os
import sys
import yaml

logger = logging.getLogger(__name__)

MY_ENV = os.environ.get("MY_ENV", "staging")
IAM = os.environ.get("IAM", False)

src = os.path.dirname(__file__)
config_file = os.path.join(src, os.pardir, "conf", "{}.yaml".format(MY_ENV))

try:
    with open(config_file, 'r') as yaml_file:
        conf = yaml.load(yaml_file)
        logger.info("Opened conf file: %s", yaml_file)
except Exception as exc:
    logger.error("Error opening conf file", exc)
    sys.exit(1)


class CeleryConfig:
    if IAM:
        broker_url = 'sqs://'
    else:
        session = boto3.Session()
        aws_credentials = session.get_credentials()
        broker_url = 'sqs://{aws_access_key_id}:{aws_secret_access_key}@'.format(
            aws_access_key_id="WHATAREYOUSEARCHINGFORMRHACKER!",
            aws_secret_access_key="WHATAREYOUSEARCHINGFORMRHACKER!")
    broker_transport_options = {
        "region": "us-east-1",
        "polling_interval": 20,
        "queue_name_prefix": "sqs-queue-name-{env}-".format(env=MY_ENV)
    }

import logging

import boto3
from botocore.exceptions import ClientError
import json

logger = logging.getLogger("app")
def fetch_secrets_from_secret_manager(secret_name, region_name):
    logger.debug(f"Entry log fetch_secrets_from_secret_manager")
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as ex:
        logger.error(f"Error caused while fetching secrets from secretsmanager. Error={ex}")
        raise ex

    vendor_config = json.loads(get_secret_value_response['SecretString'])
    logger.debug("Exit log fetch_secrets_from_secret_manager")
    return vendor_config
import logging

from django.views.decorators.csrf import csrf_exempt
logger = logging.getLogger("apps")
@csrf_exempt
def upload_file():
    print("hello")
    logger.info("Hi this is a log message in upload_file")
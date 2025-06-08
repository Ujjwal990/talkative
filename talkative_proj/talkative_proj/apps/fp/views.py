import logging

from django.views.decorators.csrf import csrf_exempt
logger = logging.getLogger("apps")


@csrf_exempt
def start_file_processing_async():
    print("hello")
    logger.info("Hi this is a log message in upload_file")
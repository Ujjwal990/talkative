from celery import shared_task
import logging
logger = logging.getLogger("apps")

@shared_task
def add(x=5, y=6):
    try:
        z = x + y
        print(f"value of z is: {z}")  # Good for testing
        logger.info(f"value of z is: {z}")  # Changed to info (not error, since it's not an error)
        return z  # Recommended: return the result
    except Exception as ex:
        print(f"Exception: {ex}")
        logger.error(f"Exception in add task: {ex}")
        raise  # Important: re-raise so Celery can mark it as failed

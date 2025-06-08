from celery import shared_task
import logging
logger = logging.getLogger("apps")

@shared_task()
def add(x=5,y=6):
    z=0
    try:
        z = x+y
        print(f'value of z is : {z}')
        logger.info(f'value of z is : {z}')
    except Exception as ex:
        print(f"{ex}")
        logger.error(f"{ex}")

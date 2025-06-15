import logging
import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from talkative_proj.db_models.generic_model import TKTgenericModel
from talkative_proj.db_models.comment_model import TKTcommentModel
logger = logging.getLogger("apps")


@csrf_exempt
def ping(request):
    print("ping success")
    logger.info("ping success")
    # return HttpResponse("ping success")
    return HttpResponse(json.dumps(dict(ping="success")))

@csrf_exempt
def db_ping(request):
    try:
        table_obj = TKTcommentModel()
        resp = table_obj.get_complete_table()
        print(resp)
        logger.info(resp)
        return HttpResponse(json.dumps(dict(ping="success")))
    except Exception as ex:
        return HttpResponse(json.dumps(dict(ping="Failed", error=str(ex))))

@csrf_exempt
def celery_ping(request):
    from talkative_proj.celery_app.tasks import add
    add.apply_async(kwargs={'y':5, 'x':4}, queue="celery_talkative_processor")
    # add.apply_async(kwargs={'y':5, 'x':4})
    return HttpResponse("Pinging")
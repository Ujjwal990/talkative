import os
import sys
from os.path import dirname

proj_name = "talkative_proj"
root_path = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, proj_name)))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, proj_name, proj_name)))
sys.path.insert(0, os.path.abspath(os.path.join(root_path, proj_name, proj_name, 'apps')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talkative_proj.settings")
from talkative_proj.celery_app.apps import app as celery_app

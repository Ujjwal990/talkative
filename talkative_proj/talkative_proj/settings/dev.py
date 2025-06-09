import os

print("inside dev file")
from .base import *

localhost = '127.0.0.1'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

VENDOR_NAME = os.environ.get("VENDOR_NAME", "ParmarSsc")

DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "parmarssc",
                "USER": "root",
                "PASSWORD": "12345678",
                "HOST": "localhost",  # "isme aws ka link aana chahiye where db is hosted",
                "PORT": "3306"
            }
        }

VENDOR_CONF = {
    "ParmarSsc": {
        "DATABASE": {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "parmarssc",
                "USER": "root",
                "PASSWORD": "12345678",
                "HOST": "localhost",  # "isme aws ka link aana chahiye where db is hosted",
                "PORT": "3306"
            }
        },
        "AWS": {
            'ACCESS_KEY': '',
            'SECRET_KEY': '',
            "REGION": ''
        },
        "CELERY": {
            "BROKER_URL": f'redis://{localhost}:6378/12',
            "BROKER_TRANSPORT_OPTIONS": {'visibility_timeout': 3600},
            "CELERY_BROKER_URL": "redis://%s:6379/12" % f'{localhost}',
            "CELERY_RESULT_BACKEND": "redis://%s:6379/12" % f'{localhost}'
        },
        "ENCRYPTION": {
            "FILE_AES": {
                "KEY": "qpPhgFYSpRong7IQysDxhDUVdcLfTSUp",
                "IV": "E2jL6XnyFatLH5nj",
            },
            "DATABASE_AES": {
                "KEY": "9YUnM0C1RLQOsNeqE5NU7qbbzCbjx6Nl",
                "IV": "yHgkiQYnaL8ycXlk",
            }
        },
        "BUCKET": "parmar_ssc_1"
    }
}
VENDOR_CONFIG = VENDOR_CONF[VENDOR_NAME]
DATABASES.update(VENDOR_CONFIG['DATABASE'])

ROOT_URLCONF = 'talkative_proj.urls'


# *************************** CELERY CONFIGURATION **********************
BROKER_URL = f"redis://localhost:6379/0"
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout':3600, 'priority_steps': list(range(10))}
CELERY_BROKER_URL = f"redis://localhost:6379/0"
CELERY_RESULT_BACKEND = f"redis://localhost:6379/0"
# *************************** END CELERY CONFIGURATION **********************
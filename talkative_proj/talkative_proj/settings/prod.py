print("inside prod file")
localhost='127.0.0.1'

VENDOR_CONF = {
    "ParmarSsc": {
        "DATABASE": {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "parmarssc",
                "USER": "parmarsscdbuat",
                "PASSWORD": "parmar@123",
                # "HOST": "isme aws ka link aana chahiye where db is hosted",
                "HOST": "localhost",
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

ROOT_URLCONF = 'talkative_proj.urls'
from sqlalchemy import create_engine

from django.conf import settings
from urllib.parse import quote

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SqlAlchemyEngine(object, metaclass=Singleton):

    def __init__(self):
        self.engines= {}

    def get_connection(self, database):
        if database not in self.engines:
            engine = create_engine(
                f"mysql+pymysql://{settings.DATABASES[database]['USER']}:%s@"
                f"{settings.DATABASES[database]['HOST']}:{settings.DATABASES[database]['PORT']}/{settings.DATABASES[database]['NAME']}"% quote(f"{settings.DATABASES[database]['PASSWORD']}"),
                echo=False, pool_size=10, max_overflow=20, pool_pre_ping=True, pool_recycle=3600)
            self.engines[database] = engine
        return self.engines[database]
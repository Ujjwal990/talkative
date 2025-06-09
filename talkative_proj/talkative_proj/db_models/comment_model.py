from talkative_proj.utils.database_utils import *
import logging
from django.conf import settings
from talkative_proj.utils.sql_alchemy_engine import SqlAlchemyEngine

logger = logging.getLogger("apps")

class TKTcommentModel:
    def __init__(self):
        self.database = list(settings.VENDOR_CONF.get("ParmarSsc").get("DATABASE", []))[0]
        self.table_name = "comment"
        self.table_columns = ["comment_id", "stream_id", "account_id", "comment_text", "comment_time", "parent_comment_id"]
        self.curr = SqlAlchemyEngine().get_connection(self.database)

    def insert(self, records=None, params={}, table_name=None):
        if table_name is None or params.get("custom_columns") is None:
            return {"success": False, "error_resource": "class"}
        columns = params.get("custom_columns")
        values = records or [[]]
        try:
            resp = insert_multiple_rows(self.curr, table_name, data_dict={'columns': columns, 'values': values})
            return resp
        except Exception as ex:
            logger.error(f"Insert operation Failure. Ex={ex}")
            return {"success":False, "error_resource":"db", "error":ex}


    def get_complete_table(self):
        try:
            query = f'select * from {self.table_name}'
            result = fetch_all(self.curr, query)
            return result
        except Exception as ex:
            return ex

from django.db import connections, transaction
import time
import logging
from sqlalchemy import text

def mysql_connect(database):
    curr = connections[database].cursor()
    return curr

def fetch_all(engine, query, params=[]):
    try:
        with engine.connect() as cursor:
            resp = cursor.execute(query, params)
            desc = resp.cursor.description
            result = [dict(zip([col[0] for col in desc], row)) for row in resp.fetchall()]
            return result
    except Exception as ex:
        logging.error(f"Error occurred in fetch_all. error={ex}")
        return ex

def insert_multiple_rows(engine, table_name, data_dict):
    placeholder = ', '.join(['%s'] * len(data_dict["columns"]))
    columns = ', '.join(data_dict["columns"])
    query = "INSERT into %s ( %s ) VALUES ( %s )" % (table_name, columns, placeholder)
    try:
        with engine.connect() as cursor:
            resp = cursor.execute(query, data_dict["values"])
            return {'success': True, 'last_row_id': resp.lastrowid, 'row_count': resp.rowcount}
    except Exception as ex:
        logging.error(f"Error occurred while inserting data into mysql table, ex={ex}")
        raise ex
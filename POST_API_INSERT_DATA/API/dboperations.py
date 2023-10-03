from django.db import connection
from rest_framework.response import Response

def dbop_insert_data(id_param):
    try:
        with connection.cursor() as cursor:
            cursor.callproc('udf_insert_progress_bar_type_and_children',[id_param])
        return {"success" : True, "message": "Data inserted successfully."}
    except Exception as e:
        return {"success" : False, "message" : str(e)}

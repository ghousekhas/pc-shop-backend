from django.db import connection
from rest_framework.response import Response

cursor = connection.cursor() #type: Cursor

def insert_query(query):
    return cursor.execute(query)

def run_basic_query(query):
    cursor.execute(query)
    return ({
        "desc": [desc[0] for desc in cursor.description],
        "result": list(cursor)
    })

def runquery(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = [dict(zip([desc[0] for desc in cursor.description],row)) for row in list(cursor)]
    return Response(result)


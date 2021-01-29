from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from django.db import connection

@api_view(['GET','POST','PATCH','PUT'])
def add_product(request  #type: Request
     ):
    if request.method == 'POST':
        data = request.data
        cursor = connection.cursor()
        cursor.execute('insert into product(model_number,')
        return Response({
            "Successful": "Success"
        })

from rest_framework.decorators import api_view
from django.db import connection
from rest_framework.request import Request
from rest_framework.response import Response

@api_view(['GET'])
def compare_orders(req  #type: Request
                   ):
    cu = connection.cursor()
    if req.method == 'GET':
        data = req.data
        try:
            user_id = data['user_id']
            order_ids = data['order_ids'] #type: list
            results = []
            for order_id in order_ids:
                cu.execute('select * from order where order_id = %s',[order_id])
                results.append(dict(zip(cu.description,[item for item in list(cu)])))
            return Response({
                "success": results
            })
        except Exception as some_exception:
            return Response({
                "error": str(some_exception)
            })
    return Response({
        "error": "Only get requests here"
    })

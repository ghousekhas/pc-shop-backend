import json

from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from utility.runquery import run_basic_query as rq
from sqlite3 import connect
import logging


success = 'success'

@api_view(['GET'])
def get_products(request #type: Request
                 ):
    # cursor = connection.cursor() #type: Cursor
    # res = cursor.execute('select * from user')
    # logging.error(res.fetchone())

    if request.method == 'GET':
        data = request.query_params
        type = str(data['type']).lower()
        if 'compatible' in data:
            compatible_with = data['compatible']
        else:
            compatible_with = []
        query = ''
        if len(compatible_with) == 0:
            result = rq(f'select * from {type+"_view"}')
            json_result = [dict(zip([desc for desc in result['desc']], [indi for indi in row])) for row in result['result']]
            return Response({
                #"response": result,
                "response1": json_result
            })
        else:
            result = rq(f'select * from \"{type+"_view"}\" right join compatiblity on  where ')




class GetProducts(TemplateView):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GetProducts, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        cursor = connection.cursor();
        params = request.GET
        product_type = params['type']
        query = ''
        try:
            if product_type.lower() == "cpu":
                query =(f'select * from cpuview')
            elif product_type.lower() == "gpu":
                query =(f'select * from gpuview')
            elif product_type.lower() == "ram":
                query = f'select * from ramview'
            cursor.execute(query)
            result_list = list(cursor)
            result = [dict(zip([desc[0] for desc in cursor.description], row)) for row in result_list]
            return JsonResponse(
                {
                    # "description": desc,
                    "products": result
                }
            )
        except Exception as e:
            print(e.message)
            return JsonResponse({
                "status": "error",
                "error": e.message
            })





        return JsonResponse({
            "num": len(request.GET)
        })

    def post(self, request, *args, **kwargs):

        def prepare_token(email, password):
            return "abc"

        print('balalala')
        print(json.loads(request.body))
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        cursor = connection.cursor()
        cursor.execute(f'select password from \"user\" where \"username\" like \"{email}\"')
        listy = cursor.fetchall()
        if (len(listy) == 0):
            return JsonResponse({
                "status": "faliure"
            })
        else:
            print(listy[0][0])
            print(password)
            if str(listy[0][0]) == password:
                token = "nigger"
                return JsonResponse({
                    "status": 6,
                    "email": email,
                    "token": token
                })

        return JsonResponse({
            'meh': 'hemmm'
        })
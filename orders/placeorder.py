from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.manager import Manager
from django.db import connection, models
from django.http import JsonResponse
from django.http import HttpRequest
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.http import request
import json
import logging as l
import json
from accounts.models import Document

from enum import Enum, auto

success = 'success'

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def place_order(request):
    if request.method == "POST":
        data = request.data
        try:
            if data['action'] == 'getAllOrders':
                cursor = connection.cursor()
                cursor.execute("""select * from all_orders """)
                result = [dict(zip([desc[0] for desc in cursor.description], row)) for row in list(cursor)]
                return Response({
                    "response": result
                })
            if data['action'] == 'getOrders':
                cursor = connection.cursor()
                cursor.execute("""select * from all_orders where user_id = %s""",(data['user_id']))
                result = [dict(zip([desc[0] for desc in cursor.description], row)) for row in list(cursor)]

                return Response({
                    "response": result
                })
        except Exception as errr:
            l.error(errr)
            print('something')
        user_id = data['user_id']
        amount = data['amount']
        parts = eval(data['parts'])
        cursor = connection.cursor()
        cursor.execute("""insert into pc_order(user_id,order_date,expected_deliv_date,order_status,address,amount)
            values (
            %s,CURDATE(),\"2021-1-10\",%s,%s,%s)
        """,(
            user_id,
            'pending',
            '1',
            amount
        ))
        order_id = cursor.lastrowid
        for i in parts:
            cursor.execute("""insert into order_part (order_id,product_id,quantity,amount) 
            values (%s,%s,1,%s)""",(order_id,i['id'],i['amount']))
        return Response({
            "id": cursor.lastrowid

        })



class PlaceOrder(TemplateView):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(PlaceOrder, self).dispatch(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        cursor = connection.cursor()
        data = request.POST
        l.error(data['username'])
        username = data['username']
        order_date = data['order_date']
        expected_deliv_date = data['expected_deliv_date']
        status = data['status']
        address = data['address']
        score = data['score']
        amount = data['amount']

        cursor.execute(f'insert into "order" (username,order_date,expected_deliv_date,status,address,score,amount) values(\"{username}\",\"{order_date}\",\"{expected_deliv_date}\",\"{status}\",{address},{score},{amount})')

        return JsonResponse(
            {
                "status": "ok added"
            }
        )
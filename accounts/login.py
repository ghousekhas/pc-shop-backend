from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from utility.runquery import runquery,run_basic_query
from logging import error as e
import json
from django.db import connection
import random
from selenium import webdriver
from rest_framework.views import APIView

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def login(request # type: Request
                ):

    if request.method == 'GET':
        cursor = connection.cursor();
        with open("jayson.json") as json_file:
            json_data = json.load(json_file)
            datae = json_data["data"]
            e(datae)
            numb = 1
            for datie in datae:
                try:
                    cursor.execute("""INSERT INTO product
                                    (
                                    `model_num`,
                                    `name`,
                                    `description`,
                                    `price`,
                                    `status`
                                    ) 
                                    VALUES (%s,%s,%s,%s,%s)""",
                                   [datie['Model'],
                                    datie['Model'],
                                    'CPU',
                                    str(random.randint(10000,50000)),
                                    1
                                    ])
                    cursor.execute(""" INSERT INTO `pc_maker`.`cpu`
                                            (`id`,
                                            `base_clock`,
                                            `boost_clock`,
                                            `cores`,
                                            `threads`,
                                            `L1_cache`,
                                            `L2_cache`,
                                            `L3_cache`,
                                            `unlocked`,
                                            `socket`,
                                            `passmark`)
                                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                   [
                                       cursor.lastrowid,
                                       datie['Max Boost'],
                                       datie['Base Clock'],
                                       datie['# of CPU Cores'],
                                       datie['# of Threads'],
                                       datie['Total L1 Cache'],
                                       datie['Total L2 Cache'],
                                       datie['Total L3 Cache'],
                                       'True',
                                       1,
                                       random.randint(40000,100000)



                                   ])
                except Exception as ioj:
                    print('oij')






        return Response({
            "something": "somethingwe",
            "data": datae
        })
    elif request.method == 'POST':
        data = request.data
        try:
            email = data['email']
            password = data['password']
            e(password)
            result = run_basic_query(f'select * from user where username like \"{email}\"')
            e(result)
            dickt = dict(zip(result['desc'], result['result'][0]))
            e(password)
            real_password = dickt['u_password']
            if password == real_password:
                e('itsthesame')
                dickt['status'] = "success";
                user_id = dickt['id']
                e(user_id)
                cursor = connection.cursor()
                cursor.execute('select * from admin_table where id = %s',(str(user_id)))
                if(cursor.rowcount == 1):
                    dickt['admin']  = True
                return Response(
                    dickt

                )
            else:
                Response({
                    "status": "Unsuccessful"
                })
        except Exception as err:
            e(err)
            return Response({

                "error": "Bad request "
            })

        return Response(
            {
                "status": "Faliure",
                "reason": "Wrong password has been entered"
            }
        )


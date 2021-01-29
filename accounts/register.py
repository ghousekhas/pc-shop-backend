from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from utility.runquery import run_basic_query as be, runquery as re, insert_query as iq
from logging import error as e, debug as deb
from django.db import connection


@api_view(['GET', 'POST'])
def register(request  # type: Request
             ):
    cursor = connection.cursor()
    if request.method == 'POST':
        data = request.data  # type: dict
        quer_str = ' '
        try:
            action = data['action']
            email = data['email']

            def verify_existance():
                q_result = be(f'select count(*) from user where email = \"{email}\" ')
                e(q_result['result'][0][0])
                num = q_result['result'][0][0]
                return num == 0

            if action == 'register':
                password = data['password']
                first_name = data['first_name']
                middle_name = data['middle_name']
                last_name = data['last_name']
                if verify_existance():
                    try:
                        cursor.execute("""insert into user (email,u_password,first_name,middle_name,last_name)
                                      values ( %s, %s, %s, %s, %s )""", (
                        email,
                        password,
                        first_name,
                        middle_name,
                        last_name
                        ))
                        q_result = cursor.execute(f'select * from user where id =  (select max(id) from user)')


                        return Response({
                            "result": cursor.lastrowidd,
                            "status": "Successful",
                            "with": dict(
                                zip([desc[0] for desc in cursor.description], [item for item in list(cursor)[0]]))
                        })
                    except Exception as excepp:
                        return Response({
                            "oisdj": "osdhjios",
                            "error": str(excepp)
                        })
                else:
                    return Response({
                        "error": "User already exists, use forgot password or update credentials"
                    })

            elif action == 'update':
                if not verify_existance():

                    try:
                        quer_str = ' '
                        datacpy = dict(data)
                        del datacpy['email']
                        del datacpy['action']
                        # del datacpy['image']
                        for desc in datacpy.keys():
                            print(desc)
                            quer_str += str(desc) + ' = \"' + str(datacpy[desc][0]) + '\"' + ', '
                        quer_str = quer_str[:-2] + ' '
                        print(quer_str)
                        q_res = iq(f'update \"user\" set {quer_str} where \"username\" like \"{email}\"')
                        return Response({"result": "Updated successfully",
                                         "row": q_res.lastrowid
                                         })
                    except Exception as excep:
                        e(excep)


        except Exception as excep:
            e(excep)
            return Response({
                "error": "Error in the fields given"
            })

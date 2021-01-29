import logging as l
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
import json
err = l.error


success = 'success'


class CreatePost(views.APIView):



    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request,*args,**kwargs):
        req_cpy = request.data

        l.error(req_cpy)
        fileName = "bleh"
        def handle_upload_file(f):
            with open(f"productimages/{fileName}.png","wb") as destination:
                print("Trying to write at least")
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()


        if 'image' in req_cpy:
            image = req_cpy['image']
            handle_upload_file(image)
        print(request.GET)

        body = req_cpy
        data = req_cpy
        #




        #handle_upload_file(image)



        def prepare_token(email, password):
            return "abc"

        #print(json.loads(request.body))

        email = data['email']
        password = data['password']
        cursor = connection.cursor()
        cursor.execute(f'select password from \"user\" where \"username\" like \"{email}\"')
        listy = cursor.fetchall()
        if(len(listy) == 0):
            return JsonResponse({
                "status": "failure",
                "reason": "No account exists with this email ID"
            })
        else:
            print(listy[0][0])
            print(password)
            if str(listy[0][0]) == password:
                token = "nigger"
                return JsonResponse({
                    "status": "successfully logged in",
                    "email": email,
                    "token": token
                })
            

        return JsonResponse({
            "status": "failure",
            "reason": "password wrong"
        })
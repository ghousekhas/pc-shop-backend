from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.manager import Manager
from django.db import connection
from django.http import JsonResponse

# Create your views here.
def login_view(request):
    cursor = connection.cursor()
    #cursor.execute('insert into somename values("mohdrayansailani21@gmail.com","IhateSkins")')
    #somet =cursor.execute('select * from somename where password = "IhateSkins"')
    print("Something big is happening")
    print("something is bugging me")
    result_list = []
    #print(cursor.fetchall())
    #list = [list[0] for list in cursor.fetchall()]
    #print(list)
    #print(result_list)

    return JsonResponse({
        'name': 'miya',
        'profession': 'khalifa'
    }
    )
    
    return HttpResponse("Bruhhh")
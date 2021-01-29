from django.urls import path, include
from django.views import View
from . import views
from accounts.login import login
from accounts.register import register
from accounts.postrequest import CreatePost
urlpatterns = [
    path('login', login, name = 'login'),
    path('register', register, name = 'login')
    

]
from django.urls import path

from api.views.auth_views import *


app_name = 'auth'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login),
    path('logout/', logout),
    path('forget/', forget),
    path('forget/reset/', forget_rest),
]

from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('hruthi/',hruthi,name='hruthi'),
    path('chinna/',chinna,name='chinna'),
]
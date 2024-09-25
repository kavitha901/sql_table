from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_country(request):
    cn=input('enter name')
    CO=Country.objects.get_or_create(cname=cn)
    if CO[1]:
        return HttpResponse('country is created')
    else:
        return HttpResponse('data is already exists')

def insert_capital(request):
    cn=input('enter name')
    cp=input('enter pop')
    cpn=input('enter capital')
    CO=Country.objects.get_or_create(cname=cn)[0]
    CP=Capital.objects.get_or_create(cname=CO,cappop=cp,capname=cpn)
    if CP[1]:
        return HttpResponse('country is created')
    else:
        return HttpResponse('data is already exists')

    




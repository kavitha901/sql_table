from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_country(request):
    cn=input('enter name')
    CO=Country.objects.get_or_create(cname=cn)
    d={'countries':Country.objects.all()}
    if CO[1]:
        return render(request,'ctry.html',d)
        #return HttpResponse('country is created')
    else:
        return HttpResponse('data is already exists')

def insert_capital(request):
    cn=input('enter name')
    cp=input('enter pop')
    cpn=input('enter capital')
    d={'capitals':Capital.objects.all()}
    CO=Country.objects.get_or_create(cname=cn)[0]
    CP=Capital.objects.get_or_create(cname=CO,cappop=cp,capname=cpn)
    if CP[1]:
        return render(request,'cpt.html',d)
        #return HttpResponse('country is created')
    else:
        return HttpResponse('data is already exists')
    
def insert_ct(request):
    cn=input('enter name')
    cp=input('enter pop')
    cpn=input('enter capital')
    COBJ=Country.objects.filter(cname=cn)
    if COBJ:
        CO=COBJ[0]
        Capital.objects.get_or_create(cname=CO,cappop=cp,capname=cp)
        return HttpResponse('contry is created')
    else:
        return HttpResponse('data is not available')

def ctry(request):
    countries=Country.objects.all()
    d={'countries':countries}
    return render(request,'ctry.html',d)
    
def cpt(request):
    d={'capitals':Capital.objects.all()}
    return render(request,'cpt.html',d)

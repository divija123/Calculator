from django.shortcuts import render
from django.http import HttpResponse
def calc(requests):
    field1=int(requests.GET['field1'])
    field2=int(requests.GET['field2'])
    operation=requests.GET['optradio']
    result=0
    if operation=='+':
        result=field1+field2
    if operation=="-":
        result=field1-field2
    if operation=='/':
        result=field1/field2
    if operation=='*':
        result=field1*field2
    return render(requests,"calc/calc.html",{'result':result})
def home(requests):
    return render(requests,"calc/home.html")


     
    

# Create your views here.

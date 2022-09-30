from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import mysql.connector as sql

na=''
em=''
nm=''
me=''
# Create your views here.
def category(request):
    return render(request, 'category.html')

def female(request):
    return render(request, 'female.html')

def index(request):
    global na,em,nm,me
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="tanu@123",database='contact')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                na=value
            if key=="email":
                em=value
            if key=="number":
                nm=value
            if key=="message":
                me=value
            
        
        c="insert into pesonal Values('{}','{}','{}','{}')".format(na,em,nm,me)
        cursor.execute(c)
        m.commit()

    return render(request,'index.html')

def kids(request):
    return render(request, 'kids.html')

def men(request):
    return render(request, 'men.html')

def sign(request):
    return render(request, 'sign.html')
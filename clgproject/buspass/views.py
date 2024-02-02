from unittest import result
from django.shortcuts import render,redirect
from urllib import request
from django.http import HttpResponse
import mysql.connector
from .models import bus
def home(request):
    return render(request,'home.html')
def registration(request):
    if request.method =="POST":
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="buspassmanagement"
        )
        mycursor=mydb.cursor()
        name=request.POST['name']
        fathername=request.POST['fathername']
        dob=request.POST['dob']
        gender=request.POST['gender']
        aadharnumber=request.POST['aadharnumber']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        mobilenumber=request.POST['mobilenumber']
        address=request.POST['address']
        mycursor.execute("insert into userdetails(name,fathername,dob,gender,aadharnumber,username,password,email,mobilenumber,address)values('"+name+"','"+fathername+"','"+dob+"','"+gender+"','"+aadharnumber+"','"+username+"','"+password+"','"+email+"','"+mobilenumber+"','"+address+"')")
        mydb.commit()
        return redirect('login')
    else:
        return render(request,'registration.html')
def login(request):
    if request.method=="POST":
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="buspassmanagement"
        )
        mycursor=mydb.cursor()
        username=request.POST['username']
        password=request.POST['password']
        mycursor.execute("select * from userdetails where username='"+username+"'and password='"+password+"'")
        result=mycursor.fetchone()
        if result!=None:
            return redirect('routeinfo')
        else:
            return render(request,'login.html',{'status':'Invalid credentials'})
    else:
        return render(request,'login.html')
    
def contactus(request):
    return render(request,'contactus.html')
def  routeinfo(request):
    if(request.method=="POST"):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="buspassmanagement"
        )    
        mycursor = mydb.cursor()
        s=request.POST['from']
        d=request.POST['to']
        print("select * from routedetails where source='"+s+"' and destination='"+d+"'")
        mycursor.execute("select * from routedetails where source='"+s+"' and destination='"+d+"'")
        result=mycursor.fetchall()
        routedetails=[]
        for x in result:
            Bus=bus()
            Bus.routeid=x[0]
            Bus.source=x[1]
            Bus.destination=x[2]
            Bus.duration=x[3]
            Bus.amount=x[4]
            routedetails.append(Bus)
        return render(request,'routeinfo.html',{'routes':routedetails})
    else:   
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="buspassmanagement"
        )    
        mycursor = mydb.cursor()
        mycursor.execute("select * from routedetails")
        result=mycursor.fetchall()
        routedetails=[]
        for x in result:
            Bus=bus()
            Bus.routeid=x[0]
            Bus.source=x[1]
            Bus.destination=x[2]
            Bus.duration=x[3]
            Bus.amount=x[4]
            routedetails.append(Bus)
        return render(request,'routeinfo.html',{'routes':routedetails})

def payment(request):
    return render(request,'payment.html')


# Create your views here.

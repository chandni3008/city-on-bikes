from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import ImageForm
from django.db import IntegrityError
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import sys
import re


def index(request):
    if request.method=='POST':
        con = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        con.name = name
        con.email = email
        con.subject = subject
        con.message = message
        con.save()
        return redirect('index')
    else:
        return render(request,'index.html',{})

def password_checker(password):
    msg=[]
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    #     length
    correct_length = len(password) >=   8
    if not correct_length:
        msg.append("Invalid password: too short")
    #     digit
    su = sum(1 for character in password if character.isdigit())
    sufficient_digits = su >= 2
    if not sufficient_digits:
        msg.append("Must have at least 2 digits")
    #     Upper/Lower
    letters = set(password)
    lower = any(letter.islower() for letter in letters)
    upper = any(letter.isupper() for letter in letters)
    if not upper:
        msg.append("No uppercase characters detected")
    if not lower:
        msg.append("No lowercase characters detected")
    #     special char
    if (regex.search(password) == None ):
        msg.append("Must contain atleast one special symbol.")
    else:
        print("Congratulations! This password is valid")
    return msg

def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
      
        post=Register()
        contact = request.POST.get('contact')
        post.username = username
        post.contact = contact
        lis = password_checker(password) 

        if (password != confirm_password):
            messages.info(request,'Password does not match.')
            return redirect('register')
        elif (len(lis) != 0  ):
            for i in lis:
                messages.info(request,i)
            return redirect('register')
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            post.save()
            messages.success(request,"Your account is created")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Successfully registered")
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":            
        username = request.POST['username'] 
        password = request.POST['password'] 
       
        user = auth.authenticate(username = username, password = password) 
       
        if user is not None: 
            auth_login(request,user)
            return redirect('bookride') 
        else: 
            messages.error(request,"Username or Password is Invalid.")
            return redirect("login")
    else:
        return render(request,'login.html')

def bookride(request):
    if request.method=='POST':
        pickup=request.POST['pickup']
        dropat=request.POST['dropat']
        kilo=request.POST['kilo']
        pickdate=request.POST['pickdate']
        picktime=request.POST['picktime']
        dropdate=request.POST['dropdate']
        droptime=request.POST['droptime']

        muser=Bike()
        muser.pickup=pickup
        muser.dropat=dropat
        muser.kilo=kilo
        muser.pickdate=pickdate
        muser.picktime=picktime
        muser.dropdate=dropdate
        muser.droptime=droptime
        muser.save()
        return redirect('bikes')
    else:
        return render(request,'bookride.html',{})

def bikes(request):
    bookride = Bookride.objects.all()
    context={
    'bookride' :bookride
    }
    return render(request, 'bikes.html',context)

def fare(request,pk):
    context={}
    if request.method=='POST':
        form =ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=ImageForm()
    try:
        km = Bike.objects.latest()
        pick = Bike.objects.latest()
        drop = Bike.objects.latest()
        bookride = Bookride.objects.get(pk=pk)
        context={
            'kilometer':km,
            'pick':pick,
            'drop':drop,
            'bookride' : bookride
        }
    except:
        pass
    return render(request,'fare.html',context)



def userlogout(request):
    logout(request)
    messages.success(request, 'Succesfully Logged Out')
    return redirect('index')
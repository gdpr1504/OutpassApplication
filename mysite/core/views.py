from django.contrib.auth import login, authenticate
from mysite.core.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import json
from django.http.request import QueryDict
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
p={}
t=''
l=''
k={}
j=''
oid=''
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def help(request):
    count = User.objects.count()
    return render(request, 'help.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            data=request.POST.copy()
            ausername=str(form.cleaned_data.get('username'))
            apassword=str(form.cleaned_data.get('password1'))
            aname=str(form.cleaned_data.get('first_name'))
            adept=str(form.cleaned_data.get('Department'))
            aemail=str(form.cleaned_data.get('email'))
            aphone=str(form.cleaned_data.get('phone_number'))
            data={"ausername":ausername,"apassword":apassword,"aname":aname,"adept":adept,"aemail":aemail,"aphone":aphone}
            resp=requests.post('https://outpassapp.herokuapp.com/adminregister', data)
            message=resp.json()
            if(message['message']=="Admin of given dept already exists"):
                return render(request,'registration/signup.html',{'form':form,'message':message})
            else:
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def signup1(request):
    return render(request,'registration/helloworld.html')
def home1(request):
    if (request.method)=="POST":
        ausername=request.POST['Username']
        apassword =request.POST['pwd']
        det = { "ausername":ausername,"apassword":apassword}
        token = requests.post("https://outpassapp.herokuapp.com/adminlogin",det)
        global p
        p=token.json()
        if(len(p)!=1):
            global l
            l=token.json()['access_token']
            global t
            t=p['adept']
            global j
            return render(request,'registration/helloworld.html',{'values':p})
        else:
            return render(request,'registration/login.html',{'data':p})    
def homepage(request):
        return render(request,'registration/login.html',{'data':p})
@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'
def login_successful(request):
    data={"adept":t}
    users={"ausername":j}
    outpassrequests=requests.get('https://outpassapp.herokuapp.com/outpassrequests',data,headers = {'Authorization':f'Bearer {l}'})
    k=outpassrequests.json()
    return render(request,'registration/login1.html',{'values1':k,'values':p})
def outpasses(request):
        global srollno
        srollno=request.GET.get('rollnumber')
        global oid
        oid=request.GET.get('oid')
        data={"srollno":srollno}
        data2={"oid":oid}
        det=requests.get('https://outpassapp.herokuapp.com/studentdetails',data,headers = {'Authorization':f'Bearer {l}'})
        ro=requests.get('https://outpassapp.herokuapp.com/getpendingnoofpassesleft',data,headers = {'Authorization':f'Bearer {l}'})
        cal=requests.get('https://outpassapp.herokuapp.com/getpasseshistory',data,headers = {'Authorization':f'Bearer {l}'})
        det2=requests.get('https://outpassapp.herokuapp.com/outpassdetails',data2,headers = {'Authorization':f'Bearer {l}'})
        roo=ro.json()
        det1=det.json()
        cal1=cal.json()
        deta2=det2.json()
        date={}
        month={}
        year={}
        for i in range(len(cal1)):
            wo=cal1[i]
            wo1=wo['odate']
            date[i]=wo1[5:7]
            month[i]=wo1[8:11]
            year[i]=wo1[12:16]
        return render(request,'registration/outpassdetails.html',{'values2':roo,'details':det1,'rollno':srollno,"values3":cal1,"date":date,"month":month,"year":year,"abc":cal1,"res":deta2})
@csrf_exempt
def home2(request):
    ostatus=request.GET.get('ostatus')
    data={"oid":oid,"ostatus":ostatus}
    token = requests.post("https://outpassapp.herokuapp.com/setoutpassstatus",data,headers = {'Authorization':f'Bearer {l}'})
    return redirect('login_successful')
def set(request):
    setpass=request.GET.get('setoutpasses')
    data={"srollno":srollno,"value":setpass}
    resp1=requests.post('https://outpassapp.herokuapp.com/setoutpassesleft',data,headers = {'Authorization':f'Bearer {l}'})
    data1={"srollno":srollno}
    data2={"oid":oid}
    det=requests.get('https://outpassapp.herokuapp.com/studentdetails',data1,headers = {'Authorization':f'Bearer {l}'})
    ro=requests.get('https://outpassapp.herokuapp.com/getpendingnoofpassesleft',data1,headers = {'Authorization':f'Bearer {l}'})
    cal=requests.get('https://outpassapp.herokuapp.com/getpasseshistory',data1,headers = {'Authorization':f'Bearer {l}'})
    det2=requests.get('https://outpassapp.herokuapp.com/outpassdetails',data2,headers = {'Authorization':f'Bearer {l}'})
    roo=ro.json()
    det1=det.json()
    cal1=cal.json()
    deta2=det2.json()
    date={}
    month={}
    year={}
    for i in range(len(cal1)):
            wo=cal1[i]
            wo1=wo['odate']
            date[i]=wo1[5:7]
            month[i]=wo1[8:11]
            year[i]=wo1[12:16]
    return render(request,'registration/setoutpass.html',{'values2':roo,'details':det1,'rollno':srollno,"values3":cal1,"date":date,"month":month,"year":year,"abc":cal1,"res":deta2})

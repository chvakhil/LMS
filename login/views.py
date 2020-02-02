from django.utils import timezone

from .forms import create_user_form, user_login_form
import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from werkzeug.utils import redirect

from LMS.settings import BASE_DIR
from login.models import AnnualLeaves,SickLeaves,WorkFromHomes,Leaves
from django.contrib.auth.models import User,auth


def show_base(request):
    form_value = user_login_form()
    return render(request, 'User_Login_Page.html', {'login_form': form_value})

def login(request):
    form_value = user_login_form()
    return render(request,'User_Login_Page.html',{'login_form':form_value})
def login_request(request):
    uname = request.POST['uname']
    pwd = request.POST['pwd']
    check =  auth.authenticate(username=uname,password=pwd)
    try:
        user_details = User.objects.get(username=uname)
    except:
        messages.info(request,'User Not Found!!!')
        form_value = user_login_form()
        return render(request, 'User_Login_Page.html', {'login_form': form_value})
    if check is not None:
        auth.login(request,check)
        data = User.objects.get(username=uname)
        data.last_login = timezone.now()
        data.save()
        # annual_leaves_data = AnnualLeaves.objects.get(USERNAME=uname)
        # sick_leaves_data = SickLeaves.objects.get(USERNAME=uname)
        # WorkFromHomes_data = WorkFromHomes.objects.get(USERNAME=uname)
        total_leaves_data = Leaves.objects.get(USERNAME=uname)
        return render(request,"after_login.html", {'name':user_details,'leaves':total_leaves_data})
    else:
        messages.info(request,"Username and Passwords does not matched")
        form_value = user_login_form()
        return render(request, 'User_Login_Page.html', {'login_form': form_value})
def create_user(request):
    form = create_user_form()
    return render(request,'user_create.html',{'form':form})
def create(request):
    form = create_user_form(request.POST)
    if form.is_valid():
        uname = form.cleaned_data['uname']
        fname = form.cleaned_data['fname']
        lname = form.cleaned_data['lname']
        pwd = form.cleaned_data['pwd1']
        pwd2 = form.cleaned_data['pwd2']
        email = form.cleaned_data['email']
        a_leaves = form.cleaned_data['a_leaves']
        s_leaves = form.cleaned_data['s_leaves']
        wfh_leaves = form.cleaned_data['wfh_data']
        if pwd == pwd2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'User already Exists')
                form = create_user_form()
                return render(request, 'user_create.html', {'form': form})
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Exists')
                form = create_user_form()
                return render(request, 'user_create.html', {'form': form})
            else:
                User.objects.create_user(username=uname,password=pwd,email=email,first_name=fname,last_name=lname).save()
                Leaves(USERNAME=uname,TOTAL_ANNUAL_LEAVES=a_leaves,TOTAL_SICK_LEAVES=s_leaves,TOTAL_WFH=wfh_leaves).save()
                print("User Created")
                messages.info(request,'User has been created, Please use the given credentials to login')
                form_value = user_login_form()
                return render(request, 'User_Login_Page.html', {'login_form': form_value})
        else:
            print("Passwords not matched!!!")
            messages.info(request, 'Passwords Not Matched')
            form = create_user_form()
            return render(request, 'user_create.html', {'form': form})


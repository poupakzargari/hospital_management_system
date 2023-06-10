from django.shortcuts import render,redirect,reverse
from . import forms ,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.db.models import Q



def aboutus_view(request):
    return render(request,'hospital/aboutus.html')
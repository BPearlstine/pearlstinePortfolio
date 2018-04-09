from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from blog.models import Blog
from jobs.models import Job
import logging

logger = logging.getLogger(pearlstinePortfolio.accounts.views)

@login_required(login_url="/accounts/login")
def profile(request):
    current_user = request.user
    logger.info("loading Profile for user %s", current_user)
    return render(request, 'accounts/profile.html',{'current_user':current_user})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        logger.info("Attempting to login in %s", user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            logger.info("Username or Password is incorrect")
            return render(request,'accounts/login.html',{'error':'Username or Password is incorrect.'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

from django.shortcuts import render,redirect
from blog.models import Blog
from .models import Job
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blog = Blog.objects.latest('id')
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs,'blog':blog})

@login_required(login_url="/accounts/login")
def newJob(request):
    if request.method == 'POST':
        if request.POST['jobSummary'] and request.POST['jobDetail'] and request.FILES['jobImage']:
            job = Job()
            job.summary = request.POST['jobSummary']
            job.moreInfo = request.POST['jobDetail']
            job.image = request.FILES['jobImage']
            job.save()
            return redirect('home')
        else:
            return render(request, 'jobs/newJob.html',{'error': 'All fields must be filled out.'})
    else:
        return render(request, 'jobs/newJob.html')

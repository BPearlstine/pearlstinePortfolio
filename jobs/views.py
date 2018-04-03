from django.shortcuts import render
from blog.models import Blog
from .models import Job

# Create your views here.
def home(request):
    blog = Blog.objects.latest('id')
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs,'blog':blog})

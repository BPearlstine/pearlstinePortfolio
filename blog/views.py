from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogHome(request):
    blogs = Blog.objects
    return render(request,'blog/blogHome.html', {'blogs':blogs})

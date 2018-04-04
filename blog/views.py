from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def blogHome(request):
    blogs = Blog.objects
    return render(request,'blog/blogHome.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})

@login_required(login_url="/accounts/login")
def newJob(request):
    if request.method == 'POST':
        if request.POST['blogTitle'] and request.POST['blogBody'] and request.FILES['blogImage']:
            blog = Blog()
            blog.title = request.POST['blogTitle']
            blog.body = request.POST['blogBody']
            blog.image = request.FILES['blogImage']
            blog.save()
            return redirect('home')
        else:
            return render(request, 'blog/newBlog.html',{'error': 'All fields must be filled out.'})
    else:
        return render(request, 'blog/newBlog.html')

from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def blogHome(request):
    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list, 5)

    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    return render(request,'blog/blogHome.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    logger.info("Blog Detail for: %s", blog.title)
    return render(request, 'blog/detail.html', {'blog':blog})

@login_required(login_url="/accounts/login")
def newBlog(request):
    if request.method == 'POST':
        logger.info("Constructing new blog")
        if request.POST['blogTitle'] and request.POST['blogBody'] and request.FILES['blogImage']:
            blog = Blog()
            blog.title = request.POST['blogTitle']
            logger.info("New blog title: %s", blog.title)
            blog.body = request.POST['blogBody']
            logger.info("New blog body: %s", blog.body )
            blog.image = request.FILES['blogImage']
            logger.info("New blog image: %s", blog.image.url)
            blog.pub_date = timezone.datetime.now()
            logger.info("New blog pub_date: %s", blog.pub_date)
            blog.save()
            return redirect('home')
        else:
            return render(request, 'blog/newBlog.html',{'error': 'All fields must be filled out.'})
    else:
        return render(request, 'blog/newBlog.html')

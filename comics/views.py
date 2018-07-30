from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comic
from .forms import AddComicForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def comicHome(request):
    comics = Comic.objects.all()
    form = AddComicForm()
    return render(request, 'comics/comicHome.html', {'comics':comics,'form':form})

def comicDetail(request, comic_id):
    comic = get_object_or_404(Comic, pk=comic_id)
    return render(request, 'comics/comicDetail.html', {'comic': comic})

def updateComic(request, comic_id):
    comic = get_object_or_404(Comic, pk=comic_id)
    if request.POST['comicTitle']:
        comic.title = request.POST['comicTitle']
    if request.POST['comicIssue']:
        comic.issue = request.POST['comicIssue']
    if request.POST['comicPublisher']:
        comic.publisher = request.POST['comicPublisher']
    if request.POST['comicGraded']:
        comic.graded = request.POST['comicGraded']
    if request.POST['comicKey']:
        comic.key = request.POST['comicKey']
    comic.save()
    return redirect('comicDetail', comic.id)

@login_required(login_url="/accounts/login")
def addComic(request):
    logger.info("begin add comic")
    if request.POST:
        form = AddComicForm(request.POST)
        comic = Comic()
        if form.is_valid():           
            comic.title = form.cleaned_data['title']
            comic.issue = form.cleaned_data['issue']
            comic.publisher = form.cleaned_data['publisher']
            comic.graded = form.cleaned_data['graded']
            comic.key = form.cleaned_data['key']
            comic.save()
        return redirect('comics:comicDetail',comic.id)

    else:
        return render(request, 'comics/comicHome.html', {'error':'All values must be filled out'})

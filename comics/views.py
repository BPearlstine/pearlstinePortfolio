from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Comic
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def comicHome(request):
    comics = Comic.objects.all()
    return render(request, 'comics/comicHome.html', {'comics':comics})

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
    if request.POST['comicTitle'] and request.POST['comicIssue'] and request.POST['comicPublisher'] and request.POST['comicGraded'] and request.POST['comicKey']:
        for comic in Comic.objects.all():
            if comic.title == request.POST['comicTitle'] and comic.issue == request.POST['comicIssue']:
                return redirect('comicDetail',comic.id)
        comic = Comic()
        comic.title = request.POST['comicTitle']
        comic.issue = request.POST['comicIssue']
        comic.publisher = request.POST['comicPublisher']
        comic.graded = request.POST['comicGraded']
        comic.key = request.POST['comicKey']
        comic.save()
        return redirect('comicDetail',comic.id)

    else:
        return render(request, 'comics/comicHome.html', {'error':'All values must be filled out'})

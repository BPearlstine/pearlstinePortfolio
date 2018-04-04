from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Comic

# Create your views here.
def comicHome(request):
    comics = Comic.objects
    return render(request, 'comics/comicHome.html', {'comics':comics})

def comicDetail(request,comic_id):
    comic = get_object_or_404(Comic, pk=comic_id)
    return render(request, 'comics/comicDetail.html',{'comic':comic})

@login_required(login_url="/accounts/login")
def addComic(request):
    if request.POST['comicTitle'] and request.POST['comicIssue'] and request.POST['comicGraded'] and request.POST['comicKey']:
        for comic in Comic.objects.all():
            if comic.title == request.POST['comicTitle'] and comic.issue == request.POST['comicIssue']:
                return redirect('comicDetail',comic.id)
        comic = Comic()
        comic.title = request.POST['comicTitle']
        comic.issue = request.POST['comicIssue']
        comic.graded = request.POST['comicGraded']
        comic.key = request.POST['comicKey']
        comic.save()
        return redirect('comicDetail',comic.id)

    else:
        return render(request, 'comics/comicHome.html', {'error':'All values must be filled out'})

from django.shortcuts import render
from cards.models import Card
from books.models import Book
from comics.models import Comic
# Create your views here.
def collections(request):
    latest_cards = Card.objects.all().order_by('-id')[:3]
    latest_books = Book.objects.all().order_by('-id')[:3]
    latest_comics = Comic.objects.all().order_by('-id')[:3]
    return render(request, 'myCollections/collections.html',{'latest_cards':latest_cards, 'latest_books':latest_books, 'latest_comics':latest_comics})

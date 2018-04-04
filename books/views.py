from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Book

# Create your views here.
def bookHome(request):
    books = Book.objects
    return render(request, 'books/bookHome.html', {'books':books})

def bookDetail(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/bookDetail.html',{'book':book})

@login_required(login_url="/accounts/login")
def addBook(request):
    if request.POST['bookTitle'] and request.POST['bookAuthor'] and request.POST['bookGenre'] and request.POST['bookIsbn']:
        for book in Book.objects.all():
            if book.isbn == request.POST['bookIsbn']:
                return redirect('bookDetail',book.id)
        book = Book()
        book.title = request.POST['bookTitle']
        book.author = request.POST['bookAuthor']
        book.genre = request.POST['bookGenre']
        book.isbn = request.POST['bookIsbn']
        book.save()
        return redirect('bookDetail',book.id)

    else:
        return render(request, 'book/bookHome.html', {'error':'All values must be filled out'})

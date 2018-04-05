from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def bookHome(request):
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 5)

    page = request.GET.get('page')
    books = paginator.get_page(page)
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

def bookSearch(request):
    books = Book.objects.all()
    searchItem = request.POST['bookSearchTerm'].upper()
    matchingBooks = []
    for book in books:
        if searchItem in book.title.upper() or searchItem in book.author.upper() or searchItem in book.genre.upper() or searchItem in book.isbn.upper():
            matchingBooks.append(book)
    if not matchingBooks:
        return render(request, 'books/bookSearchResults.html', {'isEmpty': 'Sorry we could not find any matching books'})
    else:
        return render(request, 'books/bookSearchResults.html', {'matchingBooks': matchingBooks})

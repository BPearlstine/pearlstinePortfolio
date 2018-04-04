from django.shortcuts import render

# Create your views here.
def hangman(request):
    return render(request, 'hangman/hangman.html')

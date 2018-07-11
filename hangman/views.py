from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def hangman(request):
    return render(request, 'hangman/hangman.html')

def beginGame(request):
    word = 'hangman'
    count = len(word)
    data = {
        'word': word,
        'count': count
    }

    return JsonResponse(data)


def checkLetter(request):
    letter = request.GET['letter']
    word = request.GET['word']
    if letter in word: 
        innerText = ''
               
        data = {
            'innerText': letter
        }
    else:
        data = {
            'noLuck': 'sucks to suck'
        }

    return JsonResponse(data)
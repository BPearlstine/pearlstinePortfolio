from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import re

# Create your views here.
def hangman(request):
    return render(request, 'hangman/hangman.html')

def beginGame(request):
    word = 'hangman'
    count = len(word)
    letters = list(word)

    data = {
        'word': word,
        'count': count,
        'letters': letters
    }

    return JsonResponse(data)


def checkLetter(request):
    word = request.GET['word']
    letter = request.GET['letter']
    letters = set(request.GET['letters'])
    chances = request.GET['chances']
    inner = request.GET['innerText']
    print(str(inner))
    inner = inner[:-1]
    dash = inner.split(",")
    print(str(dash))
    if letter in word: 
        letters = list(word)
        letters = set(letters) - set(letter)
        letters = list(letters)
        for match in re.finditer(letter,word):
            index = match.start()
            dash[index] = letter
        innerText = str(dash)
        innerText = innerText[1:-1]
        data = {
            'correct': True,
            'innerText': innerText,
            'letters': letters
        }
    else:
        chances = int(chances) - 1
        data = {
            'correct': False,
            'chances': chances
        }

    return JsonResponse(data)
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
    letters = request.GET['letters']
    chances = request.GET['chances']
    inner = request.GET['innerText']
    letters = letters.split(",")
    print("Letters " + str(letters))
    print("Inner Text " + str(inner))
    inner = inner[:-1]
    dash = list(inner)
    print("Dash after split " + str(dash))
    if letter in word: 
        print("Checking letter vs letters")
        newLetters = [char for char in letters if char != letter]
        letters = newLetters
        print("Letters after " + str(letters))
        # for match in re.finditer(letter,word):
        #     index = match.start()
        #     dash[index] = letter
        indexes = [i for i, e in enumerate(word) if e == letter]
        print(str(indexes))
        print("Dash " + str(dash))
        for index in indexes:
            print(str(index))
            dash[index] = letter
        print("Dash before replace " + str(dash))
        innerText = str(dash)
        innerText = innerText[1:-1]
        innerText = innerText.replace("'", " ")
        innerText = innerText.replace(",", " ")
        print("Dash after " + innerText)
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

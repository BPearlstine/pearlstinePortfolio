from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hangman, name='hangman'),
    path('ajax/beginGame', views.beginGame, name='ajax/beginGame'),
    path('ajax/checkLetter', views.checkLetter, name='checkLetter'),
]

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Card
import requests
import time

# Create your views here.
def cardHome(request):
    cards = Card.objects
    return render(request, 'cards/cardHome.html', {'cards':cards})

def cardDetail(request,card_id):
    card = get_object_or_404(Card, pk=card_id)

    payload = {'q':card.name,'order':card.set}
    r = requests.get('https://api.scryfall.com/cards/search', params=payload)
    time.sleep(0.1)
    r_json = r.json()['data'][0]['image_uris']['small']
    return render(request, 'cards/cardDetail.html',{'card':card,'r_json':r_json})

@login_required(login_url="/accounts/login")
def addCard(request):
    if request.POST['cardName'] and request.POST['cardSet'] and request.POST['cardArtist'] and request.POST['cardQuantity']:
        for card in Card.objects.all():
            if card.name == request.POST['cardName'] and card.set == request.POST['cardSet']:
                card.quantity += int(request.POST['cardQuantity'])
                card.save()
                return redirect('cardDetail',card.id)
        card = Card()
        card.name = request.POST['cardName']
        card.set = request.POST['cardSet']
        card.artist = request.POST['cardArtist']
        card.quantity = request.POST['cardQuantity']
        card.save()
        return redirect('cardDetail',card.id)

    else:
        return render(request, 'cards/cardHome.html', {'error':'All values must be filled out'})

def cardSearch(request):
    cards = Card.objects.all()
    searchItem = request.POST['cardSearchItem'].upper()
    matchingCards = []
    for card in cards:
        if searchItem in card.name.upper() or searchItem in card.set.upper() or searchItem in card.artist.upper():
            matchingCards.append(card)
    if not matchingCards:
        return render(request, 'cards/cardSearchResults.html', {'isEmpty': 'Sorry we could not find any matching cards'})
    else:
        return render(request, 'cards/cardSearchResults.html', {'matchingCards': matchingCards})

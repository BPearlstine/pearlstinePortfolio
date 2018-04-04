from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Card

# Create your views here.
def cardHome(request):
    cards = Card.objects
    return render(request, 'cards/cardHome.html', {'cards':cards})

def cardDetail(request,card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/cardDetail.html',{'card':card})

@login_required(login_url="/accounts/login")
def addCard(request):
    if request.POST['cardName'] and request.POST['cardSet'] and request.POST['cardArtist'] and request.POST['cardQuantity']:
        foundCard = False
        for card in Card.objects.all():
            if card.name == request.POST['cardName'] and card.set == request.POST['cardSet']:
                card.quantity += int(request.POST['cardQuantity'])
                card.save()
                foundCard = True
                return redirect('cardDetail',card.id)
        if foundCard != True:
            card = Card()
            card.name = request.POST['cardName']
            card.set = request.POST['cardSet']
            card.artist = request.POST['cardArtist']
            card.quantity = request.POST['cardQuantity']
            card.save()
            return redirect('cardDetail',card.id)

    else:
        return render(request, 'cards/cardHome.html', {'error':'All values must be filled out'})

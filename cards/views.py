from django.shortcuts import render, get_object_or_404
from .models import Card
# Create your views here.
def cardHome(request):
    cards = Card.objects
    return render(request, 'cards/cardHome.html', {'cards':cards})

def cardDetail(request,card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/cardDetail.html',{'card':card})

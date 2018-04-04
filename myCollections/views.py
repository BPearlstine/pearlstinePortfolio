from django.shortcuts import render
from cards.models import Card
# Create your views here.
def collections(request):
    latest_cards = Card.objects.all().order_by('-id')[:3]
    return render(request, 'myCollections/collections.html',{'latest_cards':latest_cards})

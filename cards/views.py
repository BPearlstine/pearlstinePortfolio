from django.shortcuts import render, get_object_or_404
from .models import Card
# Create your views here.
def cardDetail(request,card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'card/cardDetail.html',{'card':card})
    

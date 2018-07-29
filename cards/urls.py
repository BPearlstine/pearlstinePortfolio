from django.urls import path, include
from . import views

app_name = "cards"

urlpatterns = [
    path('', views.cardHome, name='cardHome'),
    path('<int:card_id>/', views.cardDetail, name='cardDetail'),
    path('addCard/', views.addCard, name='addCard'),
    path('results/', views.cardSearch, name='cardSearch'),
    path('update/<int:card_id>/', views.updateCard, name='updateCard'),
]

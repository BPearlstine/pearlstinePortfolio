from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cardHome, name='cardHome'),
    path('<int:card_id>/', views.cardDetail, name='cardDetail'),
    path('addCard/', views.addCard, name='addCard'),
]

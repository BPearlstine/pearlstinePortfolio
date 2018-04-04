from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:card_id>/', views.cardDetail, name='cardDetail'),
]

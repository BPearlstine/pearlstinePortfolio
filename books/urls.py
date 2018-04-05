from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bookHome, name='bookHome'),
    path('<int:book_id>/', views.bookDetail, name='bookDetail'),
    path('addBook/', views.addBook, name='addBook'),
    path('results/', views.bookSearch, name='bookSearch'),
]

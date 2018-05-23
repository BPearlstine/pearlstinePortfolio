from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.comicHome, name='comicHome'),
    path('<int:comic_id>/', views.comicDetail, name='comicDetail'),
    path('addComic/', views.addComic, name='addComic'),
    path('results/', views.comicSearch, name='comicSearch'),
    path('update/<int:comic_id>/', views.updateComic, name='updateComic'),
]

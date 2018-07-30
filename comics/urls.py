from django.urls import path, include
from . import views

app_name = 'comics'

urlpatterns = [
    path('', views.comicHome, name='comicHome'),
    path('detail/<int:comic_id>/', views.comicDetail, name='comicDetail'),
    path('addComic/', views.addComic, name='addComic'),
    path('update/<int:comic_id>/', views.updateComic, name='updateComic'),
]

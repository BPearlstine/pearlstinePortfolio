from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('<int:blog_id>/', views.detail, name='detail')
]

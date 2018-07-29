from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('blog/newBlog/', views.newBlog, name='newBlog'),
]

"""pearlstinePortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf .urls.static import static
import jobs.views
import hangman.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('jobs/newJob', jobs.views.newJob, name='newJob'),
    path('hangman/', hangman.views.hangman, name='hangman' ),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('cards/', include('cards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

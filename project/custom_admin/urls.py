from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import adminsite

urlpatterns = [
    path('', adminsite, name='adminsite'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

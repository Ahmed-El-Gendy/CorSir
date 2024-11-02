from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import adminsite, manage_courses, manage_usercourses

urlpatterns = [
    path('', adminsite, name='adminsite'),
    path('manage-courses/', manage_courses, name='manage_courses'),
    path('manage-usercourses/', manage_usercourses, name='manage_usercourses'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

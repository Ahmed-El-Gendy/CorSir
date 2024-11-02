from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import adminsite, manage_courses, manage_usercourses, manage_users, add_user , edit_course, delete_course , edit_user, delete_user, make_user_admin, manage_user_courses, add_user_course, edit_user_course, delete_user_course


urlpatterns = [
    path('', adminsite, name='adminsite'),
    path('manage-courses/', manage_courses, name='manage_courses'),
    path('manage-usercourses/', manage_usercourses, name='manage_usercourses'),
    path('manage-users/', manage_users, name='manage_users'),
    path('add-user/', add_user, name='add_user'),
    path('edit-course/<int:course_id>/', edit_course, name='edit_course'),
    path('delete-course/<int:course_id>/', delete_course, name='delete_course'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
     path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
     path('make-admin/<int:user_id>/', make_user_admin, name='make_user_admin'),
     path('manage-usercourses/', manage_user_courses, name='manage_usercourses'),
    path('add-usercourse/', add_user_course, name='add_user_course'),
    path('edit-usercourse/<int:user_course_id>/', edit_user_course, name='edit_user_course'),
    path('delete-usercourse/<int:user_course_id>/', delete_user_course, name='delete_user_course'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import adminhome, userhome, login, index, custom_logout, userdata, course_detail, done, course_search, course_table, save_user_courses, add_course, course_search, course_table, save_user_courses, list_courses
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', userhome, name='userhome'),
    path('userdata/<int:user_id>/', userdata, name='userdata'),
    path('course/<int:id>/', course_detail, name='course_detail'),
    path('course_table/', course_table, name='course_table'),
    path('save-user-courses/<int:id>/', save_user_courses, name='save_user_courses'),
    path('done/<int:id>/', done, name='done'),
    path('manger/', index, name='index'),
    path('adminhome/', adminhome, name='adminhome'),
    path('login/', login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('search/', course_search, name='course_search'),
    path('add-course/', add_course, name='add_course'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

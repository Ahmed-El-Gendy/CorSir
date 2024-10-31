from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import adminhome, userhome, login, index, custom_logout, c1, c2, c3, done1, done2, done3, userdata, course_detail, done
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', userhome, name='userhome'),
    path('userdata/<int:user_id>/', userdata, name='userdata'),
    path('course/<int:id>/', course_detail, name='course_detail'),
    path('done/<int:id>/', done, name='done'),
    path('done1/', done1, name='done1'),
    path('done2/', done2, name='done2'),
    path('done3/', done3, name='done3'),
    path('c1/', c1, name='c1'),
    path('c2/', c2, name='c2'),
    path('c3/', c3, name='c3'),
    path('manger/', index, name='index'),
    path('adminhome/', adminhome, name='adminhome'),
    path('login/', login, name='login'),
    path('logout/', custom_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

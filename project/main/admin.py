from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import adminhome, userhome, login
from django.contrib.auth.views import LogoutView
from .models import Course, UserCourse, Admin

admin.site.register(Course)
admin.site.register(UserCourse)
admin.site.register(Admin)


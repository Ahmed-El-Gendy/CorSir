from django.shortcuts import render
from main.models import Course, UserCourse, Admin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm


@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()
    return render(request, 'admin/add_course.html', {'form': form})

@login_required
def adminsite(request):
    return render(request, 'adminsite.html')

@login_required
def manage_courses(request):
    courses = Course.objects.all()
    return render(request, 'manage_courses.html', {'courses': courses})

@login_required
def manage_usercourses(request):
    user_courses = UserCourse.objects.all()
    return render(request, 'manage_usercourses.html', {'user_courses': user_courses})


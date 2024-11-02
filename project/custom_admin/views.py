from django.shortcuts import render
from main.models import Course, UserCourse, Admin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from .forms import UserCourseForm 


@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

@login_required
def adminsite(request):
    return render(request, 'adminsite.html')

@login_required
def manage_courses(request):
    courses = Course.objects.all()
    return render(request, 'manage_course.html', {'courses': courses})

@login_required
def manage_usercourses(request):
    user_courses = UserCourse.objects.all()
    return render(request, 'manage_usercourses.html', {'user_courses': user_courses})

@login_required
def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserCreationForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('manage_courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('manage_courses')
    return render(request, 'delete_course.html', {'course': course})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')
    return render(request, 'delete_user.html', {'user': user})

@login_required
def make_user_admin(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        if not Admin.objects.filter(user=user).exists():
            Admin.objects.create(user=user)
            return redirect('manage_users')
        else:
            return render(request, 'make_admin.html', {
                'user': user,
                'error': 'This user is already an admin.'
            })
    return render(request, 'make_admin.html', {'user': user})

@login_required
def manage_user_courses(request):
    user_courses = UserCourse.objects.all()
    return render(request, 'manage_usercourses.html', {'user_courses': user_courses})

@login_required
def add_user_course(request):
    if request.method == 'POST':
        form = UserCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_usercourses')
    else:
        form = UserCourseForm()
    return render(request, 'add_user_course.html', {'form': form})

@login_required
def edit_user_course(request, user_course_id):
    user_course = get_object_or_404(UserCourse, id=user_course_id)
    if request.method == 'POST':
        form = UserCourseForm(request.POST, instance=user_course)
        if form.is_valid():
            form.save()
            return redirect('manage_usercourses')
    else:
        form = UserCourseForm(instance=user_course)
    return render(request, 'edit_user_course.html', {'form': form})

@login_required
def delete_user_course(request, user_course_id):
    user_course = get_object_or_404(UserCourse, id=user_course_id)
    if request.method == 'POST':
        user_course.delete()
        return redirect('manage_usercourses')
    return render(request, 'delete_user_course.html', {'user_course': user_course})

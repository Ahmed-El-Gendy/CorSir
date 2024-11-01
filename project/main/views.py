from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Admin, UserCourse, Course
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request):
    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    admin_usernames = Admin.objects.select_related('user').values_list('user__username', flat=True)
    modified_users = User.objects.exclude(username__in=admin_usernames)
    modified_users = list(enumerate(modified_users))
    users = []

    for idx, val in modified_users:
        if idx % 2 == 0:
            users.append((0, val))
        else:
            users.append((1, val))

    data = {
        'manger': manger,
        'users': users,
    }

    if manger == 1:
        return render(request, 'index.html', data)
    else:
        return redirect('/')


def userhome(request):
    if not request.user.is_authenticated:
        return render(request, 'userhome.html', {})

    usercourses = UserCourse.objects.filter(user=request.user).select_related('course')
    usercourse_data = []
    for usercourse in usercourses:
        usercourse_data.append({
            'id': usercourse.course.id,
            'course_title': usercourse.course.title,
            'course_image': usercourse.course.image.url if usercourse.course.image else None,
            'done': usercourse.done,
        })

    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    data = {
        'manger': manger,
        'usercourses': usercourse_data,
    }
    return render(request, 'userhome.html', data)


@login_required
def adminhome(request):
    courses = Course.objects.all()
    users = User.objects.all()
    usercourses = UserCourse.objects.all()
    data = {'courses': courses, 'users': users, 'usercourses': usercourses}
    return render(request, 'adminhome.html', data)


def login(request):
    userform = CustomLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('userhome')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': userform})


def custom_logout(request):
    logout(request)
    return redirect('/')


@login_required
def course(request):
    courses = Course.objects.all()
    users = User.objects.all()
    usercourses = UserCourse.objects.all()

    data = {'courses': courses, 'users': users, 'usercourses': usercourses}
    return render(request, 'adminhome.html', data)

@login_required
def userdata(request, user_id):
    check = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        check = 1
    if check == 0:
        redirect('/')
    courses = Course.objects.all()
    user_course = UserCourse.objects.filter(user=user_id)
    user_course = list(enumerate(user_course))
    users = []

    for idx, val in user_course:
        if idx % 2 == 0:
            users.append((0, val))
        else:
            users.append((1, val))

    employee = User.objects.get(id=user_id)

    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    user_core = UserCourse.objects.filter(user=user_id).select_related('course')
    user_course_ids = user_core.values_list('course_id', flat=True)
    data = {'user_course': users, 'employee': employee, 'manger': manger, 'courses': courses, 'user_course_ids': user_course_ids}
    return render(request, 'userdata.html', data)


def course_detail(request, id):
    coursedata = get_object_or_404(Course, id=id)

    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    context = {
        'course': coursedata,
        'manger': manger,
    }
    return render(request, 'coursebase.html', context)


@login_required
def course_search(request):
    query = request.GET.get('course_name')

    try:
        course_title = Course.objects.get(title=query)
    except Course.DoesNotExist:
        return render(request, 'notfound.html')

    manager = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manager = 1

    return render(request, 'coursebase.html', {'course': course_title, 'manager': manager})


def done(request, id):
    user_course = UserCourse.objects.get(user=request.user, course__id=id)
    user_course.done = True
    user_course.save()
    return redirect('/')


def course_table(request):
    courses = Course.objects.all()
    return render(request, 'course_table.html', {'courses': courses})


def save_user_courses(request, id):
    if request.method == 'POST':
        selected_courses = request.POST.getlist('courseSelect')
        user_courses = UserCourse.objects.filter(user=id)

        existing_course_ids = set(user_courses.values_list('course_id', flat=True))
        print(existing_course_ids)
        curent_user = User.objects.get(id=id)
        for course_id in selected_courses:
            if int(course_id) not in existing_course_ids:
                curent_course = Course.objects.get(id=course_id)
                UserCourse.objects.create(user=curent_user, course=curent_course)

        for user_course in user_courses:
            if str(user_course.course.id) not in selected_courses:
                user_course.delete()

        return redirect('index')
    return HttpResponseBadRequest("Invalid request")
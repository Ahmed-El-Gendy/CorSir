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
        'usercourses': usercourse_data,  # Updated data
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
            # admins = Admin.objects.all()
            # if user in admins:
            #    return redirect('adminhome')
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
def c1(request):
    courses = Course.objects.all()
    users = User.objects.all()
    usercourses = UserCourse.objects.all()

    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    data = {'courses': courses, 'users': users, 'usercourses': usercourses, 'manger': manger }
    return render(request, 'course.html', data)


@login_required
def c2(request):
    courses = Course.objects.all()
    users = User.objects.all()
    usercourses = UserCourse.objects.all()

    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    data = {'courses': courses, 'users': users, 'usercourses': usercourses, 'manger': manger}
    return render(request, 'course2.html', data)


@login_required
def c3(request):
    courses = Course.objects.all()
    users = User.objects.all()
    usercourses = UserCourse.objects.all()

    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1

    data = {'courses': courses, 'users': users, 'usercourses': usercourses, 'manger': manger}
    return render(request, 'course3.html', data)


@login_required
def done1(request):
    # Get the course with ID 1 for the logged-in user
    user_course = UserCourse.objects.get(user=request.user, course__id=1)

    # Mark the course as done
    user_course.done = True
    user_course.save()

    # Optionally, send a success message
    messages.success(request, 'Course marked as done successfully!')
    return redirect('/')


@login_required
def done2(request):
    # Get the course with ID 1 for the logged-in user
    user_course = UserCourse.objects.get(user=request.user, course__id=2)

    # Mark the course as done
    user_course.done = True
    user_course.save()

    # Optionally, send a success message
    messages.success(request, 'Course marked as done successfully!')
    return redirect('/')


@login_required
def done3(request):
    # Get the course with ID 1 for the logged-in user
    user_course = UserCourse.objects.get(user=request.user, course__id=3)

    # Mark the course as done
    user_course.done = True
    user_course.save()

    # Optionally, send a success message
    messages.success(request, 'Course marked as done successfully!')
    return redirect('/')


@login_required
def userdata(request, user_id):
    # Get the course with ID 1 for the logged-in user

    check = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        check = 1

    if check == 0:
        redirect('/')

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

    data = {'user_course': users, 'employee': employee, 'manger': manger}
    # Optionally, send a success message
    messages.success(request, 'Course marked as done successfully!')
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
    course_title = Course.objects.get(title=query)
    print(course_title)
    manger = 0
    admins = Admin.objects.filter(user=request.user)
    if admins.exists():
        manger = 1
    
    return render(request, 'coursebase.html', {'course': course_title, 'manager': manger})

def done(request, id):
    user_course = UserCourse.objects.get(user=request.user, course__id=id)
    user_course.done = True
    user_course.save()
    return redirect('/')

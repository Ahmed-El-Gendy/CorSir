from django.shortcuts import render
from main.models import Course, UserCourse, Admin
from django.http import HttpResponse, HttpResponseRedirect


def adminsite(request):
    return render(request, 'adminsite.html')

# forms.py
from django import forms
from main.models import Course, UserCourse, Admin

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class UserCourseForm(forms.ModelForm):
    class Meta:
        model = UserCourse
        fields = '__all__'



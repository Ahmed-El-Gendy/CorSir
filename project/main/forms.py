from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Course


class CustomLoginForm(forms.Form):
    """generate form for login"""
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class CourseForm(forms.ModelForm):
    """generate form for course"""
    class Meta:
        model = Course
        fields = ['title', 'description', 'image', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

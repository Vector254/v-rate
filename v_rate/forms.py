from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Rate, Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['id','profile_picture','bio',]

class ProjectPostForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ('id','image', 'title', 'link', 'description',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design', 'usability', 'content']




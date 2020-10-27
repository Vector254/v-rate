from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Projects, Rate

# Create your views here.

def index(request):
    return render(request, 'index.html')

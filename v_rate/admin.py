from django.contrib import admin
from .models import Profile, Projects, Rate

# Register your models here.
admin.site.register(Projects)
admin.site.register(Profile)
admin.site.register(Rate)

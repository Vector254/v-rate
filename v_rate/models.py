from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    projects = models.ForeignKey('Project', on_delete=models.CASCADE,null=True, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Project(models.Model):
    title = models.CharField(max_length=155)
    link = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)

    def __str__(self):
        return f'{self.title}'

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

   


    

class Rate(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='ratings', null=True)

    def __str__(self):
        return f'{self.project} Rating'

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings


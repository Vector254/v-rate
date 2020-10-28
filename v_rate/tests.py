from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(id=1, username='test', password='test123')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.project = Project.objects.create(id=1, title='test project', image='default.png', description='This is a test project',
                                        user=self.user, link='https://github.com/Vector254/v-rate.git')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_projects(self):
        self.project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_search_project(self):
        self.project.save()
        project = Project.search_project('test')
        self.assertTrue(len(project) > 0)

    def test_delete_project(self):
        self.project.delete_project()
        project = Project.search_project('test')
        self.assertTrue(len(project) < 1)


class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.project = Project.objects.create(id=1, title='test project', image='default.png', description='this is a test project',
                                        user=self.user, link='https://github.com/Vector254/v-rate.git')
        self.rate = Rate.objects.create(id=1, design=3, usability=4, content=7, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rate))

    def test_save_rate(self):
        self.rate.save()
        rate = Rate.objects.all()
        self.assertTrue(len(rate) > 0)

    
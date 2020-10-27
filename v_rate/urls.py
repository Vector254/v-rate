from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('register/', views.register, name='register'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/', views.profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


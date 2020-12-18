from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


app_name = 'myapp'

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    path('', login_required(views.Home.as_view()), name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('upload', views.upload, name='upload'),
    # path('home', views.home, name='home'),
    # url(r'^signout/$', views.signout, name="signout"),
]


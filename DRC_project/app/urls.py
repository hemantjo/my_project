from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    # url(r'^signout/$', views.signout, name="signout"),
]


from django.urls import path

from .views import users_signin

app_name = 'users'
urlpatterns = [
    path('signin', users_signin, name='signin'),
]
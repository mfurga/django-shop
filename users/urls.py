from django.urls import path

from .views import users_signin, users_signup, users_logout

app_name = 'users'
urlpatterns = [
    path('signin', users_signin, name='signin'),
    path('signup', users_signup, name='signup'),
    path('logout', users_logout, name='logout')
]
